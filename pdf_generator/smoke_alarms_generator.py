from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, HRFlowable, Table
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def smoke_alarms_section(smoke_data):
    elements = []

    # Section Title
    elements.append(
        Paragraph(
            "<b>SMOKE ALARMS</b>",
            ParagraphStyle(
                name="SectionTitle",
                fontSize=15,
                textColor=colors.red,
                alignment=TA_CENTER,
                fontName="Helvetica-Bold",
                spaceAfter=20
            )
        )
    )
    elements.append(Spacer(1, 16))

    # HHS compliancy status, italic and bold label, value with green background
    hhs_status_html = (
        '<i><b>HHS property compliancy status:</b> '
        f'<font backcolor="green" color="white">{smoke_data["hhs_status"]}</font></i>'
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

    # Field style
    label_style = ParagraphStyle(
        name="FieldLabel",
        fontSize=10,
        fontName="Helvetica-Bold",
        alignment=TA_LEFT,
        spaceAfter=6,
    )

    # Field lines
    fields = [
        ("Working smoke alarms:", smoke_data["working"]),
        ("Within 3m of a bedroom:", smoke_data["within_3m"]),
        ("Compliant smoke alarm:", smoke_data["compliant"]),
    ]
    for label, value in fields:
        label_core = label[:-1] if label.endswith(':') else label
        text = f'<b>{label_core}</b>: {value}'
        elements.append(Paragraph(text, label_style))

    # Bottom red divider
    elements.append(Spacer(1, 30))
    elements.append(
        HRFlowable(
            width="100%",
            thickness=2.5,
            color=colors.red,
            spaceBefore=16,
            spaceAfter=0,
        )
    )

    return elements
