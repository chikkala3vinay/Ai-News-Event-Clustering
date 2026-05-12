
import streamlit as st
import pandas as pd

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="AI News Event Clustering Dashboard",
    layout="wide"
)

# ---------------- LOAD DATA ----------------

df = pd.read_csv("clustered_news.csv")

# ---------------- SIDEBAR ----------------

st.sidebar.title("Filters")

# Cluster filter
cluster_option = st.sidebar.selectbox(
    "Select Cluster",
    sorted(df["cluster"].unique())
)

# Search filter
search = st.sidebar.text_input("Search Headlines")

# ---------------- FILTERING ----------------

filtered_df = df[df["cluster"] == cluster_option]

# Search filter
if search:
    filtered_df = filtered_df[
        filtered_df["headline"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

# ---------------- TITLE ----------------

st.title("AI News Event Clustering Dashboard")

# ---------------- METRICS ----------------

col1, col2, col3 = st.columns(3)

col1.metric("Total Articles", len(df))

col2.metric("Total Clusters", df["cluster"].nunique())

col3.metric("Filtered Articles", len(filtered_df))

# ---------------- CHARTS ----------------

st.subheader("Cluster Distribution")

cluster_counts = df["cluster"].value_counts().sort_index()

st.bar_chart(cluster_counts)

# ---------------- EVENT LABEL CHART ----------------

st.subheader("Event Label Distribution")

event_counts = df["event_label"].value_counts()

st.bar_chart(event_counts)

# ---------------- FILTERED ARTICLES ----------------

st.subheader("Filtered News Articles")

if len(filtered_df) == 0:

    st.warning("No articles found")

else:

    for index, row in filtered_df.iterrows():

        st.markdown(f"## {row['headline']}")

        # Description
        if pd.notna(row["short_description"]):
            st.write(row["short_description"])
        else:
            st.write("No description available")

        # Date
        st.write("📅 Date:", row["date"])

        # Event label
        st.write("🏷️ Event Label:", row["event_label"])

        st.write("---")

# ---------------- COMPLETE DATASET ----------------

with st.expander("View Complete Dataset"):

    st.dataframe(df)
