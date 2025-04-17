import streamlit as st
from PIL import Image, ImageEnhance, ImageOps

st.set_page_config(page_title="Image Editor", layout="wide",initial_sidebar_state="collapsed")

st.markdown("<h2 style='text-align: center; color: #4A90E2;'>🖼️ Image Editor</h2>", unsafe_allow_html=True)

# Upload button
if st.button("📤 Upload an Image"):
    st.session_state.show_uploader = True

if "show_uploader" not in st.session_state:
    st.session_state.show_uploader = False

# Upload section
if st.session_state.show_uploader:
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        original_image = Image.open(uploaded_file)
        st.markdown("### ✨ Select an operation")

        operation = st.selectbox(
            "What would you like to do?",
            [
                "Transpose (Flip)",
                "Resize",
                "Enhance Contrast",
                "Enhance Brightness",
                "Enhance Sharpness",
                "Convert to Grayscale",
                "Invert Colors"
            ]
        )

        # Get manipulation options
        if operation == "Transpose (Flip)":
            flip_option = st.radio("Choose flip direction", ["Horizontal", "Vertical"])
        elif operation == "Resize":
            width = st.slider("Width", 50, 1000, original_image.width)
            height = st.slider("Height", 50, 1000, original_image.height)
        elif operation in ["Enhance Contrast", "Enhance Brightness", "Enhance Sharpness"]:
            factor = st.slider("Factor", 0.5, 3.0, 1.0)

        if st.button("Show Image"):
            edited_image = original_image.copy()

            if operation == "Transpose (Flip)":
                edited_image = ImageOps.mirror(edited_image) if flip_option == "Horizontal" else ImageOps.flip(edited_image)
            elif operation == "Resize":
                edited_image = edited_image.resize((width, height))
            elif operation == "Enhance Contrast":
                edited_image = ImageEnhance.Contrast(edited_image).enhance(factor)
            elif operation == "Enhance Brightness":
                edited_image = ImageEnhance.Brightness(edited_image).enhance(factor)
            elif operation == "Enhance Sharpness":
                edited_image = ImageEnhance.Sharpness(edited_image).enhance(factor)
            elif operation == "Convert to Grayscale":
                edited_image = edited_image.convert("L")
            elif operation == "Invert Colors":
                if edited_image.mode != 'RGB':
                    edited_image = edited_image.convert('RGB')
                edited_image = ImageOps.invert(edited_image)

            # Display both images
            st.markdown("## 🔍 Image Comparison")
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 🖼️ Original")
                st.image(original_image, use_container_width=True)

            with col2:
                st.markdown("### 🎨 Edited")
                st.image(edited_image, use_container_width=True)
        # Navigation button
if st.button("⬅️ Back to Dashboard"):
    st.switch_page("pages/2_Home_Dashboard.py")