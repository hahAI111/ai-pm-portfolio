# AI Seller Growth Copilot App

Working Streamlit MVP for diagnosing marketplace seller growth blockers.

## Features
- Select an included sample seller or upload a CSV of seller data.
- Diagnose likely traffic, conversion, listing, advertising, price, and inventory issues.
- Produce evidence-backed, prioritized actions.
- Display derived sales, sessions, and conversion trends.
- Ask the assistant a seller-growth question without requiring an external API key.
- Capture helpful / not-helpful feedback and calculate a demo recommendation acceptance rate.
- Track completed recommended actions and calculate an action completion rate for each seller.
- Simulate illustrative post-action conversion, ROAS, and sales outcomes.
- Download a CSV template directly from the app.

## Run locally

```powershell
pip install -r requirements.txt
streamlit run app.py
```

## CSV requirements
Use one row per seller with these headers:

```text
seller_id,category,weekly_sales,sales_change_pct,sessions,sessions_change_pct,conversion_rate,conversion_change_pct,ad_spend,roas,roas_change_pct,listing_quality_score,price_competitiveness,inventory_status,review_rating
```
