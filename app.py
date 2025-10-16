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
        gender_counts.columns = ['Gender','Count']

        fig = px.bar(
            gender_counts,
            x='Gender',
            y='Count',
            color='Gender',
            color_discrete_sequence=['skyblue', 'lightcoral'],
            title='Distribution of Gender in Arts Faculty',
            hover_data={'Gender': False}
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


# --- 7. TOP BEST ASPECTS OF THE PROGRAM ---
st.subheader("🏅 Top Most Appreciated Aspects of the Program")

# Check if both columns exist
if all(col in arts_df.columns for col in [
    'Q7. In your opinion,the best aspect of the program is',
    'Q8. In your opinion,the next best aspect of the program is'
]):
    # Combine both columns and clean
    best_aspects = pd.concat([
        arts_df['Q7. In your opinion,the best aspect of the program is'],
        arts_df['Q8. In your opinion,the next best aspect of the program is']
    ]).dropna()

    # Count and sort
    aspect_counts = best_aspects.value_counts().reset_index()
    aspect_counts.columns = ['Aspect', 'Count']


    # Create interactive horizontal bar chart
    fig_aspects = px.bar(
        top_aspects,
        x='Count',
        y='Aspect',
        orientation='h',
        color='Count',
        color_continuous_scale='Viridis',
        title=f"Top {top_n} Most Frequently Mentioned Best Aspects of the Program"
    )

    # Decorate layout
    fig_aspects.update_layout(
        xaxis_title='Number of Mentions',
        yaxis_title='Aspect',
        title_x=0.5,
        template='plotly_white',
        coloraxis_showscale=False
    )

    # Display chart
    st.plotly_chart(fig_aspects, use_container_width=True)
else:
    st.warning("⚠️ One or both of the aspect columns (Q7 or Q8) are missing in your dataset.")


# --- 8. DISTRIBUTION OF ARTS PROGRAMS ---
st.subheader("🎭 Distribution of Arts Programs")

# Check if the column exists
if 'Arts Program' in arts_df.columns:
    # Count each Arts Program
    program_counts = arts_df['Arts Program'].value_counts().reset_index()
    program_counts.columns = ['Arts Program', 'Count']

    # Create interactive horizontal bar chart
    fig_programs = px.bar(
        program_counts,
        x='Count',
        y='Arts Program',
        color='Arts Program',
        orientation='h',
        color_discrete_sequence=px.colors.sequential.Viridis,
        title='Distribution of Arts Programs'
    )

    # Customize layout
    fig_programs.update_layout(
        xaxis_title='Number of Students',
        yaxis_title='Arts Program',
        title_x=0.5,
        template='plotly_white',
        showlegend=False
    )

    # Display chart
    st.plotly_chart(fig_programs, use_container_width=True)
else:
    st.warning("⚠️ Column 'Arts Program' not found in your dataset.")


# --- 9. STUDENT PERCEPTION ON EDUCATION QUALITY IMPROVEMENT ---
st.subheader("📈 Student Perception on Education Quality Improvement")

# Check if the column exists
if 'Do you feel that the quality of education improved at EU over the last year?' in arts_df.columns:
    # Count the occurrences of each response
    education_quality_counts = arts_df['Do you feel that the quality of education improved at EU over the last year?'] \
        .value_counts().reset_index()
    education_quality_counts.columns = ['Education Quality Improved', 'Count']

    # Create interactive bar chart
    fig_edu_quality = px.bar(
        education_quality_counts,
        x='Education Quality Improved',
        y='Count',
        color='Education Quality Improved',
        color_discrete_sequence=px.colors.sequential.Viridis,
        title='Student Perception on Education Quality Improvement (Arts Faculty)'
    )

    # Customize chart layout
    fig_edu_quality.update_layout(
        xaxis_title='Did Education Quality Improve?',
        yaxis_title='Number of Students',
        title_x=0.5,
        template='plotly_white',
        showlegend=False
    )

    # Display in Streamlit
    st.plotly_chart(fig_edu_quality, use_container_width=True)
else:
    st.warning("⚠️ Column 'Do you feel that the quality of education improved at EU over the last year?' not found in your dataset.")


# --- 10. RELATIONSHIP BETWEEN S.S.C AND H.S.C GPA ---
st.subheader("📊 Relationship Between S.S.C (GPA) and H.S.C (GPA)")

# Check if both columns exist
if all(col in arts_df.columns for col in ['S.S.C (GPA)', 'H.S.C (GPA)']):
    # Create interactive scatter plot
    fig_scatter = px.scatter(
        arts_df,
        x='S.S.C (GPA)',
        y='H.S.C (GPA)',
        color_discrete_sequence=px.colors.sequential.Viridis,
        title='S.S.C (GPA) vs H.S.C (GPA) in Arts Faculty',
        opacity=0.7,
        trendline='ols'  # optional: adds regression line
    )

    # Customize layout
    fig_scatter.update_layout(
        xaxis_title='S.S.C (GPA)',
        yaxis_title='H.S.C (GPA)',
        title_x=0.5,
        template='plotly_white'
    )

    # Display chart
    st.plotly_chart(fig_scatter, use_container_width=True)
else:
    st.warning("⚠️ Columns 'S.S.C (GPA)' or 'H.S.C (GPA)' not found in your dataset.")
