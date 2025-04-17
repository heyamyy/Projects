import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="Wholesale Biz Launcher",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 🌸 Custom CSS: Styling + Light Background + Subtle Animation
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
        }

        .main {
            background: #fefefe;
            font-family: 'Segoe UI', sans-serif;
        }

        .loader-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 90vh;
        }

        .title {
            font-size: 36px;
            color: #2c3e50;
            margin-bottom: 10px;
            animation: fadeIn 2s ease-in-out;
        }

        .subtitle {
            font-size: 18px;
            color: #6c757d;
            animation: fadeIn 3s ease-in-out;
        }

        .spinner {
            border: 6px solid #e0e0e0;
            border-top: 6px solid #3498db;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            animation: spin 1s linear infinite;
            margin-top: 30px;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
    </style>
""", unsafe_allow_html=True)

# 🖼️ Launcher UI
st.markdown("""
    <div class="loader-container">
        <div class="title">Launching Wholesale Biz</div>
        <div class="subtitle">Preparing your dashboard...</div>
        <div class="spinner"></div>
    </div>
""", unsafe_allow_html=True)

# Short delay before redirect
time.sleep(2)

# 🔁 Redirect to homepage
st.switch_page("pages/9_Home.py")
strea