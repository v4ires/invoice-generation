
# Invoice Generator

This Python application generates a PDF invoice from a JSON input using Jinja2 for templating and pdfkit for PDF creation.

## Installation

1. Install the required Python libraries:
   ```
   pip install -r requirements.txt
   ```

2. You must have `wkhtmltopdf` installed on your system. Refer to https://wkhtmltopdf.org for installation instructions.

## Usage

To generate an invoice, run:
```
python generate_invoice.py <path_to_invoice_data.json>
```
Replace `<path_to_invoice_data.json>` with the path to your JSON file containing the invoice data. You can run the sample.json as reference.

## Email Service

export SMTP_USER="your_email@gmail.com"
export SMTP_PASSWORD="your_password"

Adjust the email.json file with email parameters


