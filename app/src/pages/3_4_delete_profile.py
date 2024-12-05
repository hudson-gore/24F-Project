import streamlit as st
import requests
import pandas as pd

# Function to fetch all contacts managed by Alex at Wayfair
def get_contacts():
    try:
        # API call to fetch contacts (adjust the endpoint if necessary)
        response = requests.get("http://api:4000/con/contacts/employees/company/31")
        if response.status_code == 200:
            contacts = response.json()
            # Process the data to display meaningful names in the dropdown
            return [{"name": f"{c['FirstName']} {c['LastName']}", "id": c['EmployeeID']} for c in contacts]
        else:
            st.error("Error fetching contacts from Wayfair.")
            return []
    except Exception as e:
        st.error(f"An error occurred while fetching contacts: {e}")
        return []

# Function to delete a contact
def delete_contact(contact_id):
    try:
        response = requests.delete(f"http://api:4000/con/contact/employee/{contact_id}")
        if response.status_code == 200:
            st.success("Contact deleted successfully!")
        else:
            st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Function to display contacts in a dataframe
def display_contacts():
    contacts = get_contacts()
    if contacts:
        df = pd.DataFrame(contacts)
        df = df.rename(columns={"name": "Name", "id": "EmployeeID"})  # Rename columns for better readability
        st.dataframe(df)
    else:
        st.warning("No contacts found to display.")

# Streamlit page title
st.title("Manage Contacts at Wayfair")

# Fetch and display contacts in a dropdown
contacts = get_contacts()

if contacts:
    # Dropdown to select a contact
    contact_options = {f"{contact['name']}": contact for contact in contacts}
    selected_contact = st.selectbox("Select a contact to delete:", options=list(contact_options.keys()))

    if selected_contact:
        contact_to_delete = contact_options[selected_contact]

        if st.button("Delete Contact"):
            delete_contact(contact_to_delete["id"])
else:
    st.warning("No contacts found for Alex at Wayfair.")

# Add a button to show an updated list of contacts
if st.button("Show Updated Contacts"):
    st.subheader("Updated Contacts List:")
    display_contacts()
