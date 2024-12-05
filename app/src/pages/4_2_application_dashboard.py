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
st.title("Student Dashboard")

# Fetch tags and display bar chart
st.subheader("Tag Counts")
tag_counts = get_tags()

if tag_counts:
    # Display bar chart with horizontal bars for better readability
    fig, ax = plt.subplots(figsize=(10, 6))  # Set a specific figure size
    ax.barh(list(tag_counts.keys()), list(tag_counts.values()), color='skyblue')
    ax.set_title("Tag Counts")
    ax.set_xlabel("Count")
    ax.set_ylabel("Tags")

    # Adjust layout to make room for labels
    plt.tight_layout()
    st.pyplot(fig)

    # Automatically fetch and display students for all tags
    st.subheader("Students who have applied:")
    students = get_students_with_tag('Applied')
    if students:
        # Convert to DataFrame for better display
        df = pd.DataFrame(students, columns=["FirstName", "LastName", "Major", "Year", "Email", "Phone"])
        st.dataframe(df)
    else:
        st.warning("No students found with the 'Applied' tag.")
else:
    st.warning("No tags found in the database.")
