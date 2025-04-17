import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Sales | Wholesale Biz",
    layout="wide",
    page_icon="📊",
     initial_sidebar_state="collapsed"
)

# Load the sales data
sales_df = pd.read_csv("data/sales_updated.csv")  # Adjust path as needed

# Custom CSS
st.markdown("""
    <style>
        body {
            background-color: #f4f9f9;
        }
        .main-title {
            font-size: 42px;
            color: #34495e;
            text-align: center;
            padding-top: 10px;
            font-family: 'Segoe UI', sans-serif;
        }
        .sub-heading {
            font-size: 20px;
            text-align: center;
            color: #7f8c8d;
        }
        .metric-box {
            background-color: #e0f7fa;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 18px;
            color: #006064;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-title">📈 Sales Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-heading">Monitor your sales performance and customer behavior</div>', unsafe_allow_html=True)

# Summary Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="metric-box">🧾 Total Transactions<br><b>{}</b></div>'.format(len(sales_df)), unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-box">💰 Total Sales Amount<br><b>₹{}</b></div>'.format(int(sales_df["Total"].sum())), unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-box">👥 Unique Customers<br><b>{}</b></div>'.format(sales_df["Customer"].nunique()), unsafe_allow_html=True)

st.markdown("---")

# Sales Over Time
st.subheader("📅 Sales Over Time")
sales_df["Date"] = pd.to_datetime(sales_df["Date"])
sales_by_date = sales_df.groupby("Date")["Total"].sum().reset_index()

fig1 = px.area(
    sales_by_date,
    x="Date",
    y="Total",
    title="Daily Sales Trend",
    color_discrete_sequence=["#00bfa5"]
)
st.plotly_chart(fig1, use_container_width=True)

# Top Customers
st.subheader("🏆 Top 5 Customers")
top_customers = sales_df.groupby("Customer")["Total"].sum().sort_values(ascending=False).head(5).reset_index()

fig2 = px.bar(
    top_customers,
    x="Customer",
    y="Total",
    title="Top Customers by Sales",
    color="Customer",
    color_discrete_sequence=px.colors.qualitative.Set2
)
st.plotly_chart(fig2, use_container_width=True)

# Optional: Product ID breakdown
st.subheader("🛒 Product-wise Sales")
product_sales = sales_df.groupby("ProductID")["Total"].sum().reset_index().sort_values(by="Total", ascending=False)

fig3 = px.pie(
    product_sales.head(6),
    values="Total",
    names="ProductID",
    title="Top Products by Sales",
    hole=0.4
)
st.plotly_chart(fig3, use_container_width=True)

# Image (optional visual enhancement)
st.image("https://cdn.pixabay.com/photo/2017/08/10/07/32/shopping-2616824_1280.jpg", use_column_width=True, caption="Sales Flow Representation")

# Navigation button
if st.button("⬅️ Back to Dashboard"):
    st.switch_page("pages/2_Home_Dashboard.py")