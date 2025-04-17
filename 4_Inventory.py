import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data/products_expanded_updated.csv")

# Streamlit page config
st.set_page_config(layout="wide",initial_sidebar_state="collapsed")

# Hide Streamlit default UI
hide_st_style = """
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .css-18e3th9 {padding-top: 2rem;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Page title
st.markdown("<h2 style='text-align: center; color: #4CAF50;'>Inventory Overview</h2>", unsafe_allow_html=True)

# Filter inputs
col1, col2, col3 = st.columns(3)

with col1:
    brand_filter = st.selectbox("Select Brand", options=[""] + sorted(df["Brand"].dropna().unique().tolist()))

with col2:
    category_filter = st.selectbox("Select Category", options=[""] + sorted(df["Category"].dropna().unique().tolist()))

with col3:
    id_filter = st.text_input("Enter Product ID")

# Filter logic
if st.button("Show Products"):
    filtered_df = df.copy()

    if id_filter:
        filtered_df = filtered_df[df["ID"].astype(str).str.strip().str.lower() == id_filter.strip().lower()]
    elif brand_filter:
        filtered_df = filtered_df[df["Brand"] == brand_filter]
    elif category_filter:
        filtered_df = filtered_df[df["Category"] == category_filter]
    else:
        filtered_df = pd.DataFrame()

    if not filtered_df.empty:
        st.success("Matching products found:")
        st.dataframe(
            filtered_df[["ID", "Name", "Brand", "Category", "Price", "Reorder_Level", "GST_Rate"]],
            use_container_width=True
        )
    else:
        st.warning("No matching products found.")

# Navigation button
if st.button("⬅️ Back to Dashboard"):
    st.switch_page("pages/2_Home_Dashboard.py")
