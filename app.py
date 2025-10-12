import streamlit as st
import plotly.express as px  # Import plotly express
import pandas as pd 
import numpy as np 

# --- 1. SET PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Scientific Visualization"
)

# --- 2. HEADER ---
st.header("Scientific Visualization", divider="gray")

# --- Data Simulation ---
# **IMPORTANT:** Replace this block with your actual data loading for arts_df
np.random.seed(42) 
data = {'Gender': np.random.choice(['Female', 'Male', 'Other'], size=100, p=[0.6, 0.35, 0.05])}
arts_df = pd.DataFrame(data)
# -----------------------

st.set_page_config(
    page_title="Gender Distribution Bar Chart (Plotly)"
)

st.title("📊 Gender Distribution in Arts Faculty")
st.markdown("This interactive bar chart is generated using **Plotly Express**.")

# 1. Calculate the gender counts and convert the Series to a DataFrame for Plotly
gender_counts_df = arts_df['Gender'].value_counts().reset_index()
# Rename columns to 'Gender' and 'Count' for clear mapping in Plotly
gender_counts_df.columns = ['Gender', 'Count'] 

# 2. Create the Plotly figure using px.bar()
fig = px.bar(
    gender_counts_df,
    x='Gender', 
    y='Count',
    title='Distribution of Gender in Arts Faculty',
    color='Gender', # Color the bars based on Gender
    color_discrete_sequence=['skyblue', 'lightcoral', 'lightgreen'],
    template='plotly_white' # Optional: Use a clean white background template
)

# 3. Update layout for clarity
fig.update_layout(
    xaxis_title='Gender',
    yaxis_title='Count',
    xaxis={'categoryorder': 'array', 'categoryarray': gender_counts_df['Gender']} # Ensure order matches the data
)

# 4. Display the Plotly figure in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.subheader("Raw Data Counts")
st.dataframe(gender_counts_df, hide_index=True)

