# AI Seller Support Automation

Working Streamlit MVP for a seller-support AI workflow.

## Features
- Select sample seller tickets.
- Classify ticket intent with transparent keyword-based logic.
- Retrieve category-specific guidance from a local knowledge base.
- Draft seller responses without requiring an external API key.
- Flag policy-sensitive questions for required human review.
- Record agent feedback and calculate a draft acceptance rate.

## Run locally

```powershell
pip install -r requirements.txt
streamlit run app.py --server.port 8503
```
