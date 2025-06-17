from fpdf import FPDF

class PDFExporter:
    def __init__(self, title):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(0, 10, title, ln=True, align='C')

    def add_section(self, title, content):
        self.pdf.set_font("Arial", 'B', 14)
        self.pdf.cell(0, 10, title, ln=True)
        self.pdf.set_font("Arial", '', 12)
        self.pdf.multi_cell(0, 10, content)
        self.pdf.ln()

    def save(self, filename):
        self.pdf.output(filename)

def export_exam_to_pdf(exam_title, exam_details):
    pdf_exporter = PDFExporter(exam_title)
    for section_title, section_content in exam_details.items():
        pdf_exporter.add_section(section_title, section_content)
    pdf_exporter.save(f"{exam_title}.pdf")