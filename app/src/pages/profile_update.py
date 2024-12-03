import streamlit as st
from modules.nav import SideBarLinks

st.title("Profile")
student_Major = st.session_state.get('Major', '')
student_grad = st.session_state.get('Expected_Grad', '')
st.caption(f"{student_Major} - {student_grad}")
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
    skills = st.tags_input(
        "Add your skills", ["Java", "SQL", "Data Structures", "Algorithms", "HTTP/HTTPS", "Cloud Computing"]
    )

with st.expander("Projects"):
    st.text_area("Showcase your best project and link your GitHub links")

with st.expander("Roles Interested In"):
    roles = st.multiselect(
        "Select Roles you are interested in", ["Software Engineer", "Data Analyst", "Cloud Engineer", "QRole"], default=["QRole"]
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
