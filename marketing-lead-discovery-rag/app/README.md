# Marketing Lead Discovery RAG

Working source-grounded research MVP for marketing and business-development lead discovery.

## Features

- Uses synthetic approved-source company excerpts.
- Retrieves candidates with a transparent hybrid keyword and semantic-proxy score.
- Reranks a small evidence set before profile generation.
- Shows source dates and citations for every profile.
- Calculates a deterministic ICP fit score.
- Includes a synthetic golden query set with Recall@3 and Precision@3 evaluation.
- Includes no-evidence and freshness cases to test refusal and source-quality behavior.
- Requires human review before any outreach action.
- Optionally uses Azure AI Foundry to draft a profile constrained to displayed citations.

## Run locally

```powershell
pip install -r requirements.txt
streamlit run app.py --server.port 8504
```

## Important Boundary

This is an independent portfolio prototype. Sources, companies, metrics, and results are synthetic demonstrations. It does not enrich personal data or contact leads.

## Azure AI Foundry Optional Configuration

Create a local .streamlit/secrets.toml file with endpoint, deployment, and API key values. That secrets file is ignored by Git. The app retains a deterministic cited fallback when model access is unavailable.
