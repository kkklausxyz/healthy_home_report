import streamlit as st

def draught_form():
    st.header("Draught Stopping")

    hhs_status = st.selectbox(
        "HHS property compliancy status:",
        ["Property is compliant", "Property is NOT compliant"],
        key="draught_hhs_status"
    )

    open_fire = st.selectbox("Open fire:", ["Yes", "No"], key="draught_open_fire")
    closed_off = st.selectbox("Closed off:", ["Yes", "No"], key="draught_closed_off")
    fireplace_closed_off = st.text_input("Fireplace closed off:", key="draught_fireplace_closed_off")

    st.markdown("**Location of doors**")
    doors_location = st.text_input("Location of doors:", key="draught_doors_location")
    doors_gaps = st.selectbox("Gaps or holes (doors):", ["Yes", "No"], key="draught_doors_gaps")

    st.markdown("**Location of windows**")
    windows_location = st.text_input("Location of windows:", key="draught_windows_location")
    windows_gaps = st.selectbox("Gaps or holes (windows):", ["Yes", "No"], key="draught_windows_gaps")

    photos = st.file_uploader(
        "Upload photos for Draught Stopping",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="draught_photos"
    )

    return {
        "hhs_status": hhs_status,
        "open_fire": open_fire,
        "closed_off": closed_off,
        "fireplace_closed_off": fireplace_closed_off,
        "doors_location": doors_location,
        "doors_gaps": doors_gaps,
        "windows_location": windows_location,
        "windows_gaps": windows_gaps,
        "photos": photos
    }
