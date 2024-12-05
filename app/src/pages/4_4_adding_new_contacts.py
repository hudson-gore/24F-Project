import streamlit as st
import requests

# Streamlit page setup
st.set_page_config(page_title="Add New Contact", layout="centered")
st.title("Add New Contact")

# Function to add a contact
def add_contact(contact_type, first_name, last_name, email, phone):
    try:
        # Prepare the contact data
        contact_data = {
            "FirstName": first_name,
            "LastName": last_name,
            "Email": email,
            "Phone": phone
        }
        
        # Send the POST request
        response = requests.post(f"http://api:4000/con/contact/{contact_type}", json=contact_data)
        
        # Check if the request was successful
        if response.status_code == 200:
            st.success(f"{contact_type.capitalize()} contact added successfully!")
        else:
            st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Input fields for contact details
contact_type = st.radio("Select Contact Type", ["student", "employee"])
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
email = st.text_input("Email")
phone = st.text_input("Phone")

# Button to submit the contact
if st.button("Add Contact"):
    if first_name and last_name and email and phone:
        add_contact(contact_type, first_name, last_name, email, phone)
    else:
        st.warning("Please fill in all fields before submitting.")

