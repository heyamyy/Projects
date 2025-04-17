import streamlit as st
import os

st.set_page_config(
    page_title="Home | Wholesale Biz",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ✅ Background Image and CSS Styling
st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("background.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        .title {{
            font-size: 52px;
            font-weight: 600;
            font-family: 'Segoe UI', sans-serif;
            color: #ffffff;
            text-align: center;
            margin-top: 40px;
            animation: fadeInDown 1.2s ease-in-out;
        }}

        .subtitle {{
            font-size: 20px;
            text-align: center;
            color: #e0f7fa;
            margin-bottom: 30px;
            animation: fadeIn 2s ease-in-out;
        }}

        .about {{
            max-width: 900px;
            margin: auto;
            font-size: 18px;
            color: #212121;
            line-height: 1.7;
            background-color: rgba(255, 255, 255, 0.95);
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0px 10px 20px rgba(0,0,0,0.1);
            animation: slideIn 1.5s ease;
        }}

        .stButton>button {{
            background-color: #4db6ac;
            color: white;
            font-weight: bold;
            padding: 0.8em 2.5em;
            font-size: 18px;
            border-radius: 10px;
            margin-top: 40px;
            transition: background-color 0.3s ease, color 0.3s ease;
        }}

        .stButton>button:hover {{
            background-color: #80cbc4;
            color: #000;
        }}

        .button-div {{
            text-align: center;
        }}

        @keyframes fadeInDown {{
            0% {{ opacity: 0; transform: translateY(-30px); }}
            100% {{ opacity: 1; transform: translateY(0); }}
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}

        @keyframes slideIn {{
            0% {{ transform: translateY(50px); opacity: 0; }}
            100% {{ transform: translateY(0px); opacity: 1; }}
        }}
    </style>
""", unsafe_allow_html=True)

# 🔷 Title & Subtitle
st.markdown('<div class="title">Welcome to Wholesale Biz</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your all-in-one solution to manage inventory, sales & suppliers</div>', unsafe_allow_html=True)

# 📖 About
st.markdown("""
<div class="about">
    <p><strong>Wholesale Biz</strong> is a clean, modern solution for wholesale shop owners. It's built to simplify your daily tasks while giving you control over your products, sales, reports, and suppliers.</p>
    <ul>
        <li>✔️ Manage inventory in real-time</li>
        <li>✔️ Record and analyze sales data</li>
        <li>✔️ Generate actionable reports</li>
        <li>✔️ Track and manage suppliers by brand</li>
    </ul>
    <p>This app is crafted using Python, Streamlit, and data tools like Pandas, with a lightweight and elegant interface.</p>
</div>
""", unsafe_allow_html=True)

# 🚀 Start Button
st.markdown('<div class="button-div">', unsafe_allow_html=True)
if st.button("Start Now"):
    st.switch_page("pages/1_Login.py")
st.markdown('</div>', unsafe_allow_html=True)
