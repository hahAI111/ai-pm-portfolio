import pandas as pd
import streamlit as st
from opportunity import calculate_opportunity_scores, generate_insight, recommend_initiative

st.set_page_config(page_title="Marketplace Opportunity Discovery", layout="wide")
st.title("Marketplace Opportunity Discovery Dashboard")
st.caption("Working PM analytics MVP for finding, sizing, and prioritizing seller-growth opportunities")

@st.cache_data
def load_data():
    return pd.read_csv("sample_marketplace_data.csv")

required_columns = {
    "seller_id", "category", "region", "monthly_gmv", "gmv_growth_pct", "orders",
    "orders_growth_pct", "conversion_rate", "conversion_change_pct", "ad_roas",
    "listing_quality_score", "active_products", "inventory_health", "return_rate", "customer_rating",
}

st.sidebar.markdown("### Data Source")
uploaded_file = st.sidebar.file_uploader("Upload marketplace CSV", type=["csv"])
if uploaded_file is not None:
    try:
        raw_data = pd.read_csv(uploaded_file)
        missing = required_columns - set(raw_data.columns)
        if missing or raw_data.empty:
            st.sidebar.error("Invalid CSV. Showing sample data.")
            if missing:
                st.sidebar.caption("Missing: " + ", ".join(sorted(missing)))
            raw_data = load_data()
        else:
            st.sidebar.success(f"Loaded {len(raw_data)} seller records")
    except (UnicodeDecodeError, pd.errors.ParserError):
        st.sidebar.error("CSV could not be read. Showing sample data.")
        raw_data = load_data()
else:
    raw_data = load_data()
    st.sidebar.caption("Using included sample marketplace data")

with st.sidebar.expander("CSV format guide"):
    st.write("The app expects one seller record per row. Download the sample data as a template.")
    st.download_button(
        "Download CSV template",
        raw_data.to_csv(index=False).encode("utf-8"),
        "marketplace_opportunity_template.csv",
        "text/csv",
    )

categories = ["All"] + sorted(raw_data["category"].unique().tolist())
regions = ["All"] + sorted(raw_data["region"].unique().tolist())
selected_category = st.sidebar.selectbox("Category", categories)
selected_region = st.sidebar.selectbox("Region", regions)

filtered = raw_data.copy()
if selected_category != "All":
    filtered = filtered[filtered["category"] == selected_category]
if selected_region != "All":
    filtered = filtered[filtered["region"] == selected_region]

scored = calculate_opportunity_scores(filtered)

total_gmv = scored["monthly_gmv"].sum()
priority_count = (scored["opportunity_tier"] == "Prioritize").sum()
avg_growth = scored["gmv_growth_pct"].mean()
avg_score = scored["opportunity_score"].mean()

metric1, metric2, metric3, metric4 = st.columns(4)
metric1.metric("Marketplace GMV", f"USD {total_gmv:,.0f}")
metric2.metric("Prioritize opportunities", int(priority_count))
metric3.metric("Average GMV growth", f"{avg_growth:.1f}%")
metric4.metric("Average opportunity score", f"{avg_score:.1f} / 100")

st.divider()
chart_col1, chart_col2 = st.columns(2)
with chart_col1:
    st.subheader("Opportunity Map")
    st.caption("High growth plus remaining execution gaps indicate stronger product opportunity.")
    st.scatter_chart(scored, x="gmv_growth_pct", y="opportunity_score", size="monthly_gmv", color="category")
with chart_col2:
    st.subheader("GMV by Category")
    st.bar_chart(scored.groupby("category")["monthly_gmv"].sum().sort_values(ascending=False))

st.divider()
st.subheader("Ranked Opportunity Backlog")
backlog_columns = ["seller_id", "category", "region", "monthly_gmv", "gmv_growth_pct", "conversion_rate", "ad_roas", "listing_quality_score", "opportunity_score", "opportunity_tier"]
st.dataframe(scored[backlog_columns], use_container_width=True, hide_index=True)

top_opportunity = scored.iloc[0]
initiative = recommend_initiative(top_opportunity)

detail_col1, detail_col2 = st.columns([1.2, 0.8])
with detail_col1:
    st.subheader("Top Opportunity Insight")
    st.success(f"{top_opportunity['seller_id']} — {top_opportunity['category']} in {top_opportunity['region']}")
    st.write(generate_insight(top_opportunity))
    st.write(f"**Opportunity score:** {top_opportunity['opportunity_score']} / 100 ({top_opportunity['opportunity_tier']})")
with detail_col2:
    st.subheader("Recommended Product Initiative")
    st.write(f"**{initiative['initiative']}**")
    st.write(initiative["why"])
    st.caption(f"Primary metric: {initiative['metric']}")

st.divider()
st.subheader("PM Prioritization Logic")
st.write("Opportunity score combines growth momentum, conversion gap, listing-quality gap, advertising efficiency, inventory readiness, and return-rate quality.")
st.code("Opportunity score = growth potential + execution gaps + business readiness", language="text")
st.caption("This transparent heuristic is appropriate for an MVP. A production implementation would calibrate weights using historical outcomes and controlled experiments.")
