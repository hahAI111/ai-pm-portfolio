# Marketing Lead Discovery RAG

Working source-grounded research MVP for marketing and business-development lead discovery.

## Features

- Uses synthetic approved-source company excerpts.
- Retrieves candidates with a transparent hybrid keyword and semantic-proxy score.
- Reranks a small evidence set before profile generation.
- Shows source dates and citations for every profile.
- Calculates a deterministic ICP fit score.
- Includes a synthetic golden query set with Recall@3 and Precision@3 evaluation.
- Requires human review before any outreach action.

## Run locally

```powershell
pip install -r requirements.txt
streamlit run app.py --server.port 8504
```

## Important Boundary

This is an independent portfolio prototype. Sources, companies, metrics, and results are synthetic demonstrations. It does not enrich personal data or contact leads.
