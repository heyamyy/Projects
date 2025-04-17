import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration and hide sidebar
st.set_page_config(layout="wide",initial_sidebar_state="collapsed")
hide_st_style = """
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .css-18e3th9 {padding-top: 2rem;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("📊 Sales Report Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload Sales CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Parse date column safely
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=True)

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head(), use_container_width=True)

    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    categorical_columns = df.select_dtypes(exclude=['number']).columns.tolist()
    all_columns = df.columns.tolist()

    chart_type = st.selectbox("📉 Select Chart Type", [
        "Bar Chart", "Line Chart", "Pie Chart",
        "Scatter Plot", "Histogram", "Box Plot", "Heatmap"
    ])

    show_fields = False
    if chart_type != "Heatmap" and chart_type != "Pie Chart":
        x_axis = st.selectbox("Select X-axis", all_columns)
        y_axis = st.selectbox("Select Y-axis", all_columns)
        show_fields = True
    elif chart_type == "Pie Chart":
        pie_col = st.selectbox("Select Category for Pie Chart", categorical_columns)
        show_fields = True
    else:
        show_fields = True  # Heatmap doesn't need selection

    if show_fields and st.button("Show Chart"):
        fig, ax = plt.subplots(figsize=(9, 6))

        if chart_type == "Bar Chart":
            ax.bar(df[x_axis], df[y_axis], color="skyblue")
            ax.set_title(f"Bar Chart of {y_axis} by {x_axis}")
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)

        elif chart_type == "Line Chart":
            ax.plot(df[x_axis], df[y_axis], marker="o", linestyle="-", color="green")
            ax.set_title(f"Line Chart of {y_axis} over {x_axis}")
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)

        elif chart_type == "Scatter Plot":
            ax.scatter(df[x_axis], df[y_axis], color="red")
            ax.set_title(f"Scatter Plot of {y_axis} vs {x_axis}")
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)

        elif chart_type == "Histogram":
            ax.hist(df[x_axis], bins=20, color="orange", edgecolor="black", alpha=0.7)
            ax.set_title(f"Histogram of {x_axis}")
            ax.set_xlabel(x_axis)
            ax.set_ylabel("Frequency")

        elif chart_type == "Box Plot":
            sns.boxplot(x=df[x_axis], y=df[y_axis], ax=ax)
            ax.set_title(f"Box Plot of {y_axis} by {x_axis}")

        elif chart_type == "Heatmap":
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
            ax.set_title("Correlation Heatmap")

        elif chart_type == "Pie Chart":
            pie_data = df[pie_col].value_counts()
            ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
            ax.set_title(f"Pie Chart of {pie_col}")

        st.pyplot(fig)
        plt.close(fig)

# Navigation button
if st.button("⬅️ Back to Dashboard"):
    st.switch_page("pages/2_Home_Dashboard.py")
