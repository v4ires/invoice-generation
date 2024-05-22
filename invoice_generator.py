import datetime
import os
import pdfkit
from typing import Any, Dict
from jinja2 import Environment, FileSystemLoader


class InvoiceGenerator:
    def __init__(self, template_dir, logger):
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template = self.env.get_template('invoice_template.html')
        self.logger = logger


    def generate_invoice(self, data: Dict[str, Any]) -> None:
        """
        Generate PDF invoice from the provided data.

        Usage example:
            template = ...  # Template engine instance
            logger = ...    # Logger instance
            data = {
                'invoice_number': '1234',
                'issue_date': '2023-01-01',
                'due_date': '2023-01-15',
                'customer_name': 'John Doe',
                'items': [
                    {'description': 'Product 1', 'quantity': 1, 'price': 100},
                    {'description': 'Product 2', 'quantity': 2, 'price': 50},
                ],
                'total_amount': 200
            }
            generator = InvoiceGenerator(template, logger)
            generator.generate_invoice(data)
        """
        try:
            # Dynamic invoice values
            if not data.get('issue_date'):
                data['issue_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
            if not data.get('due_date'):
                data['due_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
            # Render HTML
            html_output = self.template.render(data=data)
            
            # Ensure the directory exists
            output_dir = "data"
            os.makedirs(output_dir, exist_ok=True)
            
            # Define PDF path
            print(data)
            pdf_path = os.path.join(output_dir, f"invoice_{data['invoice_number']}.pdf")
            
            # Generate PDF
            pdfkit.from_string(html_output, pdf_path)
            self.logger.info(f"Invoice {data['invoice_number']} PDF generated successfully.")
        
        except KeyError as e:
            self.logger.error(f"Missing key in data: {e}")
        except IOError as e:
            self.logger.error(f"File I/O error: {e}")
        except Exception as e:
            self.logger.error(f"Failed to generate PDF: {e}")