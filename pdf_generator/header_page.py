from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Image, Table, Spacer, HRFlowable
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def generate_header_page_elements(info, photo_path=None):
    elements = []

    # Calculate content width (A4 width - left/right margin)
    PAGE_WIDTH, _ = A4
    LEFT_MARGIN = 30
    RIGHT_MARGIN = 30
    usable_width = PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN

    # Red banner title, centered and bold, white text
    banner_style = ParagraphStyle(
        name="BannerTitle",
        fontSize=14,
        leading=16,
        textColor=colors.white,
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
        spaceAfter=0,
        spaceBefore=0,
    )
    banner_table = Table(
        [[Paragraph("HEALTHY HOMES ASSESSMENT REPORT", banner_style)]],
        colWidths=[usable_width],  # Use usable_width here
        style=[
            ("BACKGROUND", (0, 0), (-1, -1), colors.red),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ],
    )
    elements.append(banner_table)
    elements.append(Spacer(1, 15))  # Space below banner

    # Info block styling
    label_style = ParagraphStyle(
        name="Label",
        fontSize=10,
        fontName="Helvetica-Bold",
        leading=15,
        textColor=colors.black,
        alignment=TA_LEFT,
        spaceAfter=0,
    )
    value_style = ParagraphStyle(
        name="Value",
        fontSize=10,
        fontName="Helvetica",
        leading=15,
        textColor=colors.black,
        alignment=TA_LEFT,
        spaceAfter=0,
    )

    # Info content (no links, no blue, no underline)
    info_lines = [
        ('Property address:', info['property_address']),
        ('Date of assessment:', info['date_of_assessment'].strftime("%b %d, %Y") if info['date_of_assessment'] else ""),
        ('Assessor name:', info['assessor_name']),
        ('Email &amp;Phone:', f"{info['email']} / {info['phone']}")
    ]
    # Add info lines with label and value on the same line, label bold
    for label, value in info_lines:
        text = f'<b>{label}</b> {value}'
        elements.append(Paragraph(text, value_style))
    elements.append(Spacer(1, 24))

    # Add property photo, centered
    if photo_path:
        img = Image(photo_path)
        img.drawHeight = 195
        img.drawWidth = 260
        img.hAlign = 'CENTER'
        elements.append(img)

    # Add a long red horizontal line as a divider at the bottom
    elements.append(Spacer(1, 16))
    elements.append(
        HRFlowable(
            width="100%",
            thickness=3,
            lineCap='round',
            color=colors.red,
            spaceBefore=0,
            spaceAfter=0
        )
    )

    return elements
