# Portfolio Architecture and AI Safety

## Shared Product Architecture

Synthetic seller, marketplace, or ticket data flows through data validation, product-specific decision logic, a grounded recommendation or prioritization layer, human review or seller approval, and feedback/outcome measurement.

## Project Architecture

| Project | Inputs | Decision Logic | Output | Safety Control |
|---|---|---|---|---|
| Seller Growth Copilot | Seller performance CSV | Rule-based growth diagnosis | Prioritized actions and outcome simulation | Advisory-only actions and confidence display |
| Opportunity Discovery | Marketplace performance CSV | Transparent weighted opportunity score | Ranked roadmap backlog | Explainable scoring and clearly labeled synthetic data |
| Support Automation | Seller ticket and local knowledge base | Keyword triage and category retrieval | Response draft and escalation decision | Mandatory human review for policy-sensitive requests |

## Why Rules Before LLMs

The MVPs intentionally use transparent deterministic rules rather than claiming model intelligence that cannot be evaluated. This makes product logic testable, supports clear explanations to users, and provides a safe fallback when an LLM service is unavailable.

## Future LLM Integration

For production, retain deterministic validation and retrieval controls: classify intent and risk, route sensitive questions to a human review queue, retrieve approved knowledge for low-risk questions, generate a draft, validate the output and confidence, then collect feedback and evaluation data.

## AI Boundary Pattern Used in This Portfolio

The LLM is used for explanation and response drafting. Structured seller facts come from CSV data, diagnosis and policy escalation use deterministic logic, and external changes remain future human-approved actions. This mirrors a production design where models assist with uncertainty rather than replace factual, policy, or authorization controls.

## Retrieval Improvement Roadmap

The current support demo uses category-based retrieval from a local approved knowledge base. A production RAG version would add source ingestion, structure-aware chunking, hybrid retrieval, reranking, citations, and separate retrieval-versus-generation evaluation.

## Production Evaluation

- **Quality:** recommendation acceptance rate, agent draft acceptance rate, grounded-response accuracy.
- **Business:** action completion, conversion lift, ROAS lift, ticket deflection, handling-time reduction.
- **Safety:** escalation recall for sensitive tickets, incorrect recommendation rate, human override rate, user complaints.
