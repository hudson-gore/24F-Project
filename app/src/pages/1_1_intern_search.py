import streamlit as st
import requests
import pandas as pd

# Streamlit app title
st.title("Student Internships by Position and Industry")

# Input fields for position and industry
position = st.text_input("Enter Job Position:", placeholder="e.g., Software Engineer")
industry = st.text_input("Enter Industry:", placeholder="e.g., Tech")

# Submit button
if st.button("Search"):
    if position and industry:
        try:
            # Construct API URL
            api_url = f"http://api:4000/con/contacts/students/pos/ind/{position}/{industry}"
            # Make the GET request
            response = requests.get(api_url)
            
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
