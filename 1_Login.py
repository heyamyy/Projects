import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="Login | Wholesale Biz",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 🧾 Load users
try:
    users_df = pd.read_csv("data/users_updated.csv")
    users_df.columns = users_df.columns.str.strip().str.lower()
except FileNotFoundError:
    st.error("❌ User data file not found.")
    st.stop()
except Exception as e:
    st.error(f"⚠️ Error loading user data: {e}")
    st.stop()

# 🌙 Dark Theme CSS
st.markdown("""
    <style>
        body, .stApp {
            background-color: #0e1117;
            color: #e0e0e0;
        }
        .login-title {
            font-size: 36px;
            color: #00e5ff;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
            padding-top: 30px;
            margin-bottom: 20px;
        }
        .login-box {
            background-color: #1c1f26;
            padding: 40px 30px;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0,255,255,0.1);
            width: 100%;
            max-width: 400px;
            margin: 0 auto;
        }
        .stTextInput>div>div>input {
            font-size: 16px;
            padding: 10px;
            background-color: #2c2f36;
            color: #ffffff;
        }
        .stSelectbox>div>div {
            background-color: #2c2f36;
            color: white;
        }
        .stButton>button {
            background-color: #00e5ff;
            color: black;
            font-weight: bold;
            padding: 0.6em 2em;
            font-size: 16px;
            border-radius: 8px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #1de9b6;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# 🔐 Login Title
st.markdown('<div class="login-title">Login to Wholesale Biz</div>', unsafe_allow_html=True)

# 🔒 Login Box
with st.container():
    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Select Role", options=["Admin", "Staff", "Manager"])

    if st.button("Login"):
        if username and password and role:
            user_match = users_df[
                (users_df['username'] == username.strip()) &
                (users_df['password'] == password.strip()) &
                (users_df['role'].str.lower() == role.lower())
            ]

            if not user_match.empty:
                st.success(f"✅ Welcome, {role}!")
                st.session_state['authenticated'] = True
                st.session_state['user_role'] = role
                st.switch_page("pages/2_Home_Dashboard.py")
            else:
                st.error("❌ Invalid credentials or role.")
        else:
            st.warning("⚠️ Please fill all fields.")

    st.markdown('</div>', unsafe_allow_html=True)
