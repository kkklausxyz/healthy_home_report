import streamlit as st

def insulation_form():
    st.header("Insulation")
    ceiling_status = st.selectbox("Ceiling Insulation", ["PASS", "FAIL"], key="ceiling_ins")
    ceiling_photos = st.file_uploader(
        "Upload photos for Ceiling Insulation",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="ceiling_ins_photos"
    )
    underfloor_status = st.selectbox("Underfloor Insulation", ["PASS", "FAIL"], key="underfloor_ins")
    underfloor_photos = st.file_uploader(
        "Upload photos for Underfloor Insulation",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="underfloor_ins_photos"
    )
    return {
        "ceiling": {"status": ceiling_status, "photos": ceiling_photos},
        "underfloor": {"status": underfloor_status, "photos": underfloor_photos}
    }
