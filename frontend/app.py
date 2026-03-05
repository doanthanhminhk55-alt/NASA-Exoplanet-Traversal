import streamlit as st
import sys
import os
import plotly.express as px

# =====================================
# Path setup
# =====================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND_DIR = os.path.join(BASE_DIR, "backend")

sys.path.append(BACKEND_DIR)

from loader import ExoplanetLoader
from search import search_exoplanets


# =====================================
# Load data (cached)
# =====================================
@st.cache_data
def load_data():
    DATA_PATH = os.path.join(BASE_DIR, "data", "exoplanets.csv")
    loader = ExoplanetLoader(DATA_PATH)
    return loader.df


df = load_data()


# =====================================
# Default Session State
# =====================================
if "results" not in st.session_state:
    st.session_state.results = None

if "extra_columns" not in st.session_state:
    st.session_state.extra_columns = []

if "year" not in st.session_state:
    st.session_state.year = ""

if "facility" not in st.session_state:
    st.session_state.facility = ""


# =====================================
# Title
# =====================================
st.title("NASA Exoplanet Traversal")


# =====================================
# Query Panel
# =====================================
st.subheader("Query Panel")

years = sorted(df["Discovery Year"].dropna().unique())
facilities = sorted(df["Discovery Facility"].dropna().unique())

col1, col2 = st.columns(2)

year = col1.selectbox(
    "Discovery Year",
    [""] + list(years),
    key="year"
)

facility = col2.selectbox(
    "Discovery Facility",
    [""] + list(facilities),
    key="facility"
)

col3, col4 = st.columns(2)

search_clicked = col3.button("Search")
clear_clicked = col4.button("Clear")


# =====================================
# Search Logic
# =====================================
if search_clicked:

    if year == "" and facility == "":
        st.error("Please select at least one query value")

    else:

        results = search_exoplanets(
            df,
            None if year == "" else year,
            None if facility == "" else facility
        )

        st.session_state.results = results


# =====================================
# Clear Logic (FIXED)
# =====================================
if clear_clicked:

    st.session_state.results = None
    st.session_state.extra_columns = []

    st.session_state.pop("year", None)
    st.session_state.pop("facility", None)

    st.rerun()


# =====================================
# Column Controls (Bonus Feature)
# =====================================
st.divider()
st.subheader("Column Controls")

add_col, remove_col = st.columns(2)

with add_col:

    new_column = st.selectbox(
        "Add Column",
        [
            "Host Name",
            "Number of Planets",
            "Number of Stars"
        ]
    )

    if st.button("Add Column"):

        if new_column not in st.session_state.extra_columns:
            st.session_state.extra_columns.append(new_column)


with remove_col:

    if st.session_state.extra_columns:

        remove_column = st.selectbox(
            "Remove Column",
            st.session_state.extra_columns
        )

        if st.button("Remove Column"):
            st.session_state.extra_columns.remove(remove_column)


# =====================================
# Results Panel
# =====================================
st.divider()
st.subheader("Results Panel")

if st.session_state.results is not None:

    results = st.session_state.results

    base_columns = [
        "Discovery Year",
        "Discovery Facility",
        "Planet Name",
        "Planet Radius (Earth Radius)",
        "Planet Mass (Earth Mass)"
    ]

    display_columns = base_columns + st.session_state.extra_columns

    display_df = results[display_columns]

    # Sort by year
    display_df = display_df.sort_values(by="Discovery Year")

    # TABLE (scroll enabled)
    st.dataframe(
        display_df,
        height=400,
        use_container_width=True
    )

    st.caption(f"Total results: {len(display_df)}")


    # =====================================
    # Superpower Graph
    # =====================================
    st.subheader("Planet Mass Visualization")

    graph_df = display_df.dropna(
        subset=["Planet Mass (Earth Mass)"]
    )

    if not graph_df.empty:

        fig = px.scatter(
            graph_df.head(10),
            x="Planet Name",
            y="Planet Mass (Earth Mass)",
            size="Planet Mass (Earth Mass)",
            title="Mass Comparison of First 10 Planets",
            labels={
                "Planet Mass (Earth Mass)": "Mass (Earth Mass)"
            }
        )

        st.plotly_chart(fig, use_container_width=True)

else:
    st.info("No search performed yet.")