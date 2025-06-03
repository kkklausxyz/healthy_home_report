import streamlit as st

def basic_info_form():
    st.header("Basic Information")
    property_address = st.text_input("Property address:")
    date_of_assessment = st.date_input("Date of assessment:")
    assessor_name = st.text_input("Assessor name:")
    email = st.text_input("Email:")
    phone = st.text_input("Phone:")
    photo = st.file_uploader("Upload property photo", type=["jpg", "jpeg", "png"])

    return {
        "property_address": property_address,
        "date_of_assessment": date_of_assessment,
        "assessor_name": assessor_name,
        "email": email,
        "phone": phone,
        "photo": photo,
    }
