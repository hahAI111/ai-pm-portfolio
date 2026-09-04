# Next-Phase Portfolio Roadmap

This roadmap defines the remaining work required to evolve the current local MVPs into a public, production-style AI Product Manager portfolio. All delivery claims will remain clearly labeled as independent portfolio work using synthetic data.

## 1. Public Interactive Deployment

### Goal
Give recruiters a browser-accessible version of the Seller Growth Copilot without exposing credentials.

### Recommended Design

- Static portfolio front end hosted on GitHub Pages.
- A dedicated Azure Function API for LLM requests and protected server-side configuration.
- Azure AI Foundry credential stored only as an Azure application setting or managed secret.
- Rate limiting, request validation, telemetry, and a public-data-only policy.

### Definition of Done

- Public portfolio landing page has a working demo link.
- Azure OpenAI key is never sent to the browser or committed to GitHub.
- API allows only safe seller-growth and support-draft scenarios using synthetic data.
- Basic usage cap and error logging are enabled.

### Product Trade-off
An interactive demo increases credibility but also creates model-usage cost and abuse risk. A public endpoint should expose a limited, read-only demo—not account, listing, price, or advertising actions.

## 2. Production-Style RAG: Hybrid Search, Reranking, and Citations

### Goal
Evolve Support Automation from category-based local retrieval into a source-grounded knowledge experience.

### Target Flow

1. Ingest approved seller-support documents.
2. Parse, clean, and structure content by section and topic.
3. Create semantic chunks with source metadata.
4. Retrieve candidate passages through hybrid keyword and vector search.
5. Rerank candidates before passing a small context set to the LLM.
6. Generate a grounded response with citations.
7. Escalate policy-sensitive, low-confidence, or unsupported requests.
8. Evaluate retrieval, generation, product outcomes, and safety separately.

### Definition of Done

- Every generated support response includes one or more source citations.
- Retrieval evaluation reports Recall@K and Precision@K on a small golden query set.
- Generation evaluation covers groundedness, completeness, and citation correctness.
- Product dashboard tracks draft acceptance, rewrite rate, handling time, and escalation recall.

### Technical PM Message
“Retrieval optimizes recall; reranking improves precision. I measure whether evidence was found separately from whether the model used it safely.”

## 3. Narrated Demo Video

### Goal
Create a 60–90 second recruiter-friendly walkthrough with English narration and burned-in English captions.

### Planned Storyline

| Segment | Content | Purpose |
|---|---|---|
| Opening | Global Seller Growth AI Portfolio | Establish the product theme |
| Opportunity Discovery | Score and prioritize seller segments | Demonstrate business judgment |
| Growth Copilot | Diagnose blocker and recommend actions | Demonstrate AI product workflow |
| Support Automation | Retrieve guidance and escalate policy risks | Demonstrate trustworthy AI design |
| Close | Python, Streamlit, Azure AI Foundry, guardrails | Summarize technical depth |

### Definition of Done

- English voiceover aligns with the existing captions.
- Video avoids personal data, secrets, browser history, and non-synthetic seller data.
- Final MP4 is attached to a GitHub Release and linked in the README.

## 4. Portfolio PDF

### Goal
Create a concise English PDF that a recruiter can read in under five minutes.

### Planned Pages

1. Portfolio cover and positioning.
2. Unified seller-lifecycle product narrative.
3. AI Seller Growth Copilot: problem, MVP, metrics, and safety boundary.
4. Marketplace Opportunity Discovery: scoring and roadmap decision.
5. AI Seller Support Automation: RAG roadmap and human-in-the-loop controls.
6. Stakeholder collaboration, technical PM approach, links to GitHub and demo video.

### Definition of Done

- PDF uses only verified portfolio statements and synthetic-data disclosures.
- Includes QR codes or clickable links to GitHub and the demo video.
- Rendered pages are visually checked before publishing.

## 5. English Resume Update

### Proposed Section

**Independent AI Product Portfolio Projects — Global Seller Growth**

- Built three working AI product MVPs covering marketplace opportunity discovery, seller-growth diagnosis, and seller-support automation using Python, Streamlit, and Azure AI Foundry.
- Defined product hypotheses, MVP boundaries, stakeholder collaboration plans, and measurement frameworks across action completion, conversion, ROAS, support quality, and safety escalation.
- Designed clear AI control boundaries: deterministic logic for structured facts and policy decisions; Azure AI Foundry for grounded explanation and response drafting; human review for policy-sensitive or high-impact scenarios.
- Portfolio: https://github.com/hahAI111/ai-pm-portfolio | Demo: https://github.com/hahAI111/ai-pm-portfolio/releases/tag/v1.0-portfolio-demo

### Definition of Done

- Project section is added to the English resume without implying employment at Amazon or any other company.
- GitHub and demo video links are clickable in the exported resume PDF.
- Resume remains limited to verified claims: independent work, synthetic data, and demonstrable implementation.

## Recommended Execution Order

1. Update the English resume and create the Portfolio PDF.
2. Produce narrated demo video.
3. Build the RAG upgrade locally with evaluation data and citations.
4. Deploy a restricted public demo once the Azure hosting design, cost cap, and API protections are approved.
