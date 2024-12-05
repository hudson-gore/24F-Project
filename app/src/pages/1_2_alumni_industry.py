import streamlit as st
import requests
import pandas as pd

# Streamlit app title
st.title("Contacts by Industry and Tag")

# Input fields for industry and tag
industry = st.text_input("Enter Industry:", placeholder="e.g., Tech")
tag = st.text_input("Enter Tag:", placeholder="e.g., Alumni")

# Submit button
if st.button("Search"):
    if industry and tag:
        try:
            # Construct API URL
            api_url = f"http://api:4000/con/contacts/industry/tag/{industry}/{tag}"
            # Make the GET request
            response = requests.get(api_url)
            
            if response.status_code == 200:
                # Convert JSON response to DataFrame
                data = response.json()
                if data:
                    df = pd.DataFrame(data, columns=["FirstName", "LastName", "JobTitle", "Phone", "Email"])
                    # Display results
                    st.write(f"Results for contacts in {industry} with tag '{tag}':")
                    st.dataframe(df)
                else:
                    st.warning("No results found for the given criteria.")
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in both Industry and Tag.")
