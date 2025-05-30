import streamlit as st

from forms.basic_info import basic_info_form
from forms.heating import heating_form
from forms.ventilation import ventilation_form
from forms.draught import draught_form
from forms.smoke_alarms import smoke_alarms_form
from forms.insulation import insulation_form
from forms.moisture import moisture_form
from forms.sign_off import sign_off_form

st.set_page_config(page_title="Healthy Home Assessment Report Generator")
st.title("Healthy Home Assessment Report Generator")

basic_info = basic_info_form()
st.markdown("---")
heating_data = heating_form()
st.markdown("---")
ventilation_data = ventilation_form()
st.markdown("---")
draught_data = draught_form()
st.markdown("---")
smoke_alarms_data = smoke_alarms_form()
st.markdown("---")
insulation_data = insulation_form()
st.markdown("---")
moisture_data = moisture_form()
st.markdown("---")
sign_off_data = sign_off_form()
st.markdown("---")

section_photo_groups = [
    ("Heating", heating_data["photos"]),
]

# Add each fan's photos from ventilation_data
for idx, fan in enumerate(ventilation_data["fans"]):
    section_photo_groups.append((f"Ventilation Fan {idx+1}", fan["photos"]))

section_photo_groups += [
    ("Draught Stopping", draught_data["photos"]),
    # ("Smoke Alarms", smoke_alarms_data["photos"]),  # 如需展示可以解注释
    ("Ceiling Insulation", insulation_data["ceiling"]["photos"]),
    ("Underfloor Insulation", insulation_data["underfloor"]["photos"]),
    ("Ground Vapour Barrier", moisture_data["ground_vapour_barrier"]["photos"]),
    ("Drainage", moisture_data["drainage"]["photos"]),
]


for label, photos in section_photo_groups:
    if photos:
        st.subheader(f"Uploaded Photos for {label}")
        for img in photos:
            st.image(img, width=200)

if st.button("Generate PDF Report"):
    st.success("PDF generation logic is not implemented yet. All information and photos are now properly grouped for PDF output!")
