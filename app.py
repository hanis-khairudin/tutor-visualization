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


# --- Sample Data Creation (Replace with your actual data loading/processing) ---
# NOTE: You'll need to load 'arts_df' in your actual Streamlit app.
# This section is just for demonstration purposes so the code runs.
try:
    # Dummy Data for Demonstration
    data = {
        'Q7. In your opinion,the best aspect of the program is': [
            'Faculty Expertise', 'Curriculum', 'Flexibility', 'Faculty Expertise', 
            'Networking', 'Curriculum', 'Resources', 'Faculty Expertise', 
            'Flexibility', 'Curriculum', 'Resources', 'Curriculum', None
        ],
        'Q8. In your opinion,the next best aspect of the program is': [
            'Curriculum', 'Flexibility', 'Faculty Expertise', 'Resources', 
            'Faculty Expertise', 'Networking', 'Curriculum', 'Flexibility', 
            'Resources', 'Networking', 'Faculty Expertise', None, 'Curriculum'
        ]
    }
    arts_df = pd.DataFrame(data)

except Exception as e:
    st.error(f"Error creating dummy data: {e}. Please ensure 'arts_df' is loaded.")
    arts_df = pd.DataFrame() # Create empty DataFrame to prevent errors

# --- Streamlit Application ---

st.set_page_config(layout="wide", page_title="Program Aspects Analysis (Plotly Express)")

st.title("Program Aspects Analysis: Best & Next Best 📊")
st.markdown("---")

# Define the number of top aspects to show
top_n = st.slider('Select the number of top aspects to display:', 
                   min_value=5, max_value=20, value=10)

# --- Data Processing Logic ---

required_cols = ['Q7. In your opinion,the best aspect of the program is', 
                 'Q8. In your opinion,the next best aspect of the program is']

if all(col in arts_df.columns for col in required_cols):
    
    # 1. Combine the responses from Q7 and Q8
    best_aspects = pd.concat([
        arts_df[required_cols[0]],
        arts_df[required_cols[1]]
    ]).dropna()

    # 2. Count the occurrences of each aspect
    aspect_counts = best_aspects.value_counts().reset_index()
    aspect_counts.columns = ['Aspect', 'Count'] 

    # 3. Get the top N aspects
    top_aspects = aspect_counts.head(top_n)
    
    # Ensure the Aspect order is consistent for the plot
    top_aspects['Aspect'] = pd.Categorical(top_aspects['Aspect'], categories=top_aspects['Aspect'], ordered=True)

    # --- Visualization (Plotly Express) ---

    st.subheader(f"Top {top_n} Most Frequently Mentioned Best Aspects of the Program")

    # Create an interactive horizontal bar chart using Plotly Express
    fig = px.bar(
        top_aspects,
        x='Count',
        y='Aspect',
        orientation='h', # Horizontal bar chart
        title=f'Top {top_n} Most Frequently Mentioned Aspects (Combined Q7 & Q8)',
        labels={'Count': 'Number of Mentions', 'Aspect': 'Program Aspect'},
        color='Count', # Color by count
        color_continuous_scale=px.colors.sequential.Viridis # Use a Viridis-like scale
    )
    
    # Customize the layout for better readability
    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'}, # Order bars from smallest to largest count
        xaxis_title='Number of Mentions',
        yaxis_title='Program Aspect',
        hovermode="y unified"
    )
    
    # Display the interactive plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # --- Data Table ---
    st.markdown("---")
    st.subheader("Data Table for Top Aspects")
    st.dataframe(top_aspects)

else:
    st.error("The DataFrame 'arts_df' is missing the required columns (Q7 or Q8). Please check your data loading.")


import streamlit as st
import pandas as pd
import plotly.express as px

# --- Sample Data Creation (Replace with your actual data loading/processing) ---
# NOTE: You'll need to load 'arts_df' in your actual Streamlit app.
# This section is just for demonstration purposes so the code runs.
try:
    # Dummy Data for Demonstration
    data = {
        'Arts Program': [
            'Visual Arts', 'Music', 'Theatre', 'Visual Arts', 'Music', 
            'Dance', 'Visual Arts', 'Theatre', 'Music', 'Dance', 
            'Visual Arts', 'Film', 'Music', 'Visual Arts', 'Film'
        ]
    }
    arts_df = pd.DataFrame(data)

except Exception as e:
    st.error(f"Error creating dummy data: {e}. Please ensure 'arts_df' is loaded.")
    arts_df = pd.DataFrame() 

# --- Streamlit Application ---

st.set_page_config(layout="wide", page_title="Arts Program Distribution")

st.title("Distribution of Arts Programs 🎨")
st.markdown("---")

# --- Data Processing Logic ---

if 'Arts Program' in arts_df.columns:
    
    # 1. Count the occurrences of each Arts Program
    program_counts = arts_df['Arts Program'].value_counts().reset_index()
    program_counts.columns = ['Arts Program', 'Count'] 

    # --- Visualization (Plotly Express) ---

    st.subheader("Count of Students per Arts Program")

    # Create an interactive horizontal bar chart using Plotly Express
    fig = px.bar(
        program_counts,
        x='Count',
        y='Arts Program',
        orientation='h', # Horizontal bar chart
        title='Distribution of Arts Programs',
        labels={'Count': 'Number of Students', 'Arts Program': 'Arts Program'},
        color='Arts Program', # Color by program
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    
    # Customize the layout
    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'}, # Order bars from smallest to largest count
        xaxis_title='Number of Students',
        yaxis_title='Arts Program',
        showlegend=False, # Hide the legend as colors match the Y-axis
        hovermode="y unified"
    )
    
    # Display the interactive plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # --- Data Table ---
    st.markdown("---")
    st.subheader("Program Counts Data")
    st.dataframe(program_counts)

else:
    st.error("The DataFrame 'arts_df' is missing the 'Arts Program' column. Please check your data loading.")


# --- Sample Data Creation (Replace with your actual data loading/processing) ---
# NOTE: You'll need to load 'arts_df' in your actual Streamlit app.
# This section is just for demonstration purposes so the code runs.
try:
    # Column name for easy reference
    Q_COL = 'Do you feel that the quality of education improved at EU over the last year?'
    
    # Dummy Data for Demonstration
    data = {
        Q_COL: [
            'Yes, significantly', 'Yes, a little', 'No change', 'Yes, significantly', 
            'No, it worsened', 'Yes, a little', 'No change', 'Yes, a little', 
            'Yes, significantly', 'No change', 'No, it worsened', 'Yes, a little'
        ]
    }
    arts_df = pd.DataFrame(data)

except Exception as e:
    st.error(f"Error creating dummy data: {e}. Please ensure 'arts_df' is loaded.")
    arts_df = pd.DataFrame() 

# --- Streamlit Application ---

st.set_page_config(layout="wide", page_title="Education Quality Perception")

st.title("Student Perception on Education Quality Improvement 🎓")
st.markdown("---")

# Define the question column name
Q_COL = 'Do you feel that the quality of education improved at EU over the last year?'

# --- Data Processing Logic ---

if Q_COL in arts_df.columns:
    
    # 1. Count the occurrences of each response
    education_quality_counts = arts_df[Q_COL].value_counts().reset_index()
    education_quality_counts.columns = ['Education Quality Improved', 'Count'] 

    # --- Visualization (Plotly Express) ---

    st.subheader("Results from Arts Faculty Survey")

    # Order the categories logically for the plot
    order = ['Yes, significantly', 'Yes, a little', 'No change', 'No, it worsened']
    
    # Filter and reindex to ensure all expected categories appear, even if count is 0
    # This also applies the correct visual order
    education_quality_counts['Education Quality Improved'] = pd.Categorical(
        education_quality_counts['Education Quality Improved'], 
        categories=order, 
        ordered=True
    )
    education_quality_counts = education_quality_counts.sort_values('Education Quality Improved')

    # Create an interactive bar chart using Plotly Express
    fig = px.bar(
        education_quality_counts,
        x='Education Quality Improved',
        y='Count',
        title='Student Perception on Education Quality Improvement (Arts Faculty)',
        labels={'Count': 'Number of Students', 'Education Quality Improved': 'Did Education Quality Improve?'},
        color='Education Quality Improved', # Color by response
        color_discrete_sequence=px.colors.sequential.Viridis # Use a color scheme
    )
    
    # Customize the layout
    fig.update_layout(
        xaxis_title='Did Education Quality Improve?',
        yaxis_title='Number of Students',
        xaxis={'categoryorder':'array', 'categoryarray': order}, # Enforce the custom order
        showlegend=False, 
        hovermode="x unified"
    )
    
    # Display the interactive plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # --- Data Table ---
    st.markdown("---")
    st.subheader("Response Counts Data")
    st.dataframe(education_quality_counts)

else:
    st.error(f"The DataFrame 'arts_df' is missing the column: '{Q_COL}'. Please check your data loading.")


# --- Sample Data Creation (Replace with your actual data loading/processing) ---
# NOTE: You'll need to load 'arts_df' in your actual Streamlit app.
try:
    # Dummy Data for Demonstration
    data = {
        'S.S.C (GPA)': [4.5, 4.8, 3.9, 5.0, 4.2, 4.7, 4.0, 4.9, 3.5, 4.6, 3.0, 5.0, 4.1],
        'H.S.C (GPA)': [4.2, 4.6, 3.5, 4.9, 4.0, 4.5, 3.8, 4.7, 3.3, 4.4, 3.1, 4.8, 4.0],
        'Arts Program': ['Music', 'Visual Arts', 'Theatre', 'Visual Arts', 'Dance', 'Music', 'Theatre', 'Visual Arts', 'Dance', 'Film', 'Music', 'Visual Arts', 'Film']
    }
    arts_df = pd.DataFrame(data)

except Exception as e:
    st.error(f"Error creating dummy data: {e}. Please ensure 'arts_df' is loaded.")
    arts_df = pd.DataFrame() 

# --- Streamlit Application ---

st.set_page_config(layout="wide", page_title="GPA Correlation Analysis (Plotly Express)")

st.title("S.S.C (GPA) vs H.S.C (GPA) Correlation 📊")
st.markdown("---")

# Define the required column names
SSC_COL = 'S.S.C (GPA)'
HSC_COL = 'H.S.C (GPA)'

# --- Data Visualization Logic (Plotly Express) ---

if SSC_COL in arts_df.columns and HSC_COL in arts_df.columns:
    
    st.subheader("Interactive Scatter Plot for Academic Performance")

    # Create an interactive scatter plot using Plotly Express
    fig = px.scatter(
        arts_df,
        x=SSC_COL,
        y=HSC_COL,
        title='S.S.C (GPA) vs H.S.C (GPA) in Arts Faculty',
        labels={SSC_COL: SSC_COL, HSC_COL: HSC_COL},
        color='Arts Program', # Use 'Arts Program' to differentiate points
        hover_data=['Arts Program'] # Show the program when hovering
    )
    
    # Customize the layout
    fig.update_layout(
        xaxis_title=SSC_COL,
        yaxis_title=HSC_COL,
        hovermode="closest"
    )

    # Add a diagonal line to indicate perfect correlation (y=x)
    max_gpa = max(arts_df[SSC_COL].max(), arts_df[HSC_COL].max())
    min_gpa = min(arts_df[SSC_COL].min(), arts_df[HSC_COL].min())
    
    fig.add_shape(
        type='line',
        x0=min_gpa, y0=min_gpa,
        x1=max_gpa, y1=max_gpa,
        line=dict(color='Red', width=1, dash='dash'),
        name='Perfect Correlation'
    )
    
    # Display the interactive plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # --- Insight ---
    st.markdown("""
    ### Analysis Notes
    * **Points near the red dashed line** indicate consistent GPA performance between S.S.C. and H.S.C.
    * **Points significantly above the line** suggest an improvement in GPA from S.S.C. to H.S.C.
    * **Points significantly below the line** suggest a drop in GPA from S.S.C. to H.S.C.
    """)

else:
    st.error(f"The DataFrame 'arts_df' is missing one or both required columns: '{SSC_COL}' or '{HSC_COL}'. Please check your data loading.")
