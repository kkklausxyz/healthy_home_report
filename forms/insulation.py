import streamlit as st

def insulation_form():
    st.header("Insulation")

    # HHS property compliancy status (for the whole section)
    hhs_status = st.selectbox(
        "HHS property compliancy status:",
        ["Property is compliant", "Property is NOT compliant"],
        key="insulation_hhs_status"
    )

    st.subheader("CEILING")
    ceiling_applicable = st.selectbox(
        "Is ceiling insulation applicable?",
        ["Yes", "No (exempt/not possible)"],
        key="ceiling_applicable"
    )

    ceiling_data = {}
    if ceiling_applicable == "Yes":
        ceiling_data["existing_depth"] = st.text_input("Existing depth (e.g. 120mm):", key="ceiling_depth")
        ceiling_data["existing_type"] = st.text_input("Existing insulation type (e.g. Glasswool):", key="ceiling_type")
        ceiling_data["existing_r_value"] = st.text_input("Existing r-value (e.g. R3.2):", key="ceiling_r_value")
        ceiling_data["condition"] = st.text_input("Condition of existing insulation:", key="ceiling_condition")
        ceiling_data["compliant"] = st.selectbox("Compliant with HHS:", ["Yes", "No"], key="ceiling_compliant")
        ceiling_data["exempt"] = st.selectbox("Property exemption from HHS:", ["No", "Yes"], key="ceiling_exempt")
        ceiling_data["notes"] = st.text_area("Additional notes (optional):", key="ceiling_notes")
    else:
        ceiling_data["notes"] = st.text_area(
            "Reason why ceiling insulation is not applicable/exempt (e.g. The roof cannot be installed insulation because of the structure):",
            key="ceiling_na_notes"
        )
        ceiling_data["exempt"] = st.selectbox("Property exemption from HHS:", ["No", "Yes"], key="ceiling_exempt_na")

    ceiling_photos = st.file_uploader(
        "Upload photos for Ceiling Insulation",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="ceiling_ins_photos"
    )

    # UNDERFLOOR
    st.subheader("UNDERFLOOR")
    underfloor_applicable = st.selectbox(
        "Is underfloor insulation applicable?",
        ["Yes", "No (exempt/not possible)"],
        key="underfloor_applicable"
    )

    underfloor_data = {}
    if underfloor_applicable == "Yes":
        underfloor_data["existing_type"] = st.text_input("Existing product type (e.g. Polyester):", key="underfloor_type")
        underfloor_data["existing_r_value"] = st.text_input("Existing r-value (e.g. R1.5):", key="underfloor_r_value")
        underfloor_data["condition"] = st.text_input("Condition of existing insulation:", key="underfloor_condition")
        underfloor_data["compliant"] = st.selectbox("Compliant with HHS:", ["Yes", "No"], key="underfloor_compliant")
        underfloor_data["exempt"] = st.selectbox("Property is exempt from HHS:", ["No", "Yes"], key="underfloor_exempt")
        underfloor_data["access"] = st.text_input("Access to underfloor (e.g. External):", key="underfloor_access")
        underfloor_data["notes"] = st.text_area("Additional notes (optional):", key="underfloor_notes")
    else:
        underfloor_data["notes"] = st.text_area(
            "Reason why underfloor insulation is not applicable/exempt (e.g. Concrete slab floor, not applicable):",
            key="underfloor_na_notes"
        )
        underfloor_data["exempt"] = st.selectbox("Property is exempt from HHS:", ["No", "Yes"], key="underfloor_exempt_na")

    underfloor_photos = st.file_uploader(
        "Upload photos for Underfloor Insulation",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="underfloor_ins_photos"
    )

    return {
        "hhs_status": hhs_status,
        "ceiling": {
            "applicable": ceiling_applicable,
            **ceiling_data,
            "photos": ceiling_photos,
        },
        "underfloor": {
            "applicable": underfloor_applicable,
            **underfloor_data,
            "photos": underfloor_photos,
        }
    }
