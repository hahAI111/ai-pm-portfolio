import argparse
import hashlib
import importlib.util
import json
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parent
APP = ROOT.parent / "app"
REPOSITORY = ROOT.parents[1]


def load_scenarios(path):
    scenarios = json.loads(path.read_text(encoding="utf-8"))
    expected_ids = [f"S{number:02}" for number in range(1, 21)]
    if [scenario["id"] for scenario in scenarios] != expected_ids:
        raise ValueError("Expected exactly 20 unique, ordered scenarios S01-S20")
    allowed = {"category", "escalation", "clarification", "unknown", "resolution_status"}
    for scenario in scenarios:
        if not scenario["expected"] or not set(scenario["expected"]) <= allowed:
            raise ValueError(f"Invalid assertions in {scenario['id']}")
        if not isinstance(scenario["input"], str) or not scenario["rationale"]:
            raise ValueError(f"Invalid scenario {scenario['id']}")
    return scenarios


def check_expectations(expected, classification):
    checks = []
    for name, target in expected.items():
        if name == "clarification":
            actual = bool(classification.get("clarification_question"))
        elif name == "unknown":
            actual = classification.get("category") in {"Unknown", "Out of scope"}
        else:
            actual = classification.get(name)
        checks.append({"check": name, "expected": target, "actual": actual, "passed": actual == target})
    return checks


def evaluate(scenarios, engine, knowledge):
    results = []
    for scenario in scenarios:
        classification = engine.classify_ticket(scenario["input"])
        guidance = engine.retrieve_guidance(knowledge, classification["category"])
        response = engine.draft_response(scenario["input"], classification, guidance)
        checks = check_expectations(scenario["expected"], classification)
        results.append({**scenario, "classification": classification, "guidance": guidance,
                        "response": response, "checks": checks,
                        "passed": all(check["passed"] for check in checks)})
    return results


def render_report(payload):
    results = payload["results"]
    total = len(results)
    passed = sum(result["passed"] for result in results)
    controls = [result for result in results if result["group"] == "control"]
    challenges = [result for result in results if result["group"] != "control"]
    lines = ["# Synthetic Support Evaluation: Baseline", "",
             "> AI-authored synthetic scenarios, not real users, a customer pilot, or observed business impact.", "",
             "## Run provenance", "",
             f"- UTC run: {payload['run_utc']}",
             f"- Source commit before evaluation artifacts: `{payload['source_commit']}`",
             f"- Python: {payload['python']}; pandas: {payload['pandas']}",
             "- Runtime model/provider: none. Actual deterministic support engine executed; no LLM judge or simulated browser user.",
             "- Content hashes identify the exact engine, knowledge and scenario inputs:"]
    lines.extend(f"  - `{name}`: `{digest}`" for name, digest in payload["sha256"].items())
    lines.extend(["", "## Observed results", "",
                  f"- Scenarios passing all defined assertions: **{passed}/{total}**.",
                  f"- Existing-behavior controls: **{sum(item['passed'] for item in controls)}/{len(controls)}**.",
                  f"- Proposed capability and robustness challenges: **{sum(item['passed'] for item in challenges)}/{len(challenges)}**.",
                  "- These counts are rubric-specific, not accuracy, customer task completion, or market-readiness estimates.", "",
                  "| ID | Group | Task | Result | Failed assertions (expected vs actual) |",
                  "|---|---|---|---|---|"])
    for result in results:
        failures = "; ".join(f"{check['check']}: {check['expected']!r} vs {check['actual']!r}"
                             for check in result["checks"] if not check["passed"])
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(f"| {result['id']} | {result['group']} | {result['task']} | {status} | {failures or '-'} |")
    lines.extend(["", "## Interpretation and limits", "",
                  "- Controls test current behavior; challenge cases deliberately probe proposed requirements. Missing capabilities are not mislabeled as regressions.",
                  "- Clarification requires a structured clarification_question signal; this is a proposed interface contract, not an existing field. Natural-language wording alone is not scored as proof.",
                  "- Resolution status is also a proposed interface. A missing field demonstrates a contract gap, not a measured customer outcome.",
                  "- Follow-up cases are standalone inputs: no claim of multi-turn simulation or memory evaluation is made.",
                  "- Escalation means a Boolean signal only. No actual handoff, approval, or ticket creation was tested.",
                  "- Replies and retrieved guidance are recorded, but semantic correctness, groundedness and instruction-injection resistance are not comprehensively scored.",
                  "- The optional cloud-model path, Streamlit UI, persistence, latency, cost and real-user usability were not tested.",
                  "- Scenarios and rubric were written with source visibility by one AI assistant. No independent SME approval, human review, randomized control, or held-out claim is made.",
                  "- Rule scores are not calibrated probabilities. Successful keyword controls do not validate the displayed confidence.", "",
                  "## Product decision: iterate before a customer pilot", "",
                  "1. P0: make risky-request detection independent of the winning category; review multilingual and bypass cases (S14-S16).",
                  "2. P1: provide explicit unknown and clarification paths; avoid routing missing information to Account (S08-S09, S13, S17).",
                  "3. P1: define conversation state, user-reported versus verified outcomes, and real handoff contracts (S18-S20).",
                  "4. P2: decide whether Chinese, misspellings and multi-intent prioritization belong in the first release; if excluded, communicate unsupported scope clearly (S10-S12).",
                  "5. Before changing implementation, review this rubric with a domain expert. Retest the same scenarios and separately authored unseen cases; report both improvements and regressions.", "",
                  "No product code was changed in this baseline. No before/after improvement is claimed.", "",
                  "## Raw evidence", "",
                  "See [results.json](results.json) for every input, rationale, classification, guidance, draft and assertion.", ""])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Run 20 synthetic support-engine scenarios without model calls.")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "baseline")
    parser.add_argument("--fail-on-scenario-failure", action="store_true")
    arguments = parser.parse_args()
    source = APP / "support_engine.py"
    specification = importlib.util.spec_from_file_location("portfolio_support_engine", source)
    engine = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(engine)
    scenario_path = ROOT / "scenarios.json"
    knowledge_path = APP / "seller_knowledge_base.csv"
    scenarios = load_scenarios(scenario_path)
    results = evaluate(scenarios, engine, pd.read_csv(knowledge_path))
    commit = subprocess.run(["git", "-C", str(REPOSITORY), "rev-parse", "HEAD"],
                            capture_output=True, text=True, check=True).stdout.strip()
    payload = {"run_utc": datetime.now(timezone.utc).isoformat(), "source_commit": commit,
               "python": platform.python_version(), "pandas": pd.__version__,
               "mode": "synthetic_deterministic_baseline",
               "sha256": {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                          for path in (source, knowledge_path, scenario_path)}, "results": results}
    arguments.output_dir.mkdir(parents=True, exist_ok=True)
    (arguments.output_dir / "results.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (arguments.output_dir / "report.md").write_text(render_report(payload), encoding="utf-8")
    passed = sum(result["passed"] for result in results)
    print(f"Executed {len(results)} scenarios: {passed} passed, {len(results) - passed} failed.")
    print(f"Report: {arguments.output_dir / 'report.md'}")
    return 1 if arguments.fail_on_scenario_failure and passed != len(results) else 0


if __name__ == "__main__":
    raise SystemExit(main())