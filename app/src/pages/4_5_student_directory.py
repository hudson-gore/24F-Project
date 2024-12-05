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

# Backend API endpoints
BASE_API_URL = "http://api:4000/s"
ALL_STUDENTS_ENDPOINT = f"{BASE_API_URL}/students"
SEARCH_STUDENTS_ENDPOINT = f"{BASE_API_URL}/students/{{}}"  # Placeholder for student search by first name

# Function to fetch all students
def fetch_all_students():
    try:
        response = requests.get(ALL_STUDENTS_ENDPOINT)
        response.raise_for_status()  # Raise an error if the request fails
        return pd.DataFrame(response.json())  # Convert to DataFrame
    except requests.RequestException as e:
        st.error(f"Error fetching all students: {e}")
        return pd.DataFrame()  # Return an empty DataFrame

# Function to search students by first name
def search_students_by_name(first_name):
    try:
        response = requests.get(SEARCH_STUDENTS_ENDPOINT.format(first_name))
        response.raise_for_status()  # Raise an error if the request fails
        return pd.DataFrame(response.json())  # Convert to DataFrame
    except requests.RequestException as e:
        st.error(f"Error fetching student data for '{first_name}': {e}")
        return pd.DataFrame()  # Return an empty DataFrame

# Fetch all students initially
students_df = fetch_all_students()

# Search bar for filtering student names
st.write("### Search for a Student")
search_query = st.text_input("Enter the first name of the student you are looking for:")

if search_query:
    # Search by name and display results
    st.write(f"### Search Results for '{search_query}'")
    search_results = search_students_by_name(search_query)
    if not search_results.empty:
        st.dataframe(search_results)
    else:
        st.write("No students found with that name.")
else:
    st.write("### All Students")
    if not students_df.empty:
        # Display all students in a scrollable window
        st.dataframe(students_df)
    else:
        st.write("No students data available.")