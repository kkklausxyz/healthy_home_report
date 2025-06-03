from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle, Spacer, Image, HRFlowable
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def heating_section(heating_data, photo_paths):
    """
    Generate Heating section PDF elements for ReportLab.

    Args:
        heating_data: dict of heating section fields
        photo_paths: list of local file paths for images

    Returns:
        list of ReportLab elements
    """
    elements = []

    # Section title: centered, red, bold
    section_title = Paragraph(
        '<b>HEATING</b>',
        ParagraphStyle(
            name="SectionTitle",
            fontSize=24,
            textColor=colors.red,
            alignment=TA_CENTER,
            fontName="Helvetica-Bold",
            spaceAfter=10
        ),
    )
    elements.append(section_title)
    elements.append(Spacer(1, 8))

    # HHS compliancy status, italic and bold label, value with green background
    hhs_status_html = (
        '<i><b>HHS property compliancy status:</b> '
        f'<font backcolor="green" color="white">{heating_data["hhs_status"]}</font></i>'
    )
    elements.append(
        Paragraph(
            hhs_status_html,
            ParagraphStyle(
                name="Compliancy",
                fontSize=12,
                leading=16,
                fontName="Helvetica-Oblique"
            )
        )
    )
    elements.append(Spacer(1, 6))

    # Basic info
    info_style = ParagraphStyle(
        name="InfoLine",
        fontSize=12,
        leading=16,
        fontName="Helvetica",
        alignment=TA_LEFT
    )
    info_lines = [
        ("Location of heat pump:", heating_data["location"]),
        ("Required heating capacity:", heating_data["required_capacity"]),
        ("Pre-existing fixed heater:", heating_data["pre_existing_heater"]),
        ("Property is exempt from HHS:", heating_data["exempt_from_hhs"])
    ]
    for label, value in info_lines:
        text = f'<b>{label}</b> {value}'
        elements.append(Paragraph(text, info_style))
    elements.append(Spacer(1, 12))

    # Subtitle for pre-existing heater
    subtitle = Paragraph(
        "PRE-EXISTING FIXED HEATER",
        ParagraphStyle(
            name="SubTitle",
            fontSize=16,
            fontName="Helvetica-Bold",
            textColor=colors.HexColor("#666666"),
            alignment=TA_LEFT,
            spaceBefore=10,
            spaceAfter=8
        )
    )
    elements.append(subtitle)

    # Subsection info
    subinfo_lines = [
        ("Heater Compliant:", heating_data["heater_compliant"]),
        ("Operational:", heating_data["operational"])
    ]
    subinfo_style = ParagraphStyle(
        name="SubInfo",
        fontSize=12,
        leading=16,
        fontName="Helvetica",
        alignment=TA_LEFT
    )
    for label, value in subinfo_lines:
        text = f'<b>{label}</b> {value}'
        elements.append(Paragraph(text, subinfo_style))

    elements.append(Spacer(1, 12))

    # Images: 2 per row
    if photo_paths:
        imgs = []
        for img_path in photo_paths:
            img = Image(img_path)
            img.drawHeight = 180
            img.drawWidth = 180
            imgs.append(img)
        img_rows = [imgs[i:i+2] for i in range(0, len(imgs), 2)]
        for row in img_rows:
            table = Table([row], hAlign="LEFT", style=[("BOTTOMPADDING", (0,0), (-1,-1), 8)])
            elements.append(table)

    # Red horizontal line at bottom
    elements.append(Spacer(1, 10))
    elements.append(
        HRFlowable(
            width="100%",
            thickness=3,
            color=colors.red,
            spaceBefore=0,
            spaceAfter=0
        )
    )

    return elements
