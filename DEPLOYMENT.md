# Deployment Guide

Each Streamlit application can be deployed independently from this GitHub repository using Streamlit Community Cloud.

## Repository

https://github.com/hahAI111/ai-pm-portfolio

## Deployments

Create one Streamlit Community Cloud app for each entry point below.

| App name | Main file path | Suggested public URL |
|---|---|---|
| AI Seller Growth Copilot | ai-seller-growth-copilot/app/app.py | ai-seller-growth-copilot.streamlit.app |
| Marketplace Opportunity Discovery | marketplace-opportunity-dashboard/app/app.py | marketplace-opportunity-dashboard.streamlit.app |
| AI Seller Support Automation | ai-seller-support-automation/app/app.py | ai-seller-support-automation.streamlit.app |

## Deployment Settings

- Repository: hahAI111/ai-pm-portfolio
- Branch: master
- Python version: Default supported version
- Main file: Use the specific path from the table above
- Secrets: None required for the current deterministic MVPs

## Post-deployment Verification

1. Growth Copilot: choose a seller, generate a recommendation, and mark an action complete.
2. Opportunity Discovery: filter by a category or region and confirm the ranked backlog updates.
3. Support Automation: classify a sample policy ticket and confirm human-review escalation.

## Portfolio Disclosure

Keep the synthetic-data disclosure visible in the repository README and case studies. Do not present demo metrics or outcome simulations as production performance.
