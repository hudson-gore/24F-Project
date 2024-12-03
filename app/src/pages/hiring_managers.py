import streamlit as st

# Set page config for Streamlit
st.set_page_config(layout="wide")

# Title of the page
st.title("Search for Hiring Managers")

# Add description or instructions
st.write("""
    Here you can search for hiring managers in the Accounting and Finance fields. 
    This will help you understand what skills are in demand and which companies are hiring.
""")

# Example input to search hiring managers
company_name = st.text_input("Enter a company name (e.g., Deloitte, EY):")

if company_name:
    st.write(f"Searching for hiring managers at {company_name}...")
    # Placeholder for actual search logic
    st.write("This feature is under construction.")
