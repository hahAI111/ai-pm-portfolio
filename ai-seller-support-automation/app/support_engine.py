import pandas as pd


KEYWORDS = {
    "Listing": ["listing", "product page", "title", "bullet", "image", "views", "orders"],
    "Advertising": ["ad", "advertising", "roas", "keyword", "spend", "campaign"],
    "Inventory": ["inventory", "stock", "units left", "replenish", "out of stock"],
    "Pricing": ["price", "promotion", "discount", "margin", "competitive"],
    "Policy": ["policy", "claim", "compliance", "restricted", "allowed"],
    "Account": ["account", "payout", "tax", "verification", "profile"],
    "Customer Experience": ["return", "refund", "review", "rating", "customer"],
}


def classify_ticket(text: str) -> dict:
    normalized = text.lower()
    scores = {
        category: sum(keyword in normalized for keyword in keywords)
        for category, keywords in KEYWORDS.items()
    }
    category, matches = max(scores.items(), key=lambda item: item[1])
    if matches == 0:
        category, matches = "Account", 0

    confidence = min(0.55 + matches * 0.15, 0.95)
    escalation = category == "Policy" or "health claim" in normalized
    return {"category": category, "confidence": confidence, "escalation": escalation}


def retrieve_guidance(knowledge_base: pd.DataFrame, category: str) -> str:
    matches = knowledge_base[knowledge_base["category"].str.lower() == category.lower()]
    if matches.empty:
        return "Review the seller context and route the request to the appropriate support team if more information is required."
    return matches.iloc[0]["content"]


def draft_response(ticket_text: str, classification: dict, guidance: str) -> str:
    if classification["escalation"]:
        return (
            "Thanks for checking before making a change. This request may involve marketplace policy or compliance. "
            "I have flagged it for human review. In the meantime, avoid publishing or changing the claim until a trained reviewer confirms the guidance. "
            f"Relevant guidance: {guidance}"
        )

    return (
        f"I classified this as a {classification['category'].lower()} question. "
        f"Recommended next step: {guidance} "
        "Please review the suggestion against your seller data and confirm any operational change before applying it."
    )
