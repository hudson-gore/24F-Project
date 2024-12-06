import streamlit as st
import requests
import pandas as pd

# Streamlit app title
st.title("Find an Employee's Profile and Add a Tag")

# Section: View Profile
st.header("Find Profile")
user_type = 'employee'
user_id = st.text_input(f"Enter {user_type.capitalize()} ID:", placeholder="Try 7")

if st.button("Search"):
    if user_type and user_id:
        try:
            # Construct API URL for profile lookup
            api_url = f"http://api:4000/p/profile/{user_type}/{user_id}"
            # Make the GET request
            response = requests.get(api_url)
            
            if response.status_code == 200:
                profile_data = response.json()
                if profile_data:
                    # Convert profile data to DataFrame and display
                    df = pd.DataFrame(profile_data)
                    st.write(f"{user_type.capitalize()} Profile:")
                    st.dataframe(df)
                else:
                    st.warning(f"No profile found for {user_type} with ID {user_id}.")
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in the User Type and ID.")

# Section: Add Tag
st.header("Add Tag to Employee Profile")
tag_name = st.text_input("Enter Tag Name:", placeholder="e.g., Mentor")
tag_owner = st.text_input("Enter Tag Owner ID:", placeholder="ID of the user adding the tag (Jordan's is 50)")
tagged_user = st.text_input("Enter Tagged User ID:", placeholder="ID of the employee to tag")

if st.button("Add Tag"):
    if tag_name and tag_owner and tagged_user:
        try:
            # Construct API URL for adding a tag
            api_url = "http://api:4000/p/profile/employee/tag"
            # Prepare JSON payload
            payload = {
                "TagName": tag_name,
                "TagOwner": tag_owner,
                "TaggedUser": tagged_user
            }
            # Make the POST request
            response = requests.post(api_url, json=payload)
            
            if response.status_code == 200:
                st.success("Successfully added tag!")
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in all fields to add a tag.")
