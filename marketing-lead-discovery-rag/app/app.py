import pandas as pd
import streamlit as st

from rag_engine import build_profile, citation_correctness, evaluate_golden_dataset, rerank_candidates, retrieve_candidates
from llm_client import azure_openai_available, generate_grounded_profile

st.set_page_config(page_title="Marketing Lead Discovery RAG", layout="wide")
st.title("Marketing Lead Discovery RAG")
st.caption("Working RAG-oriented MVP for source-grounded, human-reviewed marketplace lead research")

@st.cache_data
def load_sources():
    return pd.read_csv("sample_lead_sources.csv")

@st.cache_data
def load_golden():
    return pd.read_csv("golden_dataset.csv")

sources = load_sources()
golden = load_golden()

st.sidebar.markdown("### Source Governance")
st.sidebar.success("Synthetic approved-source dataset")
st.sidebar.write("No personal data enrichment or outreach action is enabled.")
st.sidebar.write("Source freshness is shown with each citation.")

query = st.text_input("Research question", value="Which company is expanding marketplace fulfillment?")
if st.button("Research lead", type="primary"):
    candidates = retrieve_candidates(sources, query)
    ranked = rerank_candidates(candidates, query)
    st.session_state.ranked = ranked
    st.session_state.query = query

if "ranked" not in st.session_state:
    st.session_state.ranked = rerank_candidates(retrieve_candidates(sources, query), query)
    st.session_state.query = query

ranked = st.session_state.ranked
profile = build_profile(ranked)

metric1, metric2, metric3 = st.columns(3)
metric1.metric("ICP fit score", f"{profile['icp_score']} / 100")
metric2.metric("Cited sources", len(profile["citations"]))
metric3.metric("Human review", "Required before outreach")

left, right = st.columns([1.2, 0.8])
with left:
    st.subheader("Lead Profile")
    st.success(f"{profile['company_name']} - {profile['region']}")
    st.write(profile["profile"])
    st.write("**ICP evidence:** " + ", ".join(profile["icp_reasons"]))
    st.caption("The profile is an advisory research draft. A reviewer validates fit and approved sources before any outreach decision.")
    if st.button("Generate Azure AI Foundry profile"):
        if not azure_openai_available():
            st.info("Azure AI Foundry is not configured locally. The deterministic cited profile remains available.")
        else:
            try:
                with st.spinner("Generating a citation-grounded profile..."):
                    llm_profile = generate_grounded_profile(profile)
                st.subheader("Azure AI Foundry Profile Draft")
                st.write(llm_profile)
                citation_check = citation_correctness(llm_profile, profile["citations"])
                if citation_check["citation_valid"]:
                    st.success("Citation check passed: " + ", ".join(citation_check["cited_ids"]))
                else:
                    st.error("Citation check failed. Invalid or missing source IDs: " + ", ".join(citation_check["invalid_ids"] or ["none found"]))
                st.caption("Generated only from the citations shown below. Human review is required before outreach.")
            except Exception:
                st.warning("Azure AI Foundry was unavailable. The deterministic cited profile remains the fallback.")
with right:
    st.subheader("Retrieval Pipeline")
    st.write("1. Hybrid candidate retrieval")
    st.write("2. Relevance reranking")
    st.write("3. Small cited context set")
    st.write("4. Research profile draft")
    st.write("5. Human review before action")

st.subheader("Citations")
for citation in profile["citations"]:
    with st.expander(f"[{citation['source_id']}] {citation['source_title']} - {citation['source_date']}"):
        st.write(citation["content"])

st.subheader("Retrieved and Reranked Evidence")
st.dataframe(ranked[["lead_id", "company_name", "source_id", "source_title", "keyword_score", "hybrid_score", "rerank_score"]], use_container_width=True, hide_index=True)

st.divider()
st.subheader("Offline Evaluation: Golden Query Set")
evaluation = evaluate_golden_dataset(sources, golden)
eval1, eval2, eval3 = st.columns(3)
eval1.metric("Lead retrieval rate", f"{evaluation['lead_retrieved'].mean() * 100:.0f}%")
eval2.metric("Mean Recall@3", f"{evaluation['recall_at_3'].mean() * 100:.0f}%")
eval3.metric("Mean Precision@3", f"{evaluation['precision_at_3'].mean() * 100:.0f}%")
st.dataframe(evaluation, use_container_width=True, hide_index=True)
st.caption("Evaluation uses a small synthetic golden set. A real pilot requires authorized sources, representative reviewer tasks, and a documented evaluation rubric.")
