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

import streamlit as st
import plotly.express as px  # Import Plotly Express
import pandas as pd 
import numpy as np 

# --- Data Simulation ---
# **IMPORTANT:** Replace this block with your actual data loading for arts_df
np.random.seed(42) 
data = {'Gender': np.random.choice(['Female', 'Male', 'Other'], size=100, p=[0.6, 0.35, 0.05])}
arts_df = pd.DataFrame(data)
# -----------------------

st.set_page_config(
    page_title="Gender Distribution Pie Chart (Plotly)"
)

st.title("🥧 Gender Distribution Pie Chart (Plotly)")
st.markdown("This interactive visualization uses **Plotly Express**.")

# 1. Calculate the gender counts and prepare data for Plotly
# Plotly Express needs a DataFrame with columns for 'names' and 'values'.
gender_counts_df = arts_df['Gender'].value_counts().reset_index()
# Rename columns for clear mapping in Plotly
gender_counts_df.columns = ['Gender', 'Count'] 

# 2. Create the Plotly figure using px.pie()
# 'names' is the categorical variable (labels)
# 'values' is the numerical variable (counts/size of slices)
fig = px.pie(
    gender_counts_df, 
    names='Gender', 
    values='Count', 
    title='Distribution of Gender in Arts Faculty',
    color='Gender', # Color based on the Gender category
    color_discrete_sequence=['skyblue', 'lightcoral', 'lightgreen'], # Define colors
    hole=0.3 # Optional: Makes it a donut chart for better label visibility
)

# Optional: Adjust title position and hover text
fig.update_traces(
    textposition='inside', 
    textinfo='percent+label',
    hoverinfo="label+percent+value" # Shows category, percentage, and count on hover
)
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide') # Adjust text size

# 3. Display the Plotly figure in Streamlit
# This replaces st.pyplot(fig)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Count Details")
st.dataframe(gender_counts_df, hide_index=True)

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

