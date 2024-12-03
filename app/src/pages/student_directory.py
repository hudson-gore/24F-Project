import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

# Page configuration
st.set_page_config(layout="centered")
SideBarLinks(show_home=True)

# Title and subheader for the page
st.title("Student Directory")
st.subheader("Use this page to search and view profiles of students seeking co-op and full-time opportunities.")

# Backend API endpoint
API_URL = "http://127.0.0.1:4000/students"  # Replace with the actual backend URL if running in Docker, e.g., "http://api:4000/students"

# Fetch the list of students from the backend
try:
    response = requests.get(API_URL)
    response.raise_for_status()  # Raise an error if the request fails
    students_data = response.json()["students"]  # Extract the list of students
except requests.RequestException as e:
    st.error("Error fetching student data. Please try again later.")
    st.stop()

# Convert students data to a DataFrame for display
students_df = pd.DataFrame(students_data)

# Search bar for filtering student names
search_query = st.text_input("Search for a student (by name):")

# Filter the DataFrame based on the search query
if search_query:
    filtered_students = students_df[
        (students_df["first_name"].str.contains(search_query, case=False, na=False)) |
        (students_df["last_name"].str.contains(search_query, case=False, na=False))
    ]
else:
    filtered_students = students_df

# Display the filtered students in a table
st.write("### Student List")
if not filtered_students.empty:
    st.dataframe(filtered_students)
else:
    st.write("No students found matching your search.")
