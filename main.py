import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="Lebanon Tourism Data Explorer")

st.title("Lebanon Tourism Data Explorer")
st.markdown(
    "This app visualizes tourism-related facilities across Lebanon, "
    "with interactive features for exploring towns and governorates."
)

# --- Load CSV from full path ---
df = pd.read_csv(r"C:\Users\Z\Desktop\551015b5649368dd2612f795c2a9c2d8_20240902_115953.csv")

# --- Sidebar filters ---
st.sidebar.header("Filters")

# Governorate filter
governorates = sorted(df["refArea"].unique())
selected_governorates = st.sidebar.multiselect(
    "Select Governorates",
    options=governorates,
    default=governorates
)

# Facility type filter for pie chart
facility_options = ["Hotels", "Cafes", "Restaurants", "Guest Houses"]
selected_facilities = st.sidebar.multiselect(
    "Select Facility Types for Pie Chart",
    options=facility_options,
    default=facility_options
)

# Apply governorate filter
df_filtered = df[df["refArea"].isin(selected_governorates)]

# --- Visualization 1: Line Chart ---
st.subheader("Tourism Index Across Towns")
df_sorted = df_filtered.sort_values("Tourism Index", ascending=False)
fig1 = px.line(
    df_sorted,
    x="Town",
    y="Tourism Index",
    title="Tourism Index Across Towns",
)
fig1.update_xaxes(showticklabels=False)
fig1.update_layout(title_x=0.5, plot_bgcolor="white")
st.plotly_chart(fig1, use_container_width=True)

# --- Visualization 2: Pie Chart ---
st.subheader("Distribution of Tourism Facilities")
totals = {
    "Hotels": df_filtered["Total number of hotels"].sum(),
    "Cafes": df_filtered["Total number of cafes"].sum(),
    "Restaurants": df_filtered["Total number of restaurants"].sum(),
    "Guest Houses": df_filtered["Total number of guest houses"].sum(),
}
totals = {k: v for k, v in totals.items() if k in selected_facilities}

fig2 = px.pie(
    names=list(totals.keys()),
    values=list(totals.values()),
    title="Distribution of Selected Tourism Facilities",
)
st.plotly_chart(fig2, use_container_width=True)

# --- Enhanced Insights ---
st.markdown("### Insights")

st.markdown(
    """
**Line Chart: Tourism Index Across Towns**
- The line chart shows how the Tourism Index varies across towns, highlighting the towns with the highest and lowest tourism activity.
- Towns like Beirut and Jounieh peak in the index, indicating major tourist hubs.
- Less popular towns have lower indices, reflecting fewer tourism facilities or lower visitor engagement.
- *Interactive Insight:* Use the sidebar to select specific governorates to focus on their towns and observe regional tourism trends.

**Pie Chart: Distribution of Tourism Facilities**
- Restaurants and cafes make up the largest share, reflecting Lebanon’s culinary tourism.
- Hotels are concentrated in high-tourist towns, while guest houses are the smallest category.
- *Interactive Insight:* Toggle facility types in the sidebar to analyze specific components of the tourism infrastructure.


"""
)
