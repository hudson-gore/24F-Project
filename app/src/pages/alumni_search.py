import streamlit as st

# Set page config for Streamlit
st.set_page_config(layout="wide")

# Title of the page
st.title("Search for Alumni")

# Add description or instructions
st.write("""
    Here you can search for alumni who work at major companies or in specific fields like Big Tech or Accounting/Finance.
""")

# Example input to search alumni
company_name = st.text_input("Enter a company name (e.g., Google, Amazon, Deloitte):")

if company_name:
    st.write(f"Searching for alumni who work at {company_name}...")
    # Placeholder for actual search logic
    st.write("This feature is under construction.")
