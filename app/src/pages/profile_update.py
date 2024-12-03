import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")
SideBarLinks(show_home=True)

student_major = st.session_state.get('Major', '')
student_Grad = st.session_state.get('Expected_Grad', '')

st.title("Jordan Thompson")
st.caption(f"Undergraduate: Computer Science - May 2026")
st.caption("Northeastern University")

# Resume and Transcript Uploads
col1, col2 = st.columns(2)
with col1:
    resume_uploaded = st.file_uploader("Resume Attach")
with col2:
    transcript_uploaded = st.file_uploader("Unofficial Transcript")

with st.expander("Personal Statement"):
    personal_statement = st.text_area("Add a compelling description showcasing yourself")

with st.expander("Skills"):
    skills = st.text_input(
        "Add your skills (comma-separated)", "Java, SQL, Data Structures, Algorithms, HTTP/HTTPS, Cloud Computing"
    )
    skills_list = [skill.strip() for skill in skills.split(',') if skill.strip()]

with st.expander("Projects"):
    st.text_area("Showcase your best project and link your GitHub links")

with st.expander("Roles Interested In"):
    roles = st.multiselect(
        "Select Roles you are interested in", ["Software Engineer", "Data Analyst", "Cloud Engineer", "QRole", "IT"], default=["Software Engineer"]
    )
    st.write(f"Selected {len(roles)}/5")

st.markdown(
    """
    <style>
    .stFileUploader > label {font-weight: bold;}
    .st-expander > .streamlit-expanderHeader {font-size: 16px; font-weight: bold;}
    </style>
    """,
    unsafe_allow_html=True,
)

