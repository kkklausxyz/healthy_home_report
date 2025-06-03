from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, HRFlowable
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def draught_section(draught_data):
    elements = []

    # Title
    elements.append(
        Paragraph(
            "<b>DRAUGHT STOPPING</b>",
            ParagraphStyle(
                name="SectionTitle",
                fontSize=15,
                textColor=colors.red,
                alignment=TA_CENTER,
                fontName="Helvetica-Bold",
                spaceBefore=0,
                spaceAfter=15
            )
        )
    )

    # HHS property compliancy status
    hhs_status = draught_data["hhs_status"]
    bg_color = "#36d946" if "compliant" in hhs_status.lower() else "red"
    hhs_html = (
        '<i><b>HHS property compliancy status:</b></i> '
        f'<font backcolor="{bg_color}" color="black"><b>{hhs_status}</b></font>'
    )
    elements.append(
        Paragraph(
            hhs_html,
            ParagraphStyle(
                name="HHS",
                fontSize=10,
                fontName="Helvetica-Oblique",
                leading=20,
                alignment=TA_LEFT,
                spaceAfter=15,
            )
        )
    )

    # Field style
    label_style = ParagraphStyle(
        name="FieldLabel",
        fontSize=10,
        fontName="Helvetica-Bold",
        leading=10,
        alignment=TA_LEFT,
        spaceAfter=1,
    )

    # Main fields (Open fire, Closed off, Fireplace closed off)
    fields = [
        ("Open fire:", draught_data["open_fire"]),
        ("Closed off:", draught_data["closed_off"]),
        ("Fireplace closed off:", draught_data["fireplace_closed_off"]),
    ]
    for label, value in fields:
        label_core = label[:-1] if label.endswith(':') else label
        text = f'<b>{label_core}</b>: {value}'
        elements.append(Paragraph(text, label_style))
    elements.append(Spacer(1, 18))

    # Doors part
    elements.append(Paragraph("<b>Location of doors</b>", label_style))
    elements.append(Paragraph(f'<b>Gaps or holes</b>: {draught_data["doors_gaps"]}', label_style))
    elements.append(Spacer(1, 16))

    # Windows part
    elements.append(Paragraph("<b>Location of windows</b>", label_style))
    elements.append(Paragraph(f'<b>Gaps or holes</b>: {draught_data["windows_gaps"]}', label_style))
    elements.append(Spacer(1, 16))

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
