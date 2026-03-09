from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

def create_pdf_report(results):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"results/{timestamp}_report.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4, rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=20)
    elements = []
    styles = getSampleStyleSheet()

    #==== HEADER ====
    elements.append(Paragraph("CyberDorm Vulnerability Report", styles['Title']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Scan date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Total hosts scanned: {len(results)}", styles['Normal']))
    elements.append(Spacer(1, 20))

    #==== TABLES FOR EACH HOST ====
    for host, ports in results.items():
        elements.append(Paragraph(f"Host: {host}", styles['Heading2']))
        elements.append(Spacer(1, 8))

        #==== COLUMNS ====
        data = [["Port", "Service", "Version", "CVE", "Severity"]]

        for port, info in ports.items():
            service = info.get("service", "-")
            version = info.get("version", "-")
            vulns = info.get("vulns", [])
            if vulns:
                first_vuln = vulns[0]
                cve = first_vuln.get("cve", "-")
                sev = "-"
                sev_list = first_vuln.get("severity", {}).get("cvssMetricV30", [])
                if sev_list:
                    sev = sev_list[0]["cvssData"]["baseSeverity"]
                data.append([str(port), service, version, Paragraph(cve, styles['Normal']), Paragraph(sev, styles['Normal'])])
                for v in vulns[1:]:
                    cve = v.get("cve", "-")
                    sev = "-"
                    sev_list = v.get("severity", {}).get("cvssMetricV30", [])
                    if sev_list:
                        sev = sev_list[0]["cvssData"]["baseSeverity"]
                    data.append(["", "", "", Paragraph(cve, styles['Normal']), Paragraph(sev, styles['Normal'])])
            else:
                data.append([str(port), service, version, "-", "-"])

        table = Table(data, colWidths=[40, 120, 60, 200, 60], repeatRows=1)

        style = TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.grey),
            ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
            ('ALIGN',(0,0),(-1,-1),'LEFT'),
            ('VALIGN',(0,0),(-1,-1),'TOP'),
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ])

        for i, row in enumerate(data[1:], start=1):
            if isinstance(row[4], Paragraph):
                sev_text = row[4].getPlainText().upper()
            else:
                sev_text = str(row[4]).upper()
            if "HIGH" in sev_text:
                style.add('BACKGROUND', (4,i), (4,i), colors.red)
                style.add('TEXTCOLOR', (4,i), (4,i), colors.whitesmoke)
            elif "MEDIUM" in sev_text:
                style.add('BACKGROUND', (4,i), (4,i), colors.orange)
            elif "LOW" in sev_text:
                style.add('BACKGROUND', (4,i), (4,i), colors.yellow)

        table.setStyle(style)
        elements.append(table)
        elements.append(Spacer(1, 20))

    #==== BUILDING PDF ====
    doc.build(elements)