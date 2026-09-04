import pandas as pd
import streamlit as st
from diagnosis import diagnose_seller, generate_action_plan, generate_seller_response, seller_summary
from llm_client import azure_openai_available, generate_with_azure_openai

st.set_page_config(page_title="AI Seller Growth Copilot", layout="wide")

st.title("AI Seller Growth Copilot")
st.caption("Working MVP prototype for seller growth diagnosis and action planning")

if "recommendation_feedback" not in st.session_state:
    st.session_state.recommendation_feedback = []
if "completed_actions" not in st.session_state:
    st.session_state.completed_actions = {}

@st.cache_data
def load_data():
    return pd.read_csv("sample_seller_data.csv")

required_columns = {
    "seller_id", "category", "weekly_sales", "sales_change_pct", "sessions",
    "sessions_change_pct", "conversion_rate", "conversion_change_pct", "ad_spend",
    "roas", "roas_change_pct", "listing_quality_score", "price_competitiveness",
    "inventory_status", "review_rating",
}

st.sidebar.markdown("### Data Source")
uploaded_file = st.sidebar.file_uploader("Upload seller data CSV", type=["csv"])

if uploaded_file is not None:
    try:
        uploaded_data = pd.read_csv(uploaded_file)
        missing_columns = required_columns - set(uploaded_data.columns)
        if missing_columns:
            st.sidebar.error("CSV is missing required columns.")
            st.sidebar.caption("Missing: " + ", ".join(sorted(missing_columns)))
            data = load_data()
            st.sidebar.info("Showing sample data instead.")
        elif uploaded_data.empty:
            st.sidebar.error("The uploaded CSV has no seller rows. Showing sample data instead.")
            data = load_data()
        else:
            data = uploaded_data
            st.sidebar.success(f"Loaded {len(data)} seller records")
    except (UnicodeDecodeError, pd.errors.ParserError) as error:
        st.sidebar.error("The CSV could not be read. Showing sample data instead.")
        st.sidebar.caption(str(error))
        data = load_data()
else:
    data = load_data()
    st.sidebar.caption("Using included sample seller data")

with st.sidebar.expander("CSV format guide"):
    st.write("Upload a CSV with one row per seller. Required columns:")
    st.code(
        "seller_id, category, weekly_sales, sales_change_pct, sessions, "
        "sessions_change_pct, conversion_rate, conversion_change_pct, ad_spend, "
        "roas, roas_change_pct, listing_quality_score, price_competitiveness, "
        "inventory_status, review_rating"
    )
    st.download_button(
        "Download sample CSV template",
        data=load_data().to_csv(index=False).encode("utf-8"),
        file_name="seller_growth_copilot_template.csv",
        mime="text/csv",
    )

seller_id = st.sidebar.selectbox("Choose seller", data["seller_id"].tolist())
row = data[data["seller_id"] == seller_id].iloc[0]
diagnosis = diagnose_seller(row)
actions = generate_action_plan(row, diagnosis)

st.sidebar.markdown("### Seller Profile")
st.sidebar.write(f"Category: **{row['category']}**")
st.sidebar.write(f"Review rating: **{row['review_rating']}**")
st.sidebar.write(f"Inventory: **{row['inventory_status']}**")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Weekly Sales", f"USD {row['weekly_sales']:,.0f}", f"{row['sales_change_pct']}%")
col2.metric("Sessions", f"{row['sessions']:,.0f}", f"{row['sessions_change_pct']}%")
col3.metric("Conversion Rate", f"{row['conversion_rate']}%", f"{row['conversion_change_pct']}%")
col4.metric("Ad ROAS", f"{row['roas']}", f"{row['roas_change_pct']}%")

st.divider()

st.subheader("Performance Trends")
st.caption("Demo trend data is derived from the selected seller's current metrics and recent percentage changes.")

def build_trend_data(seller_row):
    weeks = ["4 weeks ago", "3 weeks ago", "2 weeks ago", "This week"]
    sales_change_factor = 1 + seller_row["sales_change_pct"] / 100
    session_change_factor = 1 + seller_row["sessions_change_pct"] / 100
    conversion_change_factor = 1 + seller_row["conversion_change_pct"] / 100

    previous_sales = seller_row["weekly_sales"] / sales_change_factor
    previous_sessions = seller_row["sessions"] / session_change_factor
    previous_conversion = seller_row["conversion_rate"] / conversion_change_factor

    return pd.DataFrame({
        "Week": weeks,
        "Sales": [previous_sales * 0.94, previous_sales * 0.98, previous_sales, seller_row["weekly_sales"]],
        "Sessions": [previous_sessions * 0.95, previous_sessions * 0.98, previous_sessions, seller_row["sessions"]],
        "Conversion rate": [previous_conversion * 0.98, previous_conversion * 1.01, previous_conversion, seller_row["conversion_rate"]],
    }).set_index("Week")

trend_data = build_trend_data(row)
trend_col1, trend_col2 = st.columns(2)
with trend_col1:
    st.markdown("**Sales and sessions**")
    st.line_chart(trend_data[["Sales", "Sessions"]])
with trend_col2:
    st.markdown("**Conversion rate**")
    st.line_chart(trend_data[["Conversion rate"]])

left, right = st.columns([1.2, 0.8])

with left:
    st.subheader("Growth Diagnosis")
    st.warning(diagnosis["primary_blocker"])
    st.write(seller_summary(row, diagnosis))

    st.subheader("Recommended Action Plan")
    action_df = pd.DataFrame(actions)
    st.dataframe(action_df, use_container_width=True, hide_index=True)

    st.markdown("#### Track action completion")
    st.caption("Mark an action complete after the seller has made the change. This simulates the product loop from recommendation to verified execution.")
    for index, action in enumerate(actions):
        action_key = f"{seller_id}-{index}-{action['action']}"
        if action_key not in st.session_state.completed_actions:
            st.session_state.completed_actions[action_key] = False
        st.session_state.completed_actions[action_key] = st.checkbox(
            f"{action['priority']}: {action['action']}",
            value=st.session_state.completed_actions[action_key],
            key=f"checkbox-{action_key}",
        )

with right:
    st.subheader("Evidence")
    for blocker, score, evidence in diagnosis["all_blockers"]:
        st.write(f"**{blocker}** — confidence {round(score * 100)}%")
        st.caption(evidence)

    st.subheader("PM Guardrails")
    st.write("- Show confidence for each diagnosis")
    st.write("- Require seller approval before applying changes")
    st.write("- Escalate policy-sensitive recommendations")
    st.write("- Track accepted actions and business impact")

st.divider()
st.subheader("Product Experiment Plan")
st.write("Hypothesis: sellers who receive prioritized AI recommendations complete more high-impact growth actions than sellers using standard dashboards alone.")
st.write("Primary metrics: action completion rate, conversion uplift, recommendation acceptance rate, and seller satisfaction score.")

st.divider()
st.subheader("Ask the Seller Growth Assistant")
st.caption("This MVP uses the selected seller performance signals and rule-based diagnosis. No external model API key is required.")
question = st.text_area(
    "What would you like help with?",
    placeholder="Example: Why did my sales decline, and what should I do first?",
)

if st.button("Generate AI Recommendation", type="primary"):
    if not question.strip():
        st.info("Enter a seller question to generate a recommendation.")
    else:
        with st.spinner("Analyzing seller signals..."):
            fallback_response = generate_seller_response(row, diagnosis, question)
            if azure_openai_available():
                try:
                    response = generate_with_azure_openai(
                        "You are a careful marketplace seller-growth assistant. Use only the supplied seller data and diagnosis. Provide concise, practical advice. Do not guarantee outcomes or recommend automatic changes.",
                        "Seller question: " + question + "\nSeller data: " + str(row.to_dict()) + "\nDiagnosis: " + str(diagnosis) + "\nFallback: " + fallback_response,
                    )
                    st.caption("Response generated with Azure OpenAI, grounded in the displayed seller signals.")
                except Exception:
                    response = fallback_response
                    st.warning("Azure OpenAI was unavailable, so the deterministic MVP fallback was used.")
            else:
                response = fallback_response
                st.caption("Deterministic MVP fallback in use. Add Azure OpenAI secrets to enable model-generated wording.")
        st.success("Recommendation generated")
        st.write(response)
        st.caption("MVP safety note: recommendations are advisory. Sellers approve all operational changes.")

st.divider()
st.subheader("Recommendation Feedback Loop")
st.caption("Capture whether a seller found the recommendation useful. In a production product, this signal would improve future recommendation ranking and quality monitoring.")

feedback_col1, feedback_col2, feedback_col3 = st.columns([1, 1, 2])
with feedback_col1:
    if st.button("Helpful"):
        st.session_state.recommendation_feedback.append("helpful")
        st.success("Feedback recorded: helpful")
with feedback_col2:
    if st.button("Not helpful"):
        st.session_state.recommendation_feedback.append("not_helpful")
        st.info("Feedback recorded: not helpful")
with feedback_col3:
    if st.button("Clear demo feedback"):
        st.session_state.recommendation_feedback = []
        st.rerun()

feedback = st.session_state.recommendation_feedback
if feedback:
    helpful_count = feedback.count("helpful")
    acceptance_rate = helpful_count / len(feedback) * 100
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    metric_col1.metric("Feedback responses", len(feedback))
    metric_col2.metric("Helpful responses", helpful_count)
    metric_col3.metric("Recommendation acceptance rate", f"{acceptance_rate:.0f}%")
else:
    st.info("No feedback recorded yet. Use the buttons above to simulate the recommendation-quality feedback loop.")

st.divider()
st.subheader("Action Completion Tracking")
seller_action_keys = [f"{seller_id}-{index}-{action['action']}" for index, action in enumerate(actions)]
completed_count = sum(st.session_state.completed_actions.get(key, False) for key in seller_action_keys)
completion_rate = completed_count / len(seller_action_keys) * 100 if seller_action_keys else 0

completion_col1, completion_col2, completion_col3 = st.columns(3)
completion_col1.metric("Recommended actions", len(seller_action_keys))
completion_col2.metric("Completed actions", completed_count)
completion_col3.metric("Action completion rate", f"{completion_rate:.0f}%")

if completed_count:
    st.success("Completion data is ready to connect with downstream conversion, ROAS, and seller-growth outcome measurement.")
else:
    st.info("Complete one or more actions above to simulate the recommendation-to-outcome product loop.")

st.divider()
st.subheader("Outcome Simulator")
st.caption("This is a transparent portfolio simulation, not a business forecast. Estimated changes are based on completed action types and are designed to demonstrate how an AI product can connect recommendations to outcome measurement.")

completed_actions = [
    action for index, action in enumerate(actions)
    if st.session_state.completed_actions.get(f"{seller_id}-{index}-{action['action']}", False)
]

def estimate_outcomes(current_row, completed):
    conversion_uplift = 0.0
    roas_uplift = 0.0
    sales_uplift = 0.0

    for action in completed:
        action_name = action["action"].lower()
        if "title" in action_name or "listing quality" in action_name:
            conversion_uplift += 0.06
            sales_uplift += 0.04
        elif "promotion" in action_name:
            conversion_uplift += 0.04
            sales_uplift += 0.05
        elif "images" in action_name:
            conversion_uplift += 0.03
            sales_uplift += 0.02
        elif "keyword" in action_name or "budget" in action_name:
            roas_uplift += 0.08
            sales_uplift += 0.02
        elif "inventory" in action_name:
            conversion_uplift += 0.03
            sales_uplift += 0.06
        else:
            sales_uplift += 0.01

    projected_conversion = current_row["conversion_rate"] * (1 + conversion_uplift)
    projected_roas = current_row["roas"] * (1 + roas_uplift)
    projected_sales = current_row["weekly_sales"] * (1 + sales_uplift)
    return projected_conversion, projected_roas, projected_sales

if not completed_actions:
    st.info("Mark actions complete to see an illustrative outcome scenario.")
else:
    projected_conversion, projected_roas, projected_sales = estimate_outcomes(row, completed_actions)
    outcome_col1, outcome_col2, outcome_col3 = st.columns(3)
    outcome_col1.metric(
        "Projected conversion rate",
        f"{projected_conversion:.2f}%",
        f"{projected_conversion - row['conversion_rate']:.2f} pts",
    )
    outcome_col2.metric(
        "Projected ROAS",
        f"{projected_roas:.2f}",
        f"{projected_roas - row['roas']:.2f}",
    )
    outcome_col3.metric(
        "Projected weekly sales",
        f"USD {projected_sales:,.0f}",
        f"USD {projected_sales - row['weekly_sales']:,.0f}",
    )
    st.write("Completed actions included in this scenario:")
    for action in completed_actions:
        st.write(f"- {action['action']}")
    st.caption("In production, these projections would be replaced with experiment results and observed post-action seller metrics.")
