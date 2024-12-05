import streamlit as st
import requests

# Streamlit page setup
st.set_page_config(page_title="Add New Employee Contact", layout="centered")
st.title("Add New Employee Contact")

# Function to add an employee contact
def add_employee_contact(first_name, last_name, job_title, profile_details, phone, email, degree, contact_manager, profile_manager, company):
    try:
        # Prepare the employee data
        employee_data = {
            "FirstName": first_name,
            "LastName": last_name,
            "JobTitle": job_title,
            "ProfileDetails": profile_details,
            "Phone": phone,
            "Email": email,
            "Degree": degree,
            "ContactManager": contact_manager,
            "ProfileManager": profile_manager,
            "Company": company
        }
        
        # Send the POST request to add employee
        response = requests.post("http://api:4000/con/contact/employee", json=employee_data)
        
        # Check if the request was successful
        if response.status_code == 200:
            st.success("Employee contact added successfully!")
        else:
            st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Input fields for employee contact details
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
job_title = st.text_input("Job Title")
profile_details = st.text_area("Profile Details")
phone = st.text_input("Phone")
email = st.text_input("Email")
degree = st.text_input("Degree")
contact_manager = st.text_input("Contact Manager ID")
profile_manager = st.text_input("Profile Manager ID")
company = st.text_input("Company ID")

# Button to submit the employee contact
if st.button("Add Employee Contact"):
    if first_name and last_name and job_title and profile_details and phone and email and degree and contact_manager and profile_manager and company:
        add_employee_contact(first_name, last_name, job_title, profile_details, phone, email, degree, contact_manager, profile_manager, company)
    else:
        st.warning("Please fill in all fields before submitting.")


