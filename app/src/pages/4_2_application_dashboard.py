import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch all tags and their counts
def get_tags():
    try:
        response = requests.get("http://api:4000/p/profile/get/all/tags")
        if response.status_code == 200:
            tags = response.json()
            # Create a dictionary with tag counts
            tag_counts = {}
            for tag in tags:
                tag_name = tag['TagName']
                if tag_name in tag_counts:
                    tag_counts[tag_name] += 1
                else:
                    tag_counts[tag_name] = 1
            return tag_counts
        else:
            st.error("Error fetching tags.")
            return {}
    except Exception as e:
        st.error(f"An error occurred while fetching tags: {e}")
        return {}

# Function to fetch students with a specific tag
def get_students_with_tag(tag):
    try:
        response = requests.get(f"http://api:4000/p/profile/students/tags/{tag}")
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error fetching students with tag '{tag}'.")
            return []
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []

# Streamlit page title
st.title("Student Tags Analysis")

# Fetch tags and display bar chart
st.subheader("Tag Counts")
tag_counts = get_tags()

if tag_counts:
    # Display bar chart
    fig, ax = plt.subplots()
    ax.bar(tag_counts.keys(), tag_counts.values(), color='skyblue')
    ax.set_title("Tag Counts")
    ax.set_xlabel("Tags")
    ax.set_ylabel("Count")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Dropdown to select a tag
    selected_tag = st.selectbox("Select a tag to view students:", options=list(tag_counts.keys()))

    # Fetch and display students associated with the selected tag
    if st.button("Show Students with Selected Tag"):
        students = get_students_with_tag(selected_tag)
        if students:
            # Convert to DataFrame for better display
            df = pd.DataFrame(students, columns=["FirstName", "LastName", "Major", "Year", "Email", "Phone"])
            st.subheader(f"Students with tag '{selected_tag}'")
            st.dataframe(df)
        else:
            st.warning(f"No students found with tag '{selected_tag}'.")
else:
    st.warning("No tags found in the database.")
