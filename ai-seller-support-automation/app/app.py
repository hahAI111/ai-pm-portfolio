import pandas as pd
import streamlit as st
from support_engine import classify_ticket, draft_response, retrieve_guidance

st.set_page_config(page_title="AI Seller Support Automation", layout="wide")
st.title("AI Seller Support Automation")
st.caption("Working AI PM MVP for ticket classification, knowledge retrieval, safe response drafting, and escalation")

@st.cache_data
def load_tickets():
    return pd.read_csv("sample_tickets.csv")

@st.cache_data
def load_knowledge_base():
    return pd.read_csv("seller_knowledge_base.csv")

if "feedback" not in st.session_state:
    st.session_state.feedback = []

tickets = load_tickets()
knowledge_base = load_knowledge_base()

st.sidebar.markdown("### Ticket Source")
ticket_id = st.sidebar.selectbox("Choose sample ticket", tickets["ticket_id"].tolist())
selected_ticket = tickets[tickets["ticket_id"] == ticket_id].iloc[0]
st.sidebar.write(f"Seller: **{selected_ticket['seller_id']}**")
st.sidebar.write(f"Reported priority: **{selected_ticket['priority']}**")

st.subheader("Seller Support Ticket")
st.write(f"**Subject:** {selected_ticket['subject']}")
ticket_text = st.text_area("Seller message", value=selected_ticket["message"], height=120)

if st.button("Classify and draft response", type="primary"):
    classification = classify_ticket(ticket_text)
    guidance = retrieve_guidance(knowledge_base, classification["category"])
    response = draft_response(ticket_text, classification, guidance)
    st.session_state.latest_result = {
        "classification": classification,
        "guidance": guidance,
        "response": response,
    }

if "latest_result" not in st.session_state:
    st.session_state.latest_result = None

result = st.session_state.latest_result
if result:
    classification = result["classification"]
    left, right = st.columns([1.1, 0.9])
    with left:
        st.subheader("AI Triage Result")
        st.metric("Ticket category", classification["category"])
        st.metric("Classification confidence", f"{classification['confidence'] * 100:.0f}%")
        if classification["escalation"]:
            st.error("Human review required: policy-sensitive or high-risk request.")
        else:
            st.success("Eligible for AI-assisted response with seller approval.")
        st.subheader("Retrieved Guidance")
        st.info(result["guidance"])
    with right:
        st.subheader("Draft Seller Response")
        st.write(result["response"])
        st.caption("Safety design: the assistant drafts guidance, but does not make policy decisions or apply account changes.")

    st.subheader("Agent Feedback")
    feedback_col1, feedback_col2, feedback_col3 = st.columns(3)
    with feedback_col1:
        if st.button("Draft was helpful"):
            st.session_state.feedback.append("helpful")
            st.success("Feedback recorded")
    with feedback_col2:
        if st.button("Needs human rewrite"):
            st.session_state.feedback.append("rewrite")
            st.info("Feedback recorded")
    with feedback_col3:
        if st.button("Clear feedback"):
            st.session_state.feedback = []
            st.rerun()

    if st.session_state.feedback:
        helpful = st.session_state.feedback.count("helpful")
        rate = helpful / len(st.session_state.feedback) * 100
        metric1, metric2, metric3 = st.columns(3)
        metric1.metric("Agent feedback count", len(st.session_state.feedback))
        metric2.metric("Helpful drafts", helpful)
        metric3.metric("Draft acceptance rate", f"{rate:.0f}%")

st.divider()
st.subheader("Support Operations Metrics")
metric1, metric2, metric3, metric4 = st.columns(4)
metric1.metric("Target ticket deflection", "25%")
metric2.metric("Target handling-time reduction", "30%")
metric3.metric("Target first-contact resolution", "+12 pts")
metric4.metric("Policy escalation goal", "100% routed")

st.caption("Portfolio framing: this MVP demonstrates an AI support workflow with classification, retrieval, response drafting, feedback, and human-review guardrails.")
