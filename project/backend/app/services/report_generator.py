from fpdf import FPDF

class ReportGenerator:
    @staticmethod
    def generate_pdf(case_data: dict, analysis_data: dict) -> str:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Forensic Report", ln=True, align='C')
        # ... add analysis_data ...
        path = f"/tmp/report_{case_data['id']}.pdf"
        pdf.output(path)
        return path
