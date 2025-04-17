import streamlit as st

# Page config
st.set_page_config(
    page_title="Home DashBoards| Wholesale Biz",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",  # ✅ This collapses the sidebar by default
)
# Custom styling
st.markdown("""
    <style>
        .dashboard-title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            font-family: 'Segoe UI', sans-serif;
            color: #2c3e50;
            margin-bottom: 20px;
        }
        .function-btn {
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f0fbfc;
            border-radius: 12px;
            padding: 30px;
            text-align: center;
            font-size: 18px;
            font-weight: 600;
            color: #00bfa5;
            box-shadow: 0 3px 10px rgba(0,0,0,0.03);
            transition: all 0.3s ease-in-out;
            height: 100px;
        }
        .function-btn:hover {
            background-color: #ccf5f2;
            color: black;
            transform: scale(1.03);
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# Dashboard title
st.markdown('<div class="dashboard-title">📂 Select a Functionality</div>', unsafe_allow_html=True)

# Button grid layout
col1, col2, col3 = st.columns(3)
with col1:
    if st.markdown('<div class="function-btn">🔐 Login</div>', unsafe_allow_html=True):
        if st.button("Go", key="login"): st.switch_page("pages/1_Login.py")
    if st.markdown('<div class="function-btn">📦 Inventory</div>', unsafe_allow_html=True):
        if st.button("Go", key="inventory"): st.switch_page("pages/4_Inventory.py")
    if st.markdown('<div class="function-btn">📊 Reports</div>', unsafe_allow_html=True):
        if st.button("Go", key="reports"): st.switch_page("pages/6_Reports.py")

with col2:
    if st.markdown('<div class="function-btn">🏠 Dashboard</div>', unsafe_allow_html=True):
        if st.button("Go", key="dashboard"): st.switch_page("pages/2_Home_Dashboard.py")
    if st.markdown('<div class="function-btn">🛒 Add Product</div>', unsafe_allow_html=True):
        if st.button("Go", key="add_product"): st.switch_page("pages/3_Add_Product.py")
    if st.markdown('<div class="function-btn">📷 Image Editor</div>', unsafe_allow_html=True):
        if st.button("Go", key="image_editor"): st.switch_page("pages/8_Image_Editor.py")

with col3:
    if st.markdown('<div class="function-btn">💰 Sales</div>', unsafe_allow_html=True):
        if st.button("Go", key="sales"): st.switch_page("pages/5_Sales.py")
    if st.markdown('<div class="function-btn">🏭 Suppliers</div>', unsafe_allow_html=True):
        if st.button("Go", key="suppliers"): st.switch_page("pages/7_Suppliers.py")
    if st.markdown('<div class="function-btn">🏡 Home</div>', unsafe_allow_html=True):
        if st.button("Go", key="home"): st.switch_page("pages/9_Home.py")
