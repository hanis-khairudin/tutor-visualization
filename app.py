import streamlit as st

st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization", divider="gray")

data = {'Gender': ['Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female']}
arts_df = pd.DataFrame(data)
# ---------------------------------------------------

st.set_page_config(
    page_title="Gender Distribution Visualization"
)

st.title("Gender Distribution in Arts Faculty")

# Calculate the gender counts
gender_counts = arts_df['Gender'].value_counts()

# Create the matplotlib figure
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the bar chart on the axis 'ax'
ax.bar(gender_counts.index, gender_counts.values, color=['skyblue', 'lightcoral'])

# Set titles and labels for the axis 'ax'
ax.set_title('Distribution of Gender in Arts Faculty')
ax.set_xlabel('Gender')
ax.set_ylabel('Count')

# Display the matplotlib figure in Streamlit
st.pyplot(fig)
