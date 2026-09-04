# PRD v2: AI Seller Growth Copilot

## 1. Executive Summary
AI Seller Growth Copilot helps cross-border marketplace sellers identify growth blockers and take prioritized actions. It combines seller performance data, marketplace guidance, and AI-generated recommendations to reduce diagnosis time and improve seller growth outcomes.

## 2. Customer Problem
Sellers often know that sales are slowing, but they do not know why. Existing dashboards show metrics, but they do not translate data into clear next steps. This creates delayed action, repeated account manager support, and missed growth opportunities.

## 3. Product Hypothesis
If sellers receive personalized, evidence-backed, and prioritized AI recommendations, they will complete more growth actions and improve conversion, ROAS, and listing quality faster than sellers using standard dashboards alone.

## 4. Target Users

### Primary: Growth-stage Seller
- Has enough sales data for diagnosis
- Wants to scale revenue and improve efficiency
- Needs practical recommendations, not generic education

### Secondary: New Seller
- Needs step-by-step guidance to improve listing quality and first-sale readiness

### Internal: Account Manager
- Needs scalable diagnosis across many sellers
- Wants consistent, data-backed seller coaching

## 5. User Needs
- Diagnose why performance changed
- Understand the evidence behind the diagnosis
- Know which action to take first
- Track whether the action worked
- Avoid policy or marketplace mistakes

## 6. MVP Features

### 6.1 Performance Summary
Shows recent changes in sales, traffic, conversion, ROAS, inventory, and listing quality.

### 6.2 Growth Blocker Diagnosis
Classifies the seller main blocker into traffic, conversion, listing quality, advertising efficiency, inventory, or pricing competitiveness issue.

### 6.3 Evidence-backed Explanation
Explains why the system selected a blocker, using simple data comparisons.

### 6.4 Prioritized Action Plan
Generates 3 to 5 actions ranked by impact, effort, and confidence.

### 6.5 Seller Knowledge Q&A
Answers seller questions using retrieved marketplace guidance and best practices.

## 7. Non-goals
- Automatically changing listings or ads without seller approval
- Replacing account managers
- Making final policy decisions
- Guaranteeing sales growth

## 8. Success Metrics

### Primary Metrics
- First recommended action completion rate
- Conversion rate uplift after accepted actions
- Recommendation acceptance rate

### Secondary Metrics
- Time to diagnose issue
- ROAS improvement
- Listing quality score improvement
- Weekly active sellers using Copilot

### Guardrail Metrics
- Incorrect recommendation rate
- Seller complaint rate
- Policy escalation rate
- Low-confidence response rate

## 9. MVP Launch Plan

### Pilot Segment
Start with growth-stage sellers in one category where there is enough traffic and sales history to measure impact.

### Rollout Steps
1. Internal account manager preview
2. Limited seller beta
3. A/B test against standard dashboard
4. Broader category expansion

## 10. Product Trade-offs

| Decision | Option A | Option B | Recommendation |
|---|---|---|---|
| Diagnosis engine | Pure LLM | Rules + LLM | Use rules for diagnosis and LLM for explanation |
| Launch audience | All sellers | Growth-stage sellers first | Start with growth-stage sellers |
| Action automation | Auto-apply changes | Seller approval required | Require seller approval |
| Success metric | Usage only | Usage + business impact | Track action completion and metric movement |

## 11. PM Judgment
The most important product decision is to make the Copilot trustworthy before making it powerful. Sellers need to understand why a recommendation is made. Therefore, the MVP should prioritize explainability, confidence, and measurable actions over full automation.
