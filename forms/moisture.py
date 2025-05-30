import streamlit as st

def moisture_form():
    st.header("Moisture Ingress and Drainage")

    # ===== GROUND VAPOUR BARRIER =====
    st.subheader("Ground Vapour Barrier")

    ground_hhs_status = st.selectbox(
        "HHS property compliancy status (Ground Vapour Barrier):",
        ["Property is compliant", "Property is NOT compliant"],
        key="moisture_ground_hhs"
    )

    ground_applicable = st.selectbox(
        "Is Ground Vapour Barrier applicable?",
        ["Yes", "No (not applicable/exempt)"],
        key="moisture_ground_applicable"
    )

    ground_data = {}
    if ground_applicable == "Yes":
        ground_data["description"] = st.text_area(
            "Description (e.g. Existing underfloor Ground Moisture Barrier was located at the property):",
            key="moisture_ground_desc"
        )
        ground_data["exempt"] = st.selectbox(
            "Property is exempt from HHS (Ground Vapour Barrier):",
            ["No", "Yes"],
            key="moisture_ground_exempt"
        )
    else:
        ground_data["description"] = st.text_area(
            "Reason not applicable/exempt (e.g. Concrete slab floor, Underfloor vapour barrier is not applicable):",
            key="moisture_ground_na_desc"
        )
        ground_data["exempt"] = st.selectbox(
            "Property is exempt from HHS (Ground Vapour Barrier):",
            ["No", "Yes"],
            key="moisture_ground_exempt_na"
        )

    ground_photos = st.file_uploader(
        "Upload photos for Ground Vapour Barrier",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="moisture_ground_photos"
    )

    # ===== DRAINAGE =====
    st.subheader("Drainage")

    drainage_hhs_status = st.selectbox(
        "HHS property compliancy status (Drainage):",
        ["Property is compliant", "Property is NOT compliant"],
        key="moisture_drainage_hhs"
    )

    # 具体检查项
    gutters_fall = st.selectbox("Gutters present with correct fall:", ["Yes", "No"], key="gutters_fall")
    gutters_intact = st.selectbox("Gutters intact with no damage:", ["Yes", "No"], key="gutters_intact")
    gutters_clear = st.selectbox("Gutters/downpipes clear from obstructions:", ["Yes", "No"], key="gutters_clear")
    downpipes_intact = st.selectbox("Downpipes connected and intact:", ["Yes", "No"], key="downpipes_intact")
    downpipes_outfall = st.selectbox("Downpipes connected to outfall:", ["Yes", "No"], key="downpipes_outfall")

    drainage_photos = st.file_uploader(
        "Upload photos for Drainage",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="moisture_drainage_photos"
    )

    return {
        "ground_vapour_barrier": {
            "hhs_status": ground_hhs_status,
            "applicable": ground_applicable,
            **ground_data,
            "photos": ground_photos
        },
        "drainage": {
            "hhs_status": drainage_hhs_status,
            "gutters_fall": gutters_fall,
            "gutters_intact": gutters_intact,
            "gutters_clear": gutters_clear,
            "downpipes_intact": downpipes_intact,
            "downpipes_outfall": downpipes_outfall,
            "photos": drainage_photos
        }
    }
