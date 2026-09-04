# AI Product Manager Portfolio: Global Seller Growth

Three independent, working product MVPs for AI Product Manager roles in cross-border marketplace, seller growth, and operational automation.

> **Portfolio note:** All datasets, metrics, outcomes, and recommendations in this repository are synthetic demonstrations. They are not Amazon data, production systems, or claimed business results.

## Watch the Demo

[Watch or download the captioned 63-second portfolio walkthrough](https://github.com/hahAI111/ai-pm-portfolio/releases/download/v1.0-portfolio-demo/ai-pm-portfolio-demo-captioned.mp4) · [Watch the narrated version](https://github.com/hahAI111/ai-pm-portfolio/releases/download/v1.0-portfolio-demo/ai-pm-portfolio-demo-narrated.mp4) · [View the release](https://github.com/hahAI111/ai-pm-portfolio/releases/tag/v1.0-portfolio-demo)

[Download the AI PM Portfolio Casebook PDF](./output/pdf/AI_PM_Portfolio_Casebook.pdf)

## Portfolio Projects

| Project | PM Question Addressed | Working MVP | Core Evidence |
|---|---|---|---|
| [AI Seller Growth Copilot](./ai-seller-growth-copilot/) | How can sellers diagnose growth blockers and act faster? | [App](./ai-seller-growth-copilot/app/) | AI diagnosis, prioritized actions, feedback loop, outcome simulation |
| [Marketplace Opportunity Discovery Dashboard](./marketplace-opportunity-dashboard/) | Which seller segments and problems should the product roadmap prioritize? | [App](./marketplace-opportunity-dashboard/app/) | Opportunity sizing, scoring, prioritization, initiative recommendation |
| [AI Seller Support Automation](./ai-seller-support-automation/) | How can AI improve support efficiency safely? | [App](./ai-seller-support-automation/app/) | Ticket triage, retrieval, response drafting, escalation guardrails |
| [Marketing Lead Discovery RAG](./marketing-lead-discovery-rag/) | How can marketing research produce source-supported lead profiles? | [App](./marketing-lead-discovery-rag/app/) | Hybrid retrieval, reranking, citations, ICP scoring, offline evaluation |

## Product Narrative

The projects connect into one seller-lifecycle product story:

```mermaid
flowchart LR
    A[Opportunity Discovery] --> B[Seller Growth Copilot]
    B --> C[Seller Support Automation]
    C --> D[Feedback and Outcome Learning]
    D --> A
```

1. **Opportunity Discovery** identifies high-value segments and execution gaps.
2. **Growth Copilot** helps sellers understand blockers and complete high-impact actions.
3. **Support Automation** scales safe, consistent help for seller questions.
4. **Feedback and outcomes** inform prioritization and improve product quality.

## Skills Demonstrated

- Product discovery and customer problem framing
- Marketplace seller lifecycle analysis
- PRD and MVP scoping
- Roadmap and product prioritization
- Metrics, A/B testing, and outcome measurement
- AI workflow design: rules, retrieval, generated response drafts, and feedback loops
- AI safety: explainability, confidence, human approval, and escalation
- Python, Streamlit, pandas, CSV-based data workflows

## Supporting Materials

- [Architecture and AI Safety](./architecture.md)
- [Interview Guide](./interview-guide.md)
- [Technical PM Logbook](./technical-pm-logbook.md)
- [Next-Phase Roadmap](./next-phase-roadmap.md)
- [PM Ownership Evidence Plan](./pm-ownership-evidence.md)

The logbook also includes portfolio-specific answers on rules versus LLMs, MVP RAG boundaries, safe agent autonomy, and quality/safety expansion criteria.
- [Growth Copilot Case Study](./ai-seller-growth-copilot/case-study.md)
- [Opportunity Dashboard Case Study](./marketplace-opportunity-dashboard/case-study.md)
- [Support Automation Case Study](./ai-seller-support-automation/case-study.md)
- [Deployment Guide](./DEPLOYMENT.md)

## Screenshots and Demo Recording

Before publishing, run each app locally and capture one dashboard screenshot. Add the images under a screenshots directory and link them here. A short demo video should show data input, the core insight, a recommended action, and feedback or a safety control.

## Run the Apps Locally

### Prerequisites

```powershell
python -m pip install streamlit pandas
```

### 1. AI Seller Growth Copilot

```powershell
cd ai-seller-growth-copilot/app
streamlit run app.py --server.port 8501
```

### 2. Marketplace Opportunity Discovery Dashboard

```powershell
cd marketplace-opportunity-dashboard/app
streamlit run app.py --server.port 8502
```

### 3. AI Seller Support Automation

```powershell
cd ai-seller-support-automation/app
streamlit run app.py --server.port 8503
```

## Verify the Decision Logic

The portfolio includes lightweight unit tests for the diagnosis, prioritization, and safety logic.

```powershell
./run-tests.ps1
```

## Suggested Resume Framing

**Independent AI Product Portfolio Projects — Global Seller Growth**

- Built three working AI product MVPs for marketplace seller growth, opportunity discovery, and safe seller-support automation.
- Applied product discovery, transparent prioritization, AI workflow design, evaluation metrics, and human-in-the-loop guardrails.

## Repository Structure

```text
portfolio/
├── ai-seller-growth-copilot/
├── marketplace-opportunity-dashboard/
└── ai-seller-support-automation/
```
