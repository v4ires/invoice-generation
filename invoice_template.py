import pdfkit
from jinja2 import Environment, FileSystemLoader
import datetime

class InvoiceTemplate:
    def __init__(self, template_dir, logger):
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template = self.env.get_template('invoice_template.html')
        self.logger = logger


    def generate_invoice(self, data):
        """Generate PDF invoice from the provided data."""
        try:
            # Dynamic invoice values
            data['issue_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
            data['due_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
            html_output = self.template.render(data=data)
            invoice_number = data['invoice_number']
            pdf_path = f"data/invoice_{invoice_number}.pdf"
            pdfkit.from_string(html_output, pdf_path)
            self.logger.info(f"Invoice {invoice_number} PDF generated successfully.")
        except Exception as e:
            self.logger.error(f"Failed to generate PDF: {e}")