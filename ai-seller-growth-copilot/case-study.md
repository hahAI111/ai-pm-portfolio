# AI Seller Growth Copilot

## Executive Summary

An independent AI product prototype for cross-border marketplace sellers. It turns fragmented performance signals into an explainable diagnosis and a prioritized action plan, then measures whether the seller completed the recommended work. The prototype uses synthetic data and does not claim production business results.

## Product Decision

Sellers do not need another dashboard. They need help deciding what to do next. The MVP focuses on one narrow hypothesis: evidence-backed recommendations will help sellers complete higher-value growth actions than metrics alone.

## Product Flow

1. Ingest seller sales, sessions, conversion, ROAS, listing, price, and inventory signals.
2. Diagnose the likely blocker with deterministic rules.
3. Explain the evidence and confidence.
4. Generate a ranked action plan with effort and target metric.
5. Require seller approval; track completion and feedback.
6. Compare post-action metrics in a clearly labeled outcome simulation.

## Why This Is an AI Product

Structured business facts and diagnosis rules remain deterministic. Azure AI Foundry is used for natural-language explanation and response drafting. This keeps the model away from unsupported causal claims and automatic marketplace changes.

## Project Overview
AI Seller Growth Copilot is an AI product concept for cross-border marketplace sellers. It helps sellers diagnose growth blockers, understand why performance changed, and take prioritized actions across listing quality, conversion, advertising efficiency, and seller growth.

## Role
Product Manager / AI Product Strategy

## Target Users
- Growth-stage cross-border sellers
- New sellers who need structured launch guidance
- Account managers supporting seller growth at scale

## Problem
Sellers often see sales decline but cannot quickly identify the cause. Standard dashboards show metrics, but they do not explain what changed, why it matters, or which action should be taken first. This creates slow decision-making, repeated manual support, and missed growth opportunities.

## Product Hypothesis
If sellers receive personalized, evidence-backed, and prioritized AI recommendations, they will complete more high-impact growth actions and improve conversion and advertising efficiency faster than sellers using standard dashboards alone.

## Solution
The Copilot combines structured seller performance data, marketplace knowledge, and LLM-generated recommendations to produce a clear action plan.

### Core Capabilities
1. Growth diagnosis
2. Evidence-backed explanation
3. Listing optimization recommendations
4. Advertising efficiency suggestions
5. Weekly prioritized action plan
6. Outcome tracking after seller actions

## Example Use Case
A home organization seller sees weekly sales drop by 18%. Sessions are stable at +2%, but conversion rate drops by 21%. The Copilot identifies conversion as the main blocker, explains the evidence, and recommends improving the product title, updating the first two bullet points, testing a promotion, and pausing low-converting ad keywords.

## AI Design
The system uses a hybrid AI approach:

- Rule-based diagnosis for structured performance signals
- Retrieval-augmented generation for marketplace knowledge grounding
- LLM-generated seller-facing explanations and action plans
- Feedback loop to track accepted recommendations and business outcomes

## AI Boundary and Evaluation Design

Seller metrics and growth-blocker rules are deterministic because they are structured business facts. Azure AI Foundry turns the evidence into concise seller-facing explanations. A production knowledge experience would retrieve approved marketplace guidance, cite sources, and separately evaluate retrieval quality, groundedness, action completion, business impact, and safety.

## Success Metrics

| Metric | Purpose |
|---|---|
| First recommended action completion rate | Measures whether sellers act on the advice |
| Recommendation acceptance rate | Measures relevance and trust |
| Conversion rate uplift | Measures business impact |
| ROAS improvement | Measures advertising efficiency |
| Time to diagnose issue | Measures productivity gain |
| Seller satisfaction score | Measures seller confidence |

## Guardrails
- Confidence level for every diagnosis
- Human review for policy-sensitive or high-impact actions
- Source-grounded marketplace guidance
- Tracking of incorrect recommendation rate and seller complaints

## Product Trade-offs
The MVP prioritizes trust over automation. Instead of automatically changing listings or ads, the Copilot explains the issue, recommends actions, and asks sellers to approve changes. This reduces risk while building seller confidence.

## Stakeholder Collaboration Plan

| Stakeholder | Need or concern | PM interaction | Shared decision / metric |
|---|---|---|---|
| Sellers | Clear, trustworthy next actions | Interviews, beta feedback, in-product helpfulness feedback | Action completion and seller satisfaction |
| Account Managers | Faster, consistent portfolio diagnosis | Workflow co-design and pilot review | Diagnosis time and seller coverage |
| Data / Engineering | Feasible inputs and reliable results | Data-availability review and MVP scoping | Minimum data threshold and diagnosis accuracy |
| Operations | Recommendations that can be executed | Launch-readiness walkthroughs | Completion rate and escalation workflow |
| Policy / Legal | Avoid harmful or unsupported changes | Guardrail review and approval gates | Escalation recall and incorrect recommendation rate |
| Leadership | Measurable seller-growth ROI | Business-case and roadmap reviews | Conversion lift, ROAS lift, and adoption |

## Cross-functional Decision Story

The initial request could be framed as an AI assistant that automatically changes seller listings and advertising settings. The PM recommendation is to avoid that launch scope. Account managers gain efficiency from a single diagnostic view, while data and engineering teams can first validate rules against available seller signals. Policy stakeholders require human review for sensitive guidance. The MVP therefore delivers evidence-backed recommendations and seller approval, then uses acceptance, completion, conversion, and escalation data to decide whether to expand automation.

## Launch Plan

1. Validate the problem with sellers and account managers; agree on top diagnosis scenarios.
2. Run a data and engineering readiness review; set a minimum data-quality threshold.
3. Review guardrails with operations and policy stakeholders; define mandatory human escalation.
4. Pilot with one seller segment and a small account-manager cohort.
5. Evaluate action completion, conversion movement, satisfaction, complaints, and escalation recall against a standard dashboard control.
6. Review results with leadership before category expansion.

## Roadmap

### Phase 1: MVP
Growth diagnosis, listing recommendations, and action plan generation.

### Phase 2: Personalization
Seller segmentation by maturity, category, and performance pattern.

### Phase 3: Experimentation
Track accepted actions and measure downstream business impact.

### Phase 4: Workflow Integration
Integrate recommendations into seller tools and account manager workflows.

## Resume-ready Impact Statement
Designed an AI Seller Growth Copilot for cross-border marketplace sellers, defining seller lifecycle pain points, MVP scope, AI solution design, success metrics, experimentation plan, and product roadmap to improve seller growth actions, conversion, and advertising efficiency.

## Interview Pitch
I designed an AI Seller Growth Copilot to address a common marketplace problem: sellers can see performance metrics, but they often do not know why growth is slowing or what action to take first. I mapped the seller lifecycle, identified conversion and advertising efficiency as high-impact pain points, and designed an MVP that uses rule-based diagnosis, retrieval-augmented marketplace guidance, and LLM-generated action plans. I also defined success metrics, guardrails, and an A/B test plan to measure seller action completion and business impact.
