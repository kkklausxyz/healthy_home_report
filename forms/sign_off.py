import streamlit as st
from streamlit_drawable_canvas import st_canvas
from datetime import date

def sign_off_form():
    st.header("Sign Off")

    st.subheader("Signature (please sign below)")
    canvas_result = st_canvas(
        fill_color="rgba(0, 0, 0, 0)",  # Transparent background
        stroke_width=2,
        stroke_color="#000000",
        background_color="#ffffff",
        height=100,
        width=400,
        drawing_mode="freedraw",
        key="sign_canvas"
    )

    signing_date = st.date_input(
        "Signing date:",
        value=date.today(),
        key="sign_off_date"
    )
    formatted_date = signing_date.strftime("%b %-d, %Y") if signing_date else ""

    if canvas_result.image_data is not None:
        st.image(canvas_result.image_data, caption="Signature Preview", use_container_width=True)

    return {
        "signing_date": formatted_date,
        "signature_image": canvas_result.image_data
    }
