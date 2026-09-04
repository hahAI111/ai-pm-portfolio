import pandas as pd


def calculate_opportunity_scores(data: pd.DataFrame) -> pd.DataFrame:
    scored = data.copy()

    growth_score = scored["gmv_growth_pct"].clip(lower=0, upper=30) / 30 * 35
    conversion_score = (4.5 - scored["conversion_rate"]).clip(lower=0, upper=2.5) / 2.5 * 20
    listing_score = (90 - scored["listing_quality_score"]).clip(lower=0, upper=40) / 40 * 15
    roas_score = (4 - scored["ad_roas"]).clip(lower=0, upper=2) / 2 * 15
    inventory_score = (scored["inventory_health"].str.lower() == "healthy").astype(int) * 5
    return_score = (7 - scored["return_rate"]).clip(lower=0, upper=7) / 7 * 10

    scored["opportunity_score"] = (
        growth_score + conversion_score + listing_score + roas_score + inventory_score + return_score
    ).round(1)
    scored["opportunity_tier"] = pd.cut(
        scored["opportunity_score"],
        bins=[-1, 40, 60, 100],
        labels=["Monitor", "Build", "Prioritize"],
    )
    return scored.sort_values("opportunity_score", ascending=False)


def generate_insight(row: pd.Series) -> str:
    strengths = []
    gaps = []

    if row["gmv_growth_pct"] >= 15:
        strengths.append("strong GMV growth")
    if row["orders_growth_pct"] >= 15:
        strengths.append("accelerating order growth")
    if row["customer_rating"] >= 4.5:
        strengths.append("strong customer satisfaction")
    if row["conversion_rate"] < 3.5:
        gaps.append("conversion has room to improve")
    if row["listing_quality_score"] < 75:
        gaps.append("listing quality is below target")
    if row["ad_roas"] < 2.8:
        gaps.append("ad efficiency needs attention")
    if str(row["inventory_health"]).lower() == "low":
        gaps.append("inventory risk could constrain growth")

    strength_text = ", ".join(strengths) if strengths else "stable business performance"
    gap_text = ", ".join(gaps) if gaps else "no major execution gap detected"
    return f"{row['category']} in {row['region']} shows {strength_text}; {gap_text}."


def recommend_initiative(row: pd.Series) -> dict:
    if str(row["inventory_health"]).lower() == "low":
        return {"initiative": "Inventory health alert and replenishment workflow", "why": "Growth is at risk if products cannot stay available.", "metric": "In-stock rate and GMV"}
    if row["conversion_rate"] < 3.5 or row["listing_quality_score"] < 75:
        return {"initiative": "AI listing quality and conversion playbook", "why": "Improve product page quality before increasing acquisition spend.", "metric": "Conversion rate and listing quality score"}
    if row["ad_roas"] < 2.8:
        return {"initiative": "AI advertising efficiency recommendations", "why": "Improve budget allocation and keyword quality.", "metric": "ROAS and cost per order"}
    return {"initiative": "Scale high-growth seller playbook", "why": "Use growth signals to identify repeatable acquisition and retention opportunities.", "metric": "GMV growth and seller activation"}
