import streamlit as st

def smoke_alarms_form():
    st.header("Smoke Alarms")

    hhs_status = st.selectbox(
        "HHS property compliancy status:",
        ["Property is compliant", "Property is NOT compliant"],
        key="smoke_hhs_status"
    )
    working = st.selectbox(
        "Working smoke alarms:",
        ["Yes", "No"],
        key="smoke_working"
    )
    within_3m = st.selectbox(
        "Within 3m of a bedroom:",
        ["Yes", "No"],
        key="smoke_within_3m"
    )
    compliant = st.selectbox(
        "Compliant smoke alarm:",
        ["Yes", "No"],
        key="smoke_compliant"
    )

    return {
        "hhs_status": hhs_status,
        "working": working,
        "within_3m": within_3m,
        "compliant": compliant,
    }
