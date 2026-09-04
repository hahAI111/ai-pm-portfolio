# Portfolio Case Study: AI Seller Support Automation

## Problem
Seller-support teams spend significant time categorizing repeated questions, locating the right guidance, and drafting consistent responses. Automation must improve speed without allowing AI to make unsafe policy or account decisions.

## Solution
I built a working AI support MVP that classifies seller tickets, retrieves relevant knowledge-base guidance, drafts a seller-facing response, captures agent feedback, and routes policy-sensitive requests to human review.

## Product Design Principles
- Use transparent classification for predictable, high-volume requests.
- Ground response drafts in a curated knowledge base.
- Escalate policy-sensitive questions rather than presenting an uncertain answer.
- Measure draft acceptance, ticket deflection, handling time, and first-contact resolution.

## Stakeholder Collaboration Plan

| Stakeholder | Need or concern | PM interaction | Shared decision / metric |
|---|---|---|---|
| Sellers | Fast and understandable help | Analyze ticket themes and satisfaction feedback | First-contact resolution and CSAT |
| Support Agents | Fewer repetitive tasks without loss of control | Shadow workflow and draft-feedback pilot | Draft acceptance and handling time |
| Support Operations | Stable routing and capacity improvement | Define queues, service levels, and exception paths | Ticket deflection and escalation latency |
| Knowledge / Policy team | Only approved guidance is used | Content review and escalation taxonomy | Grounded-response accuracy and escalation recall |
| Engineering / AI team | Reliable integration and observable quality | Instrumentation, fallback, and error-review design | Availability, override rate, and classification accuracy |
| Leadership | Scalable cost-to-serve improvement | Pilot business-case review | Cost per contact and service quality |

## Cross-functional Decision Story

Support teams may prefer broad automation to reduce handling time, while policy stakeholders require caution on claims and compliance questions. The PM resolves this by separating low-risk triage and drafting from final policy decisions. The product automates classification and retrieval, surfaces a safe draft, and requires human review when risk signals are present. Agents provide acceptance and rewrite feedback that informs the next automation boundary.

## Launch Plan

1. Analyze high-volume ticket categories with support operations.
2. Define an approved knowledge base and escalation taxonomy with policy owners.
3. Pilot drafts with a small agent group; require review before sending every response.
4. Measure acceptance, rewrite, escalation recall, and handling-time changes.
5. Expand only low-risk categories that meet quality and safety thresholds.

## Resume Bullet
Designed and built an AI seller-support automation MVP that classified seller tickets, retrieved grounded guidance, drafted safe responses, captured quality feedback, and enforced human escalation for policy-sensitive requests.
