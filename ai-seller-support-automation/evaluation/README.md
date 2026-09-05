# Synthetic Scenario Evaluation

This is an AI-authored, offline evaluation of the actual deterministic Seller Support Automation engine. It is **not a real-user study, autonomous LLM user simulation, customer pilot, or business-impact measurement**. No cloud model or API credentials are needed.

## Goal

Test the product hypothesis that a user can describe a support problem naturally and receive an appropriate next step. This baseline only measures routing and explicit workflow signals, not end-to-end resolution. It deliberately exposes the gap between drafting an answer and helping a user finish a task.

## Reproduce

From the repository root, using Python with pandas installed:

```powershell
python -m unittest discover -s ai-seller-support-automation/evaluation -p "test_*.py"
python ai-seller-support-automation/evaluation/run_evaluation.py
```

The evaluator imports the real `classify_ticket`, `retrieve_guidance`, and `draft_response` functions. It records complete deterministic outputs in `baseline/results.json` and generates `baseline/report.md`. It does not substitute another model for the application. Reruns overwrite those reports; use `--output-dir` to keep a separate run.

Default exit code zero means the evaluator completed, **not** that all scenarios passed. Use `--fail-on-scenario-failure` for an acceptance gate. Infrastructure errors always fail the command.

## Protocol and rubric

- `scenarios.json` freezes 20 synthetic inputs and expected assertions before the first baseline run: seven controls and thirteen challenges.
- Exact category and escalation assertions check existing fields. `clarification_question`, `Unknown` / `Out of scope`, and `resolution_status` are proposed product contracts, not current capabilities.
- Follow-up and resolution examples are standalone capability probes, not actual multi-turn sessions.
- A passing category does not prove the advice is correct. A passing escalation flag does not prove a human received the request. Missing clarification or resolution state is reported as a capability gap.
- Cases are AI-authored with knowledge of the implementation; the rubric has not been independently approved by a domain expert. They are a discovery set, not a representative or held-out benchmark.
- Chinese support and typo tolerance are proposed requirements to prioritize or explicitly exclude, not promises that the current prototype already makes.
- No customer records, internal logs or private credentials are used. All test text is synthetic.

## Evidence and next decision

Read the [baseline report](baseline/report.md) for measured counts, failing cases, priorities and limitations. Original product logic is deliberately unchanged. Do not present this work as improved accuracy or a successful pilot.

Next: review expected behavior with a domain expert, select the smallest improvement, rerun this suite, and add independently authored unseen examples. Then test the optional model path, UI workflow and actual users separately. Do not infer user satisfaction, time savings, adoption, ROI or willingness to pay from these results.

## Interview framing

"I designed an initial synthetic scenario evaluation for my support prototype. I ran the actual rules-and-retrieval engine, separated existing-behavior controls from proposed capability tests, and used the failures to prioritize safer routing, clarification and resolution tracking. This was an offline baseline, not customer validation."