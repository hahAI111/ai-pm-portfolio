import re

import pandas as pd


STOP_WORDS = {"a", "an", "and", "are", "for", "is", "of", "the", "to", "which", "with", "who"}


def tokenize(text: str) -> set[str]:
    return {word for word in re.findall(r"[a-zA-Z]{3,}", text.lower()) if word not in STOP_WORDS}


def retrieve_candidates(sources: pd.DataFrame, query: str, top_k: int = 5) -> pd.DataFrame:
    query_terms = tokenize(query)
    candidates = sources.copy()
    candidates["keyword_score"] = candidates.apply(
        lambda row: len(query_terms & tokenize(" ".join([row["company_name"], row["source_title"], row["content"]]))),
        axis=1,
    )
    candidates["semantic_proxy_score"] = candidates.apply(
        lambda row: sum(term in row["content"].lower() for term in query_terms) / max(len(query_terms), 1),
        axis=1,
    )
    candidates["hybrid_score"] = candidates["keyword_score"] + candidates["semantic_proxy_score"]
    return candidates.sort_values(["hybrid_score", "source_date"], ascending=[False, False]).head(top_k)


def rerank_candidates(candidates: pd.DataFrame, query: str, top_k: int = 3) -> pd.DataFrame:
    query_terms = tokenize(query)
    ranked = candidates.copy()
    ranked["rerank_score"] = ranked.apply(
        lambda row: row["hybrid_score"] + 0.5 * len(query_terms & tokenize(row["content"])), axis=1
    )
    return ranked.sort_values(["rerank_score", "source_date"], ascending=[False, False]).head(top_k)


def icp_score(lead_sources: pd.DataFrame) -> tuple[int, list[str]]:
    text = " ".join(lead_sources["content"].tolist()).lower()
    reasons = []
    score = 0
    for keyword, points, reason in [
        ("marketplace", 30, "explicit marketplace relevance"),
        ("cross-border", 25, "cross-border expansion signal"),
        ("international", 20, "international growth signal"),
        ("online", 15, "online commerce presence"),
        ("catalog", 10, "catalog scale signal"),
    ]:
        if keyword in text:
            score += points
            reasons.append(reason)
    return min(score, 100), reasons


def build_profile(ranked_sources: pd.DataFrame) -> dict:
    lead_id = ranked_sources.iloc[0]["lead_id"]
    company = ranked_sources.iloc[0]["company_name"]
    region = ranked_sources.iloc[0]["region"]
    all_company_sources = ranked_sources[ranked_sources["lead_id"] == lead_id]
    score, reasons = icp_score(all_company_sources)
    citations = all_company_sources[["source_id", "source_title", "source_date", "content"]].to_dict("records")
    evidence = " ".join(source["content"] for source in citations)
    return {
        "lead_id": lead_id,
        "company_name": company,
        "region": region,
        "icp_score": score,
        "icp_reasons": reasons or ["limited explicit ICP evidence"],
        "profile": f"{company} is a potential marketplace-growth lead in {region}. Evidence indicates: {evidence}",
        "citations": citations,
    }


def evaluate_golden_dataset(sources: pd.DataFrame, golden: pd.DataFrame) -> pd.DataFrame:
    results = []
    for _, case in golden.iterrows():
        retrieved = rerank_candidates(retrieve_candidates(sources, case["query"]), case["query"])
        ids = set(retrieved["source_id"].tolist())
        expected_ids = set(case["expected_source_ids"].split("|"))
        expected_lead = str(case["expected_lead_id"])
        lead_match = expected_lead == "NONE" and retrieved.empty or expected_lead in set(retrieved["lead_id"].tolist())
        recall = len(ids & expected_ids) / len(expected_ids) if expected_ids else (1.0 if expected_lead == "NONE" and retrieved.empty else 0.0)
        precision = len(ids & expected_ids) / len(ids) if ids else 0
        results.append({"query": case["query"], "lead_retrieved": lead_match, "recall_at_3": recall, "precision_at_3": precision})
    return pd.DataFrame(results)


def citation_correctness(draft: str, citations: list[dict]) -> dict:
    """Check that cited source IDs exist and each source-backed claim uses a valid ID."""
    valid_ids = {source["source_id"] for source in citations}
    cited_ids = set(re.findall(r"\[([A-Za-z0-9_-]+)\]", draft))
    invalid_ids = cited_ids - valid_ids
    return {
        "cited_ids": sorted(cited_ids),
        "invalid_ids": sorted(invalid_ids),
        "citation_valid": bool(cited_ids) and not invalid_ids,
    }
