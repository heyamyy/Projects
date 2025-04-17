import streamlit as st
import pandas as pd
import os

# Set page config
st.set_page_config(page_title="Add Product", layout="wide", initial_sidebar_state="collapsed")

# 🎨 Custom CSS styling
st.markdown("""
    <style>
        body { background-color: #f4f9ff; }
        .add-title {
            font-family: 'Segoe UI', sans-serif;
            font-size: 36px;
            color: #2c3e50;
            margin-bottom: 10px;
            animation: fadeInDown 1s ease-in-out;
        }
        .form-box {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
            margin-top: 20px;
        }
        .stButton>button {
            background-color: #009688;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 10px;
            border: none;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #4db6ac;
            color: black;
        }
        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
""", unsafe_allow_html=True)

# 🗂 File paths
PRODUCT_FILE = "data/products.csv"
BACKUP_FILE = "data/products_expanded_updated.csv"

# 🔄 Ensure file exists
if not os.path.exists(PRODUCT_FILE) or os.stat(PRODUCT_FILE).st_size == 0:
    st.warning("🛠 Creating new product file with default structure...")
    default_columns = [
        "ID", "Name", "Brand", "Price", "Quantity", 
        "GST_Rate", "Category", "Reorder_Level", "ImagePath"
    ]
    pd.DataFrame(columns=default_columns).to_csv(PRODUCT_FILE, index=False)

# 📄 Load product data
df = pd.read_csv(PRODUCT_FILE)

# ✅ Get dynamic dropdown options
companies = sorted(df["Brand"].dropna().unique().tolist())
categories = sorted(df["Category"].dropna().unique().tolist())

# 🏷️ Title
st.markdown("<div class='add-title'>📦 Add New Product</div>", unsafe_allow_html=True)
st.write("---")

# 📝 Product form
with st.form("product_form", clear_on_submit=True):
    st.markdown("<div class='form-box'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        brand_option = st.selectbox("Select Brand", companies + ["Other"])
        brand = st.text_input("Enter Brand", value="" if brand_option != "Other" else "")
        if brand_option != "Other":
            brand = brand_option

        product_name = st.text_input("Product Name")

        category_option = st.selectbox("Select Category", categories + ["Other"])
        category = st.text_input("Enter Category", value="" if category_option != "Other" else "")
        if category_option != "Other":
            category = category_option

    with col2:
        quantity = st.number_input("Quantity", min_value=1, value=10)
        price = st.number_input("Price (₹)", min_value=0.0, value=50.0, step=0.5)
        image = st.file_uploader("Upload Product Image", type=["png", "jpg", "jpeg"])

    submitted = st.form_submit_button("➕ Add Product")
    st.markdown("</div>", unsafe_allow_html=True)

# ✅ On submit: Save product
if submitted:
    if not product_name or not brand or not category:
        st.warning("⚠️ Please fill all fields (Product Name, Brand, and Category).")
    else:
        new_id = df["ID"].max() + 1 if not df.empty else 1
        new_product = {
            "ID": new_id,
            "Name": product_name,
            "Brand": brand,
            "Price": price,
            "Quantity": quantity,
            "GST_Rate": 18.0,
            "Category": category,
            "Reorder_Level": 10,
            "ImagePath": image.name if image else ""
        }

        # 📥 Append and save
        df = pd.concat([df, pd.DataFrame([new_product])], ignore_index=True)
        df.to_csv(PRODUCT_FILE, index=False)
        df.to_csv(BACKUP_FILE, index=False)

        # 🖼 Save image
        if image:
            image_dir = "data/images"
            os.makedirs(image_dir, exist_ok=True)
            with open(os.path.join(image_dir, image.name), "wb") as f:
                f.write(image.read())

        st.success(f"✅ Product '{product_name}' added successfully!")
        st.balloons()

# 🔄 Navigation Button
st.markdown("###")
if st.button("🏠 Go to Home Dashboard"):
    st.switch_page("pages/2_Home_Dashboard.py")
