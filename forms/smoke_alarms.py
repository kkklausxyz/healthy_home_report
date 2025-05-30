import streamlit as st

def smoke_alarms_form():
    st.header("Smoke Alarms")
    status = st.selectbox("Alarms", ["PASS", "FAIL"], key="alarms_status")
    photos = st.file_uploader(
        "Upload photos for Alarms",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="alarms_photos"
    )
    return {"status": status, "photos": photos}
