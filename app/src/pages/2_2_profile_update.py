import streamlit as st
import requests
import json
import pandas as pd
from pandas import json_normalize

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
        
# Check Profile
st.header("Updated Profile")
update_button = st.button("See Updated Profile")

if update_button:
    try:
        response = requests.get(f"{API_URL}/profile/student/{student_id}")
        response.raise_for_status()  # Catch HTTP errors
        data = response.json()

        if data:
            # Create a DataFrame where keys are columns and values are row data
           # df = pd.DataFrame([data])  # Use [data] to create one row
            df = json_normalize(data)
            st.dataframe(df)  # Display DataFrame
        else:
            st.write("No data found for the provided Student ID.")

    except requests.exceptions.RequestException as e:
        st.error(f"API connection error: {e}")
    except ValueError:
        st.error("Invalid data format received from API.")
