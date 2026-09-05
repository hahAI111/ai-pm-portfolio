import json
import tempfile
import unittest
from pathlib import Path

from run_evaluation import ROOT, check_expectations, load_scenarios, render_report


class EvaluationHarnessTests(unittest.TestCase):
    def test_suite_contains_twenty_ordered_scenarios(self):
        self.assertEqual(len(load_scenarios(ROOT / "scenarios.json")), 20)

    def test_missing_clarification_is_not_a_pass(self):
        checks = check_expectations({"clarification": True}, {"category": "Account"})
        self.assertFalse(checks[0]["passed"])

    def test_unsafe_category_does_not_hide_failed_escalation(self):
        checks = check_expectations({"category": "Listing", "escalation": True},
                                    {"category": "Listing", "escalation": False})
        self.assertTrue(checks[0]["passed"])
        self.assertFalse(checks[1]["passed"])

    def test_unknown_and_resolution_require_explicit_state(self):
        self.assertTrue(check_expectations({"unknown": True}, {"category": "Unknown"})[0]["passed"])
        self.assertFalse(check_expectations({"resolution_status": "user_reported"}, {})[0]["passed"])

    def test_duplicate_scenario_is_rejected(self):
        scenarios = load_scenarios(ROOT / "scenarios.json")
        scenarios[-1]["id"] = scenarios[0]["id"]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "scenarios.json"
            path.write_text(json.dumps(scenarios), encoding="utf-8")
            with self.assertRaises(ValueError):
                load_scenarios(path)

    def test_report_counts_failed_assertions(self):
        payload = {"run_utc": "test", "source_commit": "test", "python": "test", "pandas": "test", "sha256": {},
                   "results": [{"id": "S01", "group": "control", "task": "test", "passed": False,
                                "checks": [{"check": "escalation", "expected": True, "actual": False, "passed": False}]}]}
        report = render_report(payload)
        self.assertIn("**0/1**", report)
        self.assertIn("escalation: True vs False", report)
        self.assertIn("not real users", report)


if __name__ == "__main__":
    unittest.main()