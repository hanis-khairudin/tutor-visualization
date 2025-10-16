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

# --- 5. GENDER DISTRIBUTION (PIE CHART) ---
st.subheader("🥧 Gender Representation Overview")

# Only run if Gender column exists
if 'Gender' in arts_df.columns:
    # Prepare data
    gender_counts = arts_df['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']

    # Add emoji decoration for label clarity
    gender_counts['Gender'] = gender_counts['Gender'].replace({
        'Male': '👨 Male',
        'Female': '👩 Female'
    })

    # Create Plotly Express pie chart
    fig_pie = px.pie(
        gender_counts,
        names='Gender',
        values='Count',
        color='Gender',
        color_discrete_sequence=['skyblue', 'lightcoral'],
        title='🎯 Distribution of Gender in Arts Faculty',
        hole=0.3  # donut-style for modern look
    )

    # Decorate the chart layout
    fig_pie.update_traces(
        textinfo='label+percent',
        textfont_size=14,
        pull=[0.05 if g == gender_counts['Gender'].max() else 0 for g in gender_counts['Gender']],
        hovertemplate="<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}"
    )

    fig_pie.update_layout(
        title_x=0.5,
        title_font=dict(size=20, color='black'),
        template='plotly_white'
    )

    st.plotly_chart(fig_pie, use_container_width=True)
else:
    st.warning("⚠️ Column 'Gender' not found. Please check your dataset columns.")


# --- 6. COACHING CENTER ATTENDANCE BY GENDER ---
st.subheader("🏫 Coaching Center Attendance by Gender")

# Check that required columns exist
if all(col in arts_df.columns for col in ['Gender', 'Did you ever attend a Coaching center?']):
    # Prepare the grouped bar chart using Plotly Express
    fig_grouped = px.histogram(
        arts_df,
        x='Gender',
        color='Did you ever attend a Coaching center?',
        barmode='group',
        color_discrete_sequence=px.colors.sequential.Viridis,
        title='Coaching Center Attendance by Gender (Arts Faculty)'
    )

    # Decorate and format
    fig_grouped.update_layout(
        xaxis_title='Gender',
        yaxis_title='Number of Students',
        title_x=0.5,
        template='plotly_white',
        legend_title_text='Attended Coaching Center?'
    )

    # Add emoji to legend labels for fun clarity
    fig_grouped.for_each_trace(
        lambda t: t.update(
            name='✅ Yes' if 'Yes' in t.name else '❌ No',
            legendgroup=t.name,
        )
    )

    st.plotly_chart(fig_grouped, use_container_width=True)
else:
    st.warning("⚠️ Columns 'Gender' or 'Did you ever attend a Coaching center?' not found in your dataset.")
