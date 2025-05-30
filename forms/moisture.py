import streamlit as st

def moisture_form():
    st.header("Moisture Ingress and Drainage")
    ground_status = st.selectbox("Ground Vapour Barrier", ["PASS", "FAIL"], key="ground_vapour")
    ground_photos = st.file_uploader(
        "Upload photos for Ground Vapour Barrier",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="ground_vapour_photos"
    )
    gutters_status = st.selectbox("Gutters, Downpipes & Drains", ["PASS", "FAIL"], key="gutters")
    gutters_photos = st.file_uploader(
        "Upload photos for Gutters, Downpipes & Drains",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="gutters_photos"
    )
    return {
        "ground": {"status": ground_status, "photos": ground_photos},
        "gutters": {"status": gutters_status, "photos": gutters_photos}
    }
