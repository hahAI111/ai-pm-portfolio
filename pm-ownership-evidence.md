# PM Ownership Evidence Plan

## Honest Current Position

The three applications in this repository are **independent prototypes using synthetic data**. They demonstrate problem framing, MVP scoping, technical product judgment, AI boundaries, stakeholder design, and evaluation planning. They do not claim a production launch, real-user adoption, realized ROI, or marketplace operating results.

## Evidence Ladder

| Stage | Evidence | Current portfolio status |
|---|---|---|
| 1. Opportunity | Persona, JTBD, baseline problem evidence, alternatives | Partially documented |
| 2. Investment decision | Sizing, cost assumptions, priority rationale, decision log | Needs stronger artifacts |
| 3. Prototype | Working workflow, synthetic or de-identified test data, offline evaluation | Completed for three MVPs |
| 4. Controlled pilot | Authorized real users, baseline, telemetry, feedback | Not yet started |
| 5. Scale / iterate / stop | Decision based on adoption, value, safety, and unit economics | Not yet available |

## Portfolio Opportunity Portfolio

| Opportunity | User and JTBD | Why now | AI fit | Decision | Evidence to build next |
|---|---|---|---|---|---|
| Seller Growth Copilot | Seller needs to identify the highest-value growth action | Fragmented performance signals slow action | Language explanation and grounded advice add value; diagnosis remains deterministic | Prototype complete | Opportunity brief, offline evaluation, controlled pilot plan |
| Seller Support Automation | Support agent needs consistent, safe drafts for repeated questions | Repeated triage and drafting can create operational load | Classification, retrieval, and drafting; escalation remains deterministic | Prototype complete | Golden dataset, citation design, agent reviewer study |
| Marketing Lead Discovery RAG | Marketing or BD reviewer needs a qualified, source-supported lead profile | Closest alignment to Marketing AI roles | RAG can synthesize authorized public sources with reviewer approval | Proposed next build | ICP, source policy, value model, evaluation rubric |

## Required Artifacts Before Calling a Project a Pilot

1. **Opportunity Brief** - persona, JTBD, baseline evidence, alternatives, and chosen problem.
2. **Business Case** - expected value, build cost, runtime cost, reviewer cost, and sensitivity range.
3. **PRD** - workflow, requirements, non-goals, acceptance criteria, and owners.
4. **Architecture and Data Flow** - data boundaries, retrieval, model boundary, identity, approvals, and audit.
5. **Golden Dataset** - representative synthetic or authorized de-identified cases with expected output and SME rubric.
6. **Telemetry Plan** - adoption, quality, cost, and guardrail event definitions.
7. **Pilot Charter** - population, duration, training, baseline, success gates, and stop criteria.
8. **Scale / Iterate / Stop Memo** - a decision only after evidence is collected.

## Business Case Formulas

### Seller Support Automation

Estimated annual net value:

$$
	ext{Eligible tickets} 	imes 	ext{adoption} 	imes 	ext{time saved per accepted draft} 	imes 	ext{agent hourly value}
- 	ext{model cost} - 	ext{review cost} - 	ext{maintenance cost}
$$

### Seller Growth Copilot

Estimate value through time to first action, accepted recommendations, repeated diagnostic work avoided, and only then downstream conversion or ROAS change. Do not claim incremental revenue until a controlled design supports attribution.

## Decision Gates

| Decision | Required evidence |
|---|---|
| Scale | Quality and safety gate passes; repeat usage; measurable value; acceptable unit economics; operational readiness |
| Iterate | User-value signal exists, but trust, workflow, latency, cost, or quality prevents expansion |
| Stop | Weak problem, low adoption, unsafe boundary, unavailable data, poor economics, or deterministic tooling is better |

## Resume Rule

Describe the current work as **Independent AI Product Portfolio Projects** and as **prototypes**. Add pilot, adoption, ROI, or launch claims only when they are supported by actual authorized evidence.
