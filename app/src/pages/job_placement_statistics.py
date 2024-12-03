import streamlit as st

# Page configuration
st.set_page_config(layout="wide")

# Title for the page
st.title("Job Placement Statistics")

# Description
st.write("""
    Use this page to explore job placement statistics for your department.
""")

# Example filters for statistics
department = st.selectbox("Select Department:", ["Computer Science", "Business", "Engineering", "Other"])
year = st.slider("Select Graduation Year:", 2010, 2024, 2024)

# Placeholder for displaying statistics
if department:
    st.write(f"Displaying job placement statistics for {department}, Graduation Year: {year}")
    st.write("This feature is under construction.")