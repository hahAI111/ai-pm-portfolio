# Technical PM Logbook: AI Product Decisions

Original interview-preparation notes for explaining product impact, technical boundaries, trade-offs, and evaluation.

## 1. Decide Where AI Belongs

| Problem type | Preferred capability | Portfolio example |
|---|---|---|
| Natural-language ambiguity | LLM | Explain a seller growth blocker |
| Approved knowledge question | Retrieval plus LLM draft | Draft seller-support guidance |
| Structured fact | Data query or API | Sales, ROAS, inventory values |
| Explicit rule | Deterministic logic | Low-inventory and policy escalation |
| High-risk decision | Human approval | Policy-sensitive support request |

**Interview answer:** “I use AI for language understanding and explanation. Facts, policies, permissions, and high-risk actions remain controlled by deterministic systems.”

## 2. RAG: Four Product Layers

1. **Knowledge quality** — Is the source approved, current, and correctly scoped?
2. **Retrieval quality** — Can the system find the needed evidence?
3. **Generation quality** — Does the response faithfully use that evidence?
4. **Product quality** — Does the user complete the task better or faster?

| Concept | Plain explanation | PM decision |
|---|---|---|
| Chunking | Split source content into retrievable units | Use document structure and evaluation, not one fixed size |
| Embeddings | Represent semantic meaning for similarity search | Validate quality, languages, latency, and cost |
| Hybrid search | Exact keyword plus semantic retrieval | Preserve exact IDs, SKUs, and policy terms |
| Reranking | Reorder candidates by relevance | Retrieve for recall; rerank for precision |
| Groundedness | Claims are supported by evidence | Measure separately from source correctness |
| Citation | Show the source behind a claim | Treat as a trust feature |

**Interview answer:** “I evaluate retrieval and generation separately. An answer can fail because evidence was missing, ranked poorly, or ignored by generation.”

## 3. Evaluation, Latency, and Cost

| Layer | Example measures |
|---|---|
| Retrieval | Recall at K, precision at K, evidence relevance |
| Generation | Groundedness, completeness, citation accuracy |
| Product | Task completion, acceptance rate, time saved, adoption |
| Safety | Escalation recall, override rate, incorrect recommendation rate |

Latency depends on user context. The goal is sufficient evidence with minimal unnecessary context and cost.

## 4. Agent Controls

| Concern | Product control |
|---|---|
| Identity | Authenticate who makes the request |
| Authorization | Re-check backend permission and scope |
| Policy | Use deterministic eligibility rules |
| Tool safety | Allowlist tools and validate parameters |
| High risk | Human review and approval |
| Audit | Record actor, action, policy result, and outcome |

**Interview answer:** “The model can propose a plan, but it is not the source of truth for identity, authorization, policy eligibility, or irreversible actions.”

## 5. MVP and Prioritization

An MVP is the smallest usable product that validates the most important assumption, not the smallest feature list. Prioritize by customer pain, business value, confidence, risk, effort, and **incremental learning**.

**Interview answer:** “I compare incremental learning, not only engineering effort. I invest when a feature validates a critical unknown, and defer similar functionality after the core workflow is proven.”

## 6. Portfolio-Specific Technical Answers

### Why does the Seller Growth Copilot use both rules and an LLM?

Seller sales, sessions, conversion, inventory, and ROAS are structured facts. The MVP uses transparent rules to create a repeatable diagnosis and exposes evidence and confidence. Azure AI Foundry then improves the natural-language explanation. This separates factual diagnosis from language generation and makes the failure mode easier to evaluate.

### Is the Support Automation MVP already a full RAG system?

No. It is a retrieval-oriented MVP using a small approved knowledge base and category matching. The MVP validates whether grounded drafting and escalation improve support workflows. The next stage is a production RAG architecture with source ingestion, semantic chunking, hybrid search, reranking, citations, access controls, and layered evaluation.

### Why not make the Seller Growth Copilot an autonomous agent?

The MVP does not need dynamic tool execution to test its primary hypothesis: can evidence-backed recommendations help sellers select and complete better actions? Listing changes, pricing, and advertising updates may have business or policy impact, so they require explicit seller approval and future backend authorization. Agent autonomy should match the risk and reversibility of an action.

### How would you decide whether to expand the MVP?

I would require evidence across product value, quality, and safety. For example: recommendation acceptance and action completion show adoption; conversion or ROAS movement show business value; incorrect recommendation rate, escalation recall, and human overrides show safety. I would only expand the automation boundary when all three meet predefined thresholds.

### What is the highest-risk failure mode?

For Support Automation, a sensitive policy request could be incorrectly treated as low-risk and receive unsupported guidance. The design response is deterministic risk classification, conservative escalation, approved-source grounding, human review, and audit logging. For Growth Copilot, the risk is presenting a causal conclusion with more certainty than the data supports; the product therefore displays evidence, confidence, and advisory—not automatic—actions.
