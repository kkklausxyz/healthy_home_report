from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import HRFlowable


def ventilation_section(ventilation_data, fans_photo_paths):
    """
    Generate Ventilation section elements for ReportLab.

    Args:
        ventilation_data: dict, from ventilation_form
        fans_photo_paths: list of list，每个 fan 的图片本地路径列表

    Returns:
        list of ReportLab elements
    """
    elements = []

    # Section Title
    section_title = Paragraph(
        '<b>VENTILATION</b>',
        ParagraphStyle(
            name="SectionTitle",
            fontSize=32,
            textColor=colors.red,
            alignment=TA_CENTER,
            fontName="Helvetica-Bold",
            spaceAfter=20
        ),
    )
    elements.append(section_title)
    elements.append(Spacer(1, 30))

    # --- Openable windows and doors ---
    elements.append(
        Paragraph(
            "<b>OPENABLE WINDOWS AND DOORS</b>",
            ParagraphStyle(
                name="BigSubTitle",
                fontSize=15,
                fontName="Helvetica-Bold",
                textColor=colors.black,
                alignment=TA_LEFT,
                spaceAfter=16,
            )
        )
    )

    # HHS property compliancy status (italic bold label, color background for value)
    openable = ventilation_data["openable_windows_and_doors"]
    hhs_status = openable["hhs_status"]
    hhs_bg_color = "red" if "not compliant" in hhs_status.lower() else "#36d946"
    hhs_status_html = (
        '<i><b>HHS property compliancy status:</b></i> '
        f'<font backcolor="{hhs_bg_color}" color="black"><b>{hhs_status}</b></font>'
    )
    elements.append(
        Paragraph(
            hhs_status_html,
            ParagraphStyle(
                name="Compliancy",
                fontSize=10,
                leading=15,
                fontName="Helvetica-Oblique"
            )
        )
    )
    elements.append(Spacer(1, 12))

    # Info
    info_style = ParagraphStyle(
        name="InfoLine",
        fontSize=10,
        leading=15,
        fontName="Helvetica",
        alignment=TA_LEFT
    )
    bold_label = lambda label, value: f'<b>{label}</b> {value}'
    elements.append(Paragraph(bold_label("Room:", openable["room"]), info_style))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph(bold_label("Openable window or door (fixed position):", openable["openable_window"]), info_style))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph(bold_label("Room is exempt from HHS:", openable["room_exempt"]), info_style))
    elements.append(Spacer(1, 40))

    # --- Extraction Fans ---
    elements.append(
        Paragraph(
            "<b>EXTRACTION FANS</b>",
            ParagraphStyle(
                name="FansSubTitle",
                fontSize=15,
                fontName="Helvetica-Bold",
                textColor=colors.black,
                alignment=TA_LEFT,
                spaceAfter=10,
            )
        )
    )
    # fans: list of dict
    for idx, fan in enumerate(ventilation_data["fans"]):
        fan_title = Paragraph(
            f'<b><font color="#888888">FAN {idx+1}</font></b>',
            ParagraphStyle(
                name="FanTitle",
                fontSize=10,
                fontName="Helvetica-Bold",
                textColor=colors.HexColor("#888888"),
                alignment=TA_LEFT,
                spaceBefore=4,
                spaceAfter=6
            )
        )
        elements.append(fan_title)

        # HHS property compliancy status for fan
        fan_hhs_status = fan["hhs_status"]
        fan_hhs_bg = "red" if "not compliant" in fan_hhs_status.lower() else "#36d946"
        fan_hhs_html = (
            '<i><b>HHS property compliancy status:</b></i> '
            f'<font backcolor="{fan_hhs_bg}" color="black"><b>{fan_hhs_status}</b></font>'
        )
        elements.append(
            Paragraph(
                fan_hhs_html,
                ParagraphStyle(
                    name="Compliancy",
                    fontSize=10,
                    leading=15,
                    fontName="Helvetica-Oblique"
                )
            )
        )
        elements.append(Spacer(1, 6))

        # Info for fan
        fan_info_style = ParagraphStyle(
            name="FanInfo",
            fontSize=10,
            leading=15,
            fontName="Helvetica",
            alignment=TA_LEFT
        )
        def b(label, value):
            return f'<b>{label}</b> {value}'

        fan_info_lines = [
            b("Location of extraction fan:", fan["location"]),
            b("Pre-existing extraction fan:", fan["pre_existing"]),
            b("Fan operational:", fan["operational"]),
            b("Vents to the outdoors:", fan["vents"]),
            b("Exhaust ducting diameter:", fan["diameter"]),
            b("Property is exempt from HHS:", fan["exempt"]),
        ]
        for l in fan_info_lines:
            elements.append(Paragraph(l, fan_info_style))
            elements.append(Spacer(1, 2))

        # Fan photos (2 per row)
        if fans_photo_paths and len(fans_photo_paths) > idx:
            fan_photos = fans_photo_paths[idx]
            if fan_photos:
                imgs = []
                for img_path in fan_photos:
                    img = Image(img_path)
                    img.drawHeight = 180
                    img.drawWidth = 180
                    imgs.append(img)
                img_rows = [imgs[i:i+2] for i in range(0, len(imgs), 2)]
                for row in img_rows:
                    table = Table([row], hAlign="LEFT", style=[("BOTTOMPADDING", (0,0), (-1,-1), 8)])
                    elements.append(table)
        elements.append(Spacer(1, 18))

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
