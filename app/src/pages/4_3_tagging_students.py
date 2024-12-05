import streamlit as st
import requests

# Streamlit page setup
st.set_page_config(page_title="Add Tag to Student Profiles", layout="centered")
st.title("Add Tag to Student Profiles")

# Function to add a tag to a student profile
def add_tag(tag_name, tag_owner, tagged_user):
    try:
        data = {
            "TagName": tag_name,
            "TagOwner": tag_owner,
            "TaggedUser": tagged_user
        }
        response = requests.post("http://api:4000/p/profile/student/tag", json=data)
        if response.status_code == 200:
            st.success(f"Tag '{tag_name}' successfully added to student ID {tagged_user}.")
        else:
            st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Input fields for adding a tag
st.subheader("Add a New Tag")
tag_name = st.text_input("Tag Name", placeholder="Enter a tag name, e.g., Hard Worker")
tag_owner = st.text_input("Tag Owner", placeholder="Enter an EmployeeID number")
tagged_user = st.text_input("Tagged User (Student ID)", placeholder="Enter the StudentID")

# Button to submit the tag
if st.button("Add Tag"):
    if tag_name and tag_owner and tagged_user:
        add_tag(tag_name, tag_owner, tagged_user)
    else:
        st.warning("Please fill in all fields before submitting.")

