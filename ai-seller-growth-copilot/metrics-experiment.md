# Metrics and Experiment Plan

## North Star Metric
Seller growth actions completed per active seller, weighted by verified business impact.

## Success Metrics

| Category | Metric | Why It Matters |
|---|---|---|
| Adoption | Weekly active sellers using Copilot | Measures engagement |
| Activation | % sellers completing first recommended action | Measures first-value success |
| Business Impact | Conversion rate uplift | Measures seller growth |
| Business Impact | ROAS improvement | Measures ad efficiency |
| Efficiency | Time to diagnose issue | Measures productivity gain |
| Quality | Recommendation acceptance rate | Measures relevance |
| Trust | Seller satisfaction score | Measures user confidence |

## Guardrail Metrics
- Incorrect recommendation rate
- Policy escalation rate
- Seller complaint rate
- Low-confidence answer rate
- Human override rate

## A/B Test Design

### Hypothesis
Sellers who receive AI-generated prioritized action plans will complete more high-impact growth actions and improve conversion faster than sellers who only see standard dashboards.

### Test Groups
- Control: Standard performance dashboard
- Treatment: Dashboard + AI Seller Growth Copilot recommendations

### Primary Metrics
- Action completion rate
- Conversion rate change after 14 days
- Seller satisfaction score

### Launch Decision Criteria
Launch broadly if treatment improves action completion by at least 15%, without increased complaints or incorrect recommendations.
