import streamlit as st
import requests

# Streamlit Page Title
st.title("Add New Internship Experience")

# Instructions
st.write("Fill in the details below to add a new internship experience.")

# Form for Internship Details
with st.form(key="internship_form"):
    job_title = st.text_input("Job Title", placeholder='Investment Banking')
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    company = st.text_input("Company", placeholder='Goldman Sachs ID = 37')
    position_holder = st.text_input("Student ID (Position Holder)", placeholder="Maya's ID is 49")
    supervisor = st.text_input("Supervisor", placeholder='An employee at GS is 64')
    
    # Submit Button
    submit_button = st.form_submit_button(label="Add Internship")

# Handle Form Submission
if submit_button:
    # Prepare payload for POST request
    payload = {
        "JobTitle": job_title,
        "StartDate": start_date.isoformat(),
        "EndDate": end_date.isoformat(),
        "Company": company,
        "PositionHolder": position_holder,
        "Supervisor": supervisor
    }

    # Make POST request to the API
    try:
        api_url = "http://api:4000/i/internships"  
        response = requests.post(api_url, json=payload)
        response.raise_for_status()  

        # Display success or error message
        if response.status_code == 200:
            st.success("Internship experience successfully added!")
        else:
            st.error(f"Error: {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
