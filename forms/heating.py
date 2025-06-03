import streamlit as st

def heating_form():
    st.header("Heating")

    # HHS compliancy
    hhs_status = st.selectbox(
        "HHS property compliancy status:",
        ["Property is compliant", "Property is NOT compliant"],
        key="heating_hhs_status"
    )

    # Basic Info
    location = st.text_input("Location of heat pump:", key="heat_pump_location")
    required_capacity = st.text_input("Required heating capacity (e.g. 13.9kw):", key="required_heating_capacity")
    pre_existing_heater = st.selectbox("Pre-existing fixed heater:", ["Yes", "No"], key="pre_existing_heater")
    exempt_from_hhs = st.selectbox("Property is exempt from HHS:", ["No", "Yes"], key="exempt_from_hhs")

    st.markdown("**PRE-EXISTING FIXED HEATER**")
    heater_compliant = st.text_input("Heater Compliant (e.g. Yes (6kw+8kw heat pump)):", key="heater_compliant")
    operational = st.selectbox("Operational:", ["Yes", "No"], key="heater_operational")

    # Photos
    photos = st.file_uploader(
        "Upload photos for Heating",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="heating_photos"
    )

    return {
        "hhs_status": hhs_status,
        "location": location,
        "required_capacity": required_capacity,
        "pre_existing_heater": pre_existing_heater,
        "exempt_from_hhs": exempt_from_hhs,
        "heater_compliant": heater_compliant,
        "operational": operational,
        "photos": photos
    }
