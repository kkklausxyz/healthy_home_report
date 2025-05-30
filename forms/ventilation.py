import streamlit as st

def ventilation_form():
    st.header("Ventilation")

    # Basic info for openable windows and doors
    hhs_status = st.selectbox(
        "HHS property compliancy status:",
        ["Property is compliant", "Property is NOT compliant"],
        key="vent_hhs_status"
    )
    room = st.text_input("Room:", value="Bedrooms/Living area/Bathrooms", key="vent_room")
    openable_window = st.selectbox("Openable window or door (fixed position):", ["Yes", "No"], key="vent_openable_window")
    room_exempt = st.selectbox("Room is exempt from HHS:", ["No", "Yes"], key="vent_room_exempt")

    st.markdown("----")
    st.subheader("Extraction Fans")

    # Use session_state to track fan IDs for dynamic management (unique keys)
    if "fan_ids" not in st.session_state:
        st.session_state.fan_ids = [1]  # List of fan IDs, always unique

    # Add Fan Button
    if st.button("Add Fan"):
        if len(st.session_state.fan_ids) == 0:
            st.session_state.fan_ids = [1]
        else:
            st.session_state.fan_ids.append(max(st.session_state.fan_ids) + 1)

    # For collecting fans' data
    fans_data = []
    to_delete = None

    # Each fan area with its own delete button
    for fan_id in st.session_state.fan_ids:
        with st.container():
            st.markdown(f"**Fan {fan_id}**")
            cols = st.columns([6, 1])
            with cols[1]:
                if st.button("Delete", key=f"delete_fan_{fan_id}"):
                    to_delete = fan_id
            with cols[0]:
                fan_hhs_status = st.selectbox(
                    f"Fan {fan_id} HHS property compliancy status:",
                    ["Property is compliant", "Property is NOT compliant"],
                    key=f"fan_{fan_id}_hhs_status"
                )
                fan_location = st.text_input(
                    f"Location of extraction fan (Fan {fan_id}):",
                    key=f"fan_{fan_id}_location"
                )
                fan_pre_existing = st.selectbox(
                    f"Pre-existing extraction fan (Fan {fan_id}):",
                    ["Yes", "No"],
                    key=f"fan_{fan_id}_pre_existing"
                )
                fan_operational = st.selectbox(
                    f"Fan operational (Fan {fan_id}):",
                    ["Yes", "No"],
                    key=f"fan_{fan_id}_operational"
                )
                fan_vents = st.selectbox(
                    f"Vents to the outdoors (Fan {fan_id}):",
                    ["Yes", "No"],
                    key=f"fan_{fan_id}_vents"
                )
                fan_diameter = st.text_input(
                    f"Exhaust ducting diameter (Fan {fan_id}) [e.g. 120mm]:",
                    key=f"fan_{fan_id}_diameter"
                )
                fan_exempt = st.selectbox(
                    f"Property is exempt from HHS (Fan {fan_id}):",
                    ["No", "Yes"],
                    key=f"fan_{fan_id}_exempt"
                )
                fan_photos = st.file_uploader(
                    f"Upload photos for Fan {fan_id}",
                    type=["jpg", "jpeg", "png"],
                    accept_multiple_files=True,
                    key=f"fan_{fan_id}_photos"
                )
                fans_data.append({
                    "hhs_status": fan_hhs_status,
                    "location": fan_location,
                    "pre_existing": fan_pre_existing,
                    "operational": fan_operational,
                    "vents": fan_vents,
                    "diameter": fan_diameter,
                    "exempt": fan_exempt,
                    "photos": fan_photos,
                })

    # Remove a fan if its delete button is pressed
    if to_delete is not None and len(st.session_state.fan_ids) > 1:
        st.session_state.fan_ids.remove(to_delete)
        st.rerun()

    # Return all the collected form data
    return {
        "openable_windows_and_doors": {
            "hhs_status": hhs_status,
            "room": room,
            "openable_window": openable_window,
            "room_exempt": room_exempt,
        },
        "fans": fans_data
    }
