import streamlit as st
import requests
import pandas as pd

# Streamlit app title
st.title("Employee Contacts by Position and Industry")

# Create two columns for position and industry input fields
col1, col2 = st.columns(2)

with col1:
    position = st.text_input("Job Position", placeholder="e.g., Hiring Manager")

with col2:
    industry = st.text_input("Industry", placeholder="e.g., Retail")

# Submit button
if st.button("Search"):
    if position and industry:
        try:
            # Make the GET request
            response = requests.get(f"http://api:4000/con/contacts/employees/pos/ind/{position}/{industry}")
            
            if response.status_code == 200:
                # Convert JSON response to DataFrame
                data = response.json()
                if data:
                    df = pd.DataFrame(data, columns=["FirstName", "LastName", "Phone", "Email"])
                    # Display results
                    st.write(f"Results for {position} in {industry}:")
                    st.dataframe(df)
                else:
                    st.warning("No results found for the given criteria.")
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in both Position and Industry.")

