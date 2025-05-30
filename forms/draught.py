import streamlit as st

def draught_form():
    st.header("Draught Stopping")
    status = st.selectbox("Draught Stopping Status", ["PASS", "FAIL"], key="draught_status")
    photos = st.file_uploader(
        "Upload photos for Draught Stopping",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="draught_photos"
    )
    return {"status": status, "photos": photos}
