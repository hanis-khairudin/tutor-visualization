# --- 1. IMPORT LIBRARIES ---
import streamlit as st
import pandas as pd
import plotly.express as px

# --- 2. PAGE CONFIGURATION ---
st.set_page_config(page_title="🧠🔬 Scientific Visualization")

st.header("🧠 Scientific Visualization 🔬", divider="gray")
st.write("Explore how **data** transforms into **insightful visuals** that tell powerful stories 📊💡")

# --- 3. LOAD DATA FROM GITHUB ---
# ⚠️ Replace this link with your actual raw GitHub CSV URL
url = "https://raw.githubusercontent.com/hanis-khairudin/tutor-visualization/refs/heads/main/ARTS_STUDENT-SURVEY_exported.csv"

try:
    arts_df = pd.read_csv(url)
    st.success("✅ Dataset loaded successfully from GitHub!")
    st.dataframe(arts_df.head())

    # --- 4. GENDER DISTRIBUTION VISUALIZATION ---
    st.subheader("👩‍🎨 Gender Distribution in Arts Faculty")

    if 'Gender' in arts_df.columns:
        gender_counts = arts_df['Gender'].value_counts().reset_index()
        gender_counts.columns = ['Gender', 'Count']

        fig = px.bar(
            gender_counts,
            x='Gender',
            y='Count',
            color='Gender',
            color_discrete_sequence=['skyblue', 'lightcoral'],
            title='Distribution of Gender in Arts Faculty'
        )
        fig.update_layout(
            xaxis_title='Gender',
            yaxis_title='Count',
            title_x=0.5,
            template='plotly_white'
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("❌ Column 'Gender' not found in your dataset.")
except Exception as e:
    st.error(f"⚠️ Unable to load dataset. Please check your GitHub raw URL.\n\nError: {e}")
