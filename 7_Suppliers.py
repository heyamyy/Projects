import streamlit as st
import pandas as pd

# --- Load supplier data ---
supplier_df = pd.read_csv("data/suppliers_updated.csv")

# --- Page config ---
st.set_page_config(page_title="Supplier Manager", layout="wide",initial_sidebar_state="collapsed")
st.title("🚚 Supplier Manager")
st.markdown("Add and view suppliers by brand.")

# --- CSS Styling & Animation ---
st.markdown("""
    <style>
        body {
            background-color: #f7f9fc;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
        .supplier-card {
            padding: 1em;
            border-radius: 12px;
            background: linear-gradient(145deg, #e6f7ff, #ccf2ff);
            box-shadow: 4px 4px 10px rgba(0,0,0,0.05);
            margin-bottom: 1.2em;
            color: #1a1a1a;
            font-family: 'Segoe UI', sans-serif;
            transition: transform 0.2s ease;
        }
        .supplier-card:hover {
            transform: scale(1.02);
        }
        .supplier-card h4 {
            margin-bottom: 0.4em;
            color: #004d66;
        }
        .supplier-card p {
            margin: 0.2em 0;
        }
    </style>
""", unsafe_allow_html=True)

# --- Add New Supplier ---
st.subheader("➕ Add New Supplier")
with st.form("add_supplier_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Supplier Name")
        brand = st.text_input("Brand")
        contact = st.text_input("Contact Number")
    with col2:
        email = st.text_input("Email")
        address = st.text_area("Address")
        rating = st.slider("Rating", 1, 5, 4)

    submitted = st.form_submit_button("Add Supplier")
    if submitted:
        new_supplier = {
            "Name": name,
            "Brand": brand,
            "Contact": contact,
            "Email": email,
            "Address": address,
            "Rating": rating
        }
        supplier_df = pd.concat([supplier_df, pd.DataFrame([new_supplier])], ignore_index=True)
        supplier_df.to_csv("data/suppliers_updated.csv", index=False)
        st.success("🎉 New supplier added successfully!")
        st.rerun()


st.markdown("---")

# --- Search Filter Dropdown ---
st.subheader("🔍 Search Suppliers by Brand")
brand_options = sorted(supplier_df["Brand"].dropna().unique())
selected_brand = st.selectbox("Select Brand", ["All"] + brand_options)

if selected_brand != "All":
    filtered_df = supplier_df[supplier_df["Brand"] == selected_brand]
else:
    filtered_df = supplier_df

# --- Display Supplier Cards ---
st.markdown("### 📋 Supplier List")
if filtered_df.empty:
    st.warning("No suppliers found for this brand.")
else:
    for _, row in filtered_df.iterrows():
        st.markdown(f"""
            <div class="supplier-card">
                <h4>{row['Name']} ({row['Brand']})</h4>
                <p>📞 <strong>{row['Contact']}</strong></p>
                <p>📧 <strong>{row['Email']}</strong></p>
                <p>📍 {row['Address']}</p>
                <p>⭐ <strong>Rating:</strong> {row['Rating']}</p>
            </div>
        """, unsafe_allow_html=True)

# 🔄 Navigation Button
st.markdown("###")
if st.button("🏠 Go to Home Dashboard"):
    st.switch_page("pages/2_Home_Dashboard.py")
