import pandas as pd


def generate_seller_response(row: pd.Series, diagnosis: dict, question: str) -> str:
    """Create a grounded MVP response without an external model API."""
    actions = generate_action_plan(row, diagnosis)
    top_actions = "; ".join(action["action"] for action in actions[:2])
    question_context = question.strip() or "how to improve current performance"
    confidence = round(diagnosis["confidence"] * 100)
    return (
        f"For your question about {question_context}, the strongest current signal is "
        f"{diagnosis['primary_blocker'].lower()} ({confidence}% confidence). "
        f"{diagnosis['evidence']} Recommended next steps: {top_actions}. "
        "Please review any pricing, advertising, or listing change before applying it and "
        "measure the relevant metric for at least 7 to 14 days."
    )


def diagnose_seller(row: pd.Series) -> dict:
    sales_change = row["sales_change_pct"]
    sessions_change = row["sessions_change_pct"]
    conversion_change = row["conversion_change_pct"]
    roas_change = row["roas_change_pct"]
    listing_quality = row["listing_quality_score"]
    inventory = str(row["inventory_status"]).lower()
    price = str(row["price_competitiveness"]).lower()

    blockers = []

    if sales_change < 0 and sessions_change >= -3 and conversion_change < -10:
        blockers.append(("Conversion issue", 0.92, "Traffic is stable, but conversion dropped sharply."))
    if sessions_change < -10:
        blockers.append(("Traffic issue", 0.86, "Sessions declined meaningfully."))
    if listing_quality < 70:
        blockers.append(("Listing quality issue", 0.78, "Listing quality score is below the recommended threshold."))
    if roas_change < -10:
        blockers.append(("Advertising efficiency issue", 0.74, "ROAS declined while ad spend is still active."))
    if "low" in inventory:
        blockers.append(("Inventory issue", 0.72, "Inventory status may limit sales or delivery promise."))
    if "weak" in price:
        blockers.append(("Pricing competitiveness issue", 0.70, "Price competitiveness is weaker than peer listings."))

    if not blockers:
        blockers.append(("No urgent blocker", 0.65, "Core metrics look stable or positive."))

    blockers = sorted(blockers, key=lambda item: item[1], reverse=True)
    return {
        "primary_blocker": blockers[0][0],
        "confidence": blockers[0][1],
        "evidence": blockers[0][2],
        "all_blockers": blockers,
    }


def generate_action_plan(row: pd.Series, diagnosis: dict) -> list[dict]:
    actions = []
    blocker = diagnosis["primary_blocker"]

    if blocker == "Conversion issue":
        actions.extend([
            {"priority": "P0", "action": "Improve product title and first two bullet points", "reason": "Value proposition may not be clear enough after shoppers land on the page.", "effort": "Low", "metric": "Conversion rate"},
            {"priority": "P1", "action": "Test a 7-day promotion", "reason": "Price competitiveness is weak or average.", "effort": "Medium", "metric": "Conversion rate and margin"},
            {"priority": "P1", "action": "Replace weak secondary images", "reason": "Product benefits may not be visually clear.", "effort": "Medium", "metric": "Add-to-cart rate"},
        ])
    elif blocker == "Traffic issue":
        actions.extend([
            {"priority": "P0", "action": "Review keyword coverage and category placement", "reason": "Sessions declined meaningfully.", "effort": "Medium", "metric": "Sessions"},
            {"priority": "P1", "action": "Refresh advertising keyword targets", "reason": "Paid traffic may not be reaching relevant shoppers.", "effort": "Medium", "metric": "CTR and sessions"},
        ])
    elif blocker == "Advertising efficiency issue":
        actions.extend([
            {"priority": "P0", "action": "Pause low-converting keywords", "reason": "ROAS declined while ad spend remains active.", "effort": "Low", "metric": "ROAS"},
            {"priority": "P1", "action": "Shift budget to high-intent keywords", "reason": "Budget should favor keywords with better conversion.", "effort": "Medium", "metric": "ROAS"},
        ])
    else:
        actions.append({"priority": "P1", "action": "Monitor weekly performance and run listing quality check", "reason": "No single severe blocker is detected.", "effort": "Low", "metric": "Sales and conversion"})

    if row["listing_quality_score"] < 70 and not any("listing" in a["action"].lower() for a in actions):
        actions.append({"priority": "P1", "action": "Improve listing quality score", "reason": "Listing quality is below 70.", "effort": "Medium", "metric": "Listing quality score"})
    if str(row["inventory_status"]).lower() == "low":
        actions.append({"priority": "P0", "action": "Replenish inventory", "reason": "Low inventory can reduce conversion and delivery confidence.", "effort": "High", "metric": "Inventory health"})

    return actions


def seller_summary(row: pd.Series, diagnosis: dict) -> str:
    confidence = round(diagnosis["confidence"] * 100)
    return (
        f"The main blocker is likely {diagnosis['primary_blocker'].lower()} "
        f"with {confidence}% confidence. {diagnosis['evidence']} "
        f"Sales changed by {row['sales_change_pct']}%, sessions by {row['sessions_change_pct']}%, "
        f"and conversion by {row['conversion_change_pct']}%."
    )
