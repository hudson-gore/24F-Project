import streamlit as st
import requests

# Function to send a POST request to add an employee profile
def add_employee_to_db(profile_data):
    try:
        response = requests.post('http://api:4000/p/profile/employee', json=profile_data)
        if response.status_code == 200:
            st.success("Employee profile successfully added!")
            return True
        else:
            st.error(f"Error: {response.text}")
            return False
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False

# Function to get an employee profile from the database
def get_employee_profile(employee_id):
    try:
        response = requests.get(f'http://api:4000/p/profile/employee/{employee_id}')
        if response.status_code == 200:
            return response.json() 
        else:
            st.error(f"Error: {response.text}")
            return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Function to get all employee profiles for a specific company
def get_company_profiles(company):
    try:
        response = requests.get(f'http://api:4000/p/profile/employees/company/{company}')
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error: {response.text}")
            return []
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []

# Streamlit page title
st.title("Add Employee Profile")

# Employee profile input fields
st.subheader("Employee Profile")
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
job_title = st.text_input("Job Title")
profile_details = st.text_area("Profile Details")
phone = st.text_input("Phone")
email = st.text_input("Email")
contact_manager = st.text_input("Contact Manager")
profile_manager = st.text_input("Profile Manager")
company = st.text_input("Company")
employee_id = st.text_input("EmployeeID")

# Add employee profile submission
if st.button("Submit Employee Profile"):
    if first_name and last_name and job_title and profile_details and phone and email and contact_manager and profile_manager and company:
        employee_data = {
            "FirstName": first_name,
            "LastName": last_name,
            "JobTitle": job_title,
            "ProfileDetails": profile_details,
            "Phone": phone,
            "Email": email,
            "ContactManager": contact_manager,
            "ProfileManager": profile_manager,
            "Company": company,
            "EmployeeID": employee_id
        }
        if add_employee_to_db(employee_data):
            # Fetch and display the added employee profile
            profile = get_employee_profile(employee_id)
        else:
            st.warning("Profile could not be added.")
    else:
        st.warning("Please fill in all the fields.")

# Button to view all employee profiles for a specific company
if company and st.button(f"See Company Profiles"):
    profiles = get_company_profiles(company)
    if profiles:
        st.dataframe(profiles)
    else:
        st.warning(f"No profiles found for {company}.")
