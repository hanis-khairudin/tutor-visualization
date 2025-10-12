import streamlit as st

st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization", divider="gray")

# --- Data Simulation ---
# Since 'arts_df' isn't defined, we create a sample DataFrame for the example.
# **IMPORTANT:** In your real application, replace this section with your actual data loading.
np.random.seed(42) # For reproducible results
data = {'Gender': np.random.choice(['Female', 'Male', 'Other'], size=100, p=[0.6, 0.35, 0.05])}
arts_df = pd.DataFrame(data)
# -----------------------

st.set_page_config(
    page_title="Gender Distribution Visualization"
)

st.title("📊 Faculty Gender Distribution")
st.markdown("---")

# 1. Calculate the gender counts
gender_counts = arts_df['Gender'].value_counts()

# 2. Create the Matplotlib figure and axes object
# This is the standard way to create figures for Streamlit
fig, ax = plt.subplots(figsize=(8, 6))

# 3. Plot the bar chart on the axis 'ax'
ax.bar(gender_counts.index, gender_counts.values, color=['skyblue', 'lightcoral', 'lightgreen'])

# 4. Set titles and labels for the axis 'ax'
ax.set_title('Distribution of Gender in Arts Faculty', fontsize=16)
ax.set_xlabel('Gender', fontsize=14)
ax.set_ylabel('Count', fontsize=14)
ax.tick_params(axis='x', rotation=0) # Ensure labels are horizontal
ax.grid(axis='y', linestyle='--', alpha=0.7) # Add subtle horizontal grid lines

# 5. Display the Matplotlib figure in Streamlit
st.pyplot(fig)

st.write("---")
st.subheader("Raw Data Counts")
st.dataframe(gender_counts) # Display the count data as a table
