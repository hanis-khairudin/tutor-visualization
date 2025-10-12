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

# --- 3. DATA SIMULATION (Define arts_df for the chart) ---
# Replace this section with your actual data loading for arts_df
np.random.seed(42) 
data = {'Gender': np.random.choice(['Female', 'Male', 'Other'], size=100, p=[0.6, 0.35, 0.05])}
arts_df = pd.DataFrame(data)
# ----------------------------------------------------------------

st.title("📊 Gender Distribution in Arts Faculty (Plotly)")
st.markdown("This interactive visualization uses **Plotly Express**.")

# --- 4. CONVERTED CODE TO PLOTLY EXPRESS ---

# Calculate the gender counts and convert the Series to a DataFrame for Plotly
gender_counts_df = arts_df['Gender'].value_counts().reset_index()
gender_counts_df.columns = ['Gender', 'Count'] # Rename columns for clarity

# Create the Plotly figure using Plotly Express
fig = px.bar(
    gender_counts_df,
    x='Gender', 
    y='Count',
    title='Distribution of Gender in Arts Faculty',
    color='Gender', # Use gender for color mapping
    color_discrete_sequence=['skyblue', 'lightcoral', 'lightgreen'] # Set colors
)

# Update layout for better aesthetics (optional)
fig.update_layout(
    xaxis_title='Gender',
    yaxis_title='Count',
    xaxis={'categoryorder': 'total descending'} # Order bars by count
)

# Display the Plotly figure in Streamlit using st.plotly_chart()
st.plotly_chart(fig, use_container_width=True)

st.subheader("Count Details")
st.dataframe(gender_counts_df)
