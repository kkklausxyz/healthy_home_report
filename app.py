import streamlit as st
import os

from pdf_generator.header_page import generate_header_page_elements
from pdf_generator.heating_generator import heating_section
from pdf_generator.ventilation_generator import ventilation_section
from pdf_generator.draught_generator import draught_section


from datetime import datetime
from PIL import Image as PILImage

from forms.basic_info import basic_info_form
from forms.heating import heating_form
from forms.ventilation import ventilation_form
from forms.draught import draught_form

from reportlab.platypus import SimpleDocTemplate

st.set_page_config(page_title="Healthy Home Assessment Report Generator")
st.title("Healthy Home Assessment Report Generator")

# Collect basic info and heating info
basic_info = basic_info_form()
st.markdown("---")
heating_data = heating_form()
st.markdown("---")
ventilation_data = ventilation_form()
st.markdown("---")
draught_data = draught_form()
st.markdown("---")

if st.button("Generate PDF Report"):
    # Save uploaded image for header page if present
    temp_photo_path = None
    if basic_info["photo"] is not None:
        pil_img = PILImage.open(basic_info["photo"])
        temp_photo_path = "temp_property_photo.png"
        pil_img.save(temp_photo_path)

    # Save heating photos if present
    heating_photo_paths = []
    if heating_data["photos"]:
        for i, file in enumerate(heating_data["photos"]):
            img = PILImage.open(file)
            img_path = f"temp_heating_photo_{i}.png"
            img.save(img_path)
            heating_photo_paths.append(img_path)

    # Prepare ventilation fan photos: fans_photo_paths = [[fan1_img1, ...], [fan2_img1, ...], ...]
    fans_photo_paths = []
    for i, fan in enumerate(ventilation_data["fans"]):
        this_fan_photo_paths = []
        if fan["photos"]:
            for j, file in enumerate(fan["photos"]):
                img = PILImage.open(file)
                img_path = f"temp_vent_fan_{i}_{j}.png"
                img.save(img_path)
                this_fan_photo_paths.append(img_path)
        fans_photo_paths.append(this_fan_photo_paths)

    # Generate PDF content
    pdf_path = "report_output.pdf"
    doc = SimpleDocTemplate(pdf_path)

    # Gather all elements (header + heating)
    elements = []
    elements += generate_header_page_elements(basic_info, photo_path=temp_photo_path)
    elements += heating_section(heating_data, heating_photo_paths)
    elements += ventilation_section(ventilation_data, fans_photo_paths)
    elements += draught_section(draught_data)

    # Build the PDF
    doc.build(elements)

    # Offer the PDF for download
    with open(pdf_path, "rb") as f:
        st.download_button("Download PDF", f, file_name="HealthyHomeReport.pdf", mime="application/pdf")
    st.success("PDF generated successfully!")

    # Cleanup temp image files
    if temp_photo_path and os.path.exists(temp_photo_path):
        os.remove(temp_photo_path)
    for path in heating_photo_paths:
        if os.path.exists(path):
            os.remove(path)

    # ...heating temp cleanup...
    for fan_paths in fans_photo_paths:
        for path in fan_paths:
            if os.path.exists(path):
                os.remove(path)

