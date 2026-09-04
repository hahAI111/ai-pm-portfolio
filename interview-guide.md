# Interview Guide: Global Seller Growth AI Portfolio

## Unified 60-Second Story

I built three independent AI product MVPs around the cross-border seller lifecycle. First, the Marketplace Opportunity Discovery Dashboard helps a PM identify which seller segments and execution gaps are worth prioritizing. Second, the AI Seller Growth Copilot turns seller performance data into explainable diagnoses and ranked actions. Third, AI Seller Support Automation classifies repeated seller questions, retrieves grounded guidance, and escalates policy-sensitive cases to human reviewers. Across the portfolio, I focused on product discovery, measurable outcomes, transparent decision logic, and human-in-the-loop AI safety.

## Project 1: AI Seller Growth Copilot

### 60-Second Pitch
I designed and built an MVP for sellers who see declining performance but do not know which action to take first. The app loads seller metrics, identifies likely blockers such as conversion, traffic, listing quality, advertising, price, or inventory, and explains the evidence. It then generates a prioritized action plan, captures feedback, tracks completed actions, and illustrates how a PM could connect actions to business-outcome measurement. The key design choice was prioritizing explainability and seller approval over automatic changes.

**Why not let the LLM diagnose directly?** Structured performance diagnosis needs consistency and auditability. I use deterministic signals for the initial diagnosis, then generated language only for explanation and action-plan communication.

**What is the north-star metric?** Completed seller growth actions weighted by verified downstream business impact. Usage alone is insufficient.

## Project 2: Marketplace Opportunity Discovery Dashboard

### 60-Second Pitch
This MVP answers a roadmap question: with limited engineering capacity, where should a marketplace team invest? It combines GMV growth, conversion gaps, listing quality, advertising efficiency, inventory health, and return rate into a transparent opportunity score. The dashboard filters by category and region, shows an opportunity map, ranks the backlog, and recommends a corresponding product initiative. The PM value is moving from raw data to a defendable prioritization decision.

**How did you choose the weights?** They are explicit MVP heuristics. In production, I would calibrate them against historical intervention results and revisit them with finance and business stakeholders.

## Project 3: AI Seller Support Automation

### 60-Second Pitch
This MVP addresses repetitive seller-support work while keeping critical decisions safe. It classifies a seller ticket, retrieves relevant guidance from an approved local knowledge base, drafts a response, and sends policy-sensitive questions to human review. It also records agent feedback. AI assists with triage and drafting but does not make policy decisions or apply account changes.

**What is the key safety metric?** Escalation recall: the percentage of sensitive requests correctly routed to a human. It should be optimized alongside draft acceptance and handling-time reduction.

## Resume Positioning

Use the heading **Independent AI Product Portfolio Projects — Global Seller Growth**. Describe the work as portfolio MVPs with synthetic data; do not present simulated metrics as employment results.

## Cross-Functional Leadership Story

Use this answer when asked how the portfolio would work in a real organization:

I would begin by aligning the stakeholder system rather than treating the request as only an LLM feature. Sellers need useful and trustworthy actions. Seller-success and support teams need workflows that reduce repeated work. Data and engineering teams need feasible data boundaries and observable logic. Policy owners need escalation for sensitive decisions, while leadership needs measurable ROI. I would use a pilot to align these groups around shared metrics: action completion and business impact for adoption, quality and override rate for the operating teams, and escalation recall for safety. The rollout decision would depend on all three dimensions, not on usage alone.
