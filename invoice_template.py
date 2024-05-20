import pdfkit
from jinja2 import Environment, FileSystemLoader

class InvoiceTemplate:
    def __init__(self, template_dir, logger):
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template = self.env.get_template('invoice_template.html')
        self.logger = logger

    def generate_invoice(self, data):
        """Generate PDF invoice from the provided data."""
        try:
            html_output = self.template.render(data=data)
            pdf_path = f"data/invoice_{data['invoice_number']}.pdf"
            pdfkit.from_string(html_output, pdf_path)
            self.logger.info(f"Invoice {data['invoice_number']} PDF generated successfully.")
        except Exception as e:
            self.logger.error(f"Failed to generate PDF: {e}")