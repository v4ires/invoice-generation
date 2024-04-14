
import json
import pdfkit
from jinja2 import Environment, FileSystemLoader
import sys

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('invoice_template.html')

def generate_invoice(data):
    # Render the HTML content
    html_output = template.render(data=data)
    pdfkit.from_string(html_output, f"data/invoice_{data['invoice_number']}.pdf")
    print(f"Invoice {data['invoice_number']} PDF generated successfully.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python generate_invoice.py <invoice_params.json>")
        sys.exit(1)

    # Load JSON data
    with open(sys.argv[1], 'r') as file:
        data = json.load(file)

    generate_invoice(data)
