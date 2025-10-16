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
    page_title="Gender Distribution Pie Chart"
)

st.title("🥧 Gender Distribution Pie Chart")
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
    page_title="Gender Distribution Bar Chart"
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


# --- MOCK DATA SETUP (Replace with your actual data loading) ---
# Create a mock arts_df for demonstration purposes
np.random.seed(42) # for reproducibility
n_students = 200
arts_df = pd.DataFrame({
    'Gender': np.random.choice(['Female', 'Male', 'Non-Binary'], size=n_students, p=[0.55, 0.40, 0.05]),
    'Did you ever attend a Coaching center?': np.random.choice(['Yes', 'No'], size=n_students, p=[0.6, 0.4])
})
# -----------------------------------------------------------------


st.title('Coaching Center Attendance Analysis 📊')
st.subheader('Coaching Center Attendance by Gender (Arts Faculty)')

# 1. Create the Plotly Express Grouped Bar Chart
# px.histogram() automatically calculates the counts (like sns.countplot)
fig = px.histogram(
    arts_df,
    x='Gender',
    color='Did you ever attend a Coaching center?', # This acts as the 'hue' for grouping
    barmode='group',                            # Displays bars side-by-side
    
    # Customize the colors and labels (similar to Matplotlib's 'palette')
    color_discrete_map={'Yes': 'darkgreen', 'No': 'firebrick'}, 
    labels={'Gender': 'Student Gender', 'count': 'Number of Students'} 
)

# 2. Update Layout for a professional look and clearer titles
fig.update_layout(
    xaxis_title='Gender',
    yaxis_title='Number of Students',
    legend_title='Attended Coaching Center',
    title_x=0.5 # Center the chart title
)

# Optional: Add text labels on top of the bars
fig.update_traces(texttemplate='%{y}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')


# 3. Display the Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)
