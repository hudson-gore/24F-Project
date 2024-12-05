import streamlit as st
import requests
import pandas as pd

# Function to get all available tags from the database (you can modify this function as needed)
def get_tags():
    try:
        response = requests.get("http://api:4000/p/profile/students/tags") 
        if response.status_code == 200:
            # Extract only the tag names from the response
            tags = [tag['TagName'] for tag in response.json()]  
            return tags
        else:
            st.error("Error fetching tags from the database.")
            return []
    except Exception as e:
        st.error(f"An error occurred while fetching tags: {e}")
        return []

# Function to get all students with a specific tag
def get_students_by_tag(tag):
    try:
        response = requests.get(f"http://api:4000/con/contacts/students/tags/{tag}")
        if response.status_code == 200:
            return response.json()  
        else:
            st.error(f"Error fetching students with tag '{tag}'.")
            return []
    except Exception as e:
        st.error(f"An error occurred while fetching students: {e}")
        return []

# Streamlit app title
st.title("Students by Tag")

# Get tags from the database
tags = get_tags()

# Display the dropdown menu for selecting a tag
if tags:
    tag = st.selectbox("Select Tag:", tags) 
else:
    st.warning("No tags found in the database.")

# Submit button
if st.button("Search") and tag:
    try:
        # Get students with the selected tag
        students = get_students_by_tag(tag)
        
        if students:
            # Convert JSON response to DataFrame
            df = pd.DataFrame(students, columns=["FirstName", "LastName", "Year", "Major", "Email", "Phone"])
            # Display results
            st.write(f"Students with the tag '{tag}':")
            st.dataframe(df)
        else:
            st.warning(f"No students found with the tag '{tag}'.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    if not tag:
        st.warning("Please select a Tag.")
