# Interview Practice: 60-Second Answers

## Why this problem?

I started from a repeated user workflow rather than from a model capability. Sellers struggle to translate fragmented performance signals into an action; support agents repeatedly classify and draft responses; researchers repeatedly consolidate source evidence. I selected problems where better decisions or lower repetitive effort could be measured.

## Why AI?

AI is useful for ambiguity, unstructured language, synthesis, and explanation. I keep structured facts in APIs or data systems, explicit rules in deterministic logic, and high-risk decisions behind human approval. This avoids adding AI where a predictable workflow is sufficient.

## Why this MVP?

The MVP is the smallest usable product that tests the most important assumption. For the Growth Copilot, that assumption is whether evidence-backed recommendations help sellers choose and complete better actions. For Support Automation, it is whether grounded drafting improves speed without weakening policy safety. I intentionally excluded automatic account, listing, pricing, and advertising changes.

## What did you not build?

I did not build autonomous operational actions, broad personal-data enrichment, or production marketplace integrations. Those features require stronger authorization, policy review, source governance, monitoring, and authorized user evidence. Deferring them reduces risk while preserving the learning goal.

## How did you handle stakeholders?

I mapped sellers, operations, engineering, data, policy, finance, and leadership to different success criteria. Sellers need clarity and trust; operations needs an executable workflow; engineering needs feasible data boundaries; policy needs escalation controls; leadership needs measurable value. I use a pilot and shared gates rather than optimizing one stakeholder's metric in isolation.

## How did you measure success?

I separate retrieval quality, generation quality, product value, and safety. Metrics include Recall@K, Precision@K, groundedness, citation correctness, task completion, acceptance, time saved, repeat use, escalation recall, overrides, and unit cost. This lets me identify whether a failure came from missing evidence, poor ranking, weak generation, or low product value.

## When would you stop or scale?

I would scale only when quality and safety gates pass, users repeat the workflow, business value is measurable, and unit economics are acceptable. I would iterate when value exists but trust, quality, workflow, latency, or cost is blocking expansion. I would stop when the problem is weak, evidence is unavailable, the boundary is unsafe, or a deterministic tool is better.

## Honest Portfolio Framing

These are independent prototypes using synthetic data and offline evaluation. They demonstrate product and technical judgment; they do not claim production launch, real-user adoption, or realized ROI.
