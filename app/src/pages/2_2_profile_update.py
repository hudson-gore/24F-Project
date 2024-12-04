import streamlit as st
import requests
import json

API_URL = "http://api:4000/p"  

# Function to update a student or employee profile
def update_profile(type, profile_data):
    url = f"{API_URL}/profile/{type}"
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, headers=headers, data=json.dumps(profile_data))
    
    if response.status_code == 200:
        st.success("Profile updated successfully!")
    else:
        st.error(f"Error: {response.text}")

# Function to delete a profile
def delete_profile(id):
    url = f"{API_URL}/profile/{id}"
    response = requests.delete(url)
    
    if response.status_code == 200:
        st.success("Profile deleted successfully!")
    else:
        st.error(f"Error: {response.text}")

# Function to get profiles by tag
def get_profiles_by_tag(tag):
    url = f"{API_URL}/profile/{tag}"
    response = requests.get(url)
    
    if response.status_code == 200:
        profiles = response.json()
        if profiles:
            st.write("Profiles found:")
            for profile in profiles:
                st.write(profile)
        else:
            st.warning(f"No profiles found with tag {tag}")
    else:
        st.error(f"Error: {response.text}")

# Streamlit page content
st.title("Student Profiles")

# Option for selecting the type (student or employee)
profile_type = "student"

# Form for updating a profile
with st.form(key="update_form"):
    st.header(f"Update {profile_type.capitalize()} Profile")
    
    if profile_type == "student":
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        major = st.text_input("Major")
        grad_year = st.text_input("Expected Graduation Year")
        year = st.text_input("Year")
        profile_details = st.text_area("Profile Details")
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        profile_manager = st.text_input("Profile Manager")
        student_id = st.text_input("Student ID")
        
        profile_data = {
            "FirstName": first_name,
            "LastName": last_name,
            "Major": major,
            "ExpectedGrad": grad_year,
            "Year": year,
            "ProfileDetails": profile_details,
            "Phone": phone,
            "Email": email,
            "ProfileManager": profile_manager,
            "StudentID": student_id,
        }
    
    submit_button = st.form_submit_button("Update Profile")
    
    if submit_button:
        if all(profile_data.values()):
            update_profile(profile_type, profile_data)
        else:
            st.error("Please fill in all fields.")
        
# Delete a profile section
st.header("Updated Profile")
update_button = st.button("See Updated Profile")
if update_button:
    data = {} 
    try:
        data = requests.get(f"http://api:4000/p/profile/student/{student_id}")
    except:
        st.write("**Important**: Could not connect to sample api, so using dummy data.")
        data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

    st.dataframe(data)
