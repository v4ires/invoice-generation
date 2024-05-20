import schedule
import time
import os
from datetime import datetime
from email_service import EmailService
from invoice_template import InvoiceTemplate

class EmailScheduler:
    def __init__(self, email_config, invoice_config, logger):
        self.email_config = email_config
        self.invoice_data = invoice_config
        self.logger = logger
        self.days_to_send = list(map(int, os.getenv('EMAIL_DAYS', '20,28').split(','))) 
        self.template = InvoiceTemplate('templates', self.logger)
        self.pdf_path = f"data/invoice_{self.invoice_data['invoice_number']}.pdf"

    def send_email(self):
        """Send email with invoice attachment."""
        try:
            email_service = EmailService(self.logger)
            email_service.send_email(self.email_config, self.pdf_path)
            self.logger.info("Email sent successfully.")
        except Exception as e:
            self.logger.error(f"Failed to send email: {e}")

    def generate_new_invoice(self):
        """Generate new invoice."""
        self.template.generate_invoice(self.invoice_data)
    
    def generate_invoice_send_email(self):
            self.generate_new_invoice()
            self.send_email()
            
    def send_monthly_emails(self):
        """Send emails on specified days of each month."""
        today = datetime.today()
        if today.day in self.days_to_send:
            self.generate_invoice_send_email()
        else:
            self.logger.info(f"Not the scheduled day ({today.day})")

    def send_every_x_seconds(self, seconds):
        """Send emails every X seconds."""
        schedule.every(seconds).seconds.do(self.generate_invoice_send_email)
        self.logger.info(f"Email scheduler set to send every {seconds} seconds")

    def send_every_x_minutes(self, minutes):
        """Send emails every X minutes."""
        schedule.every(minutes).minutes.do(self.generate_invoice_send_email)
        self.logger.info(f"Email scheduler set to send every {minutes} minutes")

    def send_every_x_hours(self, hours):
        """Send emails every X hours."""
        schedule.every(hours).hours.do(self.generate_invoice_send_email)
        self.logger.info(f"Email scheduler set to send every {hours} hours")

    def send_every_x_days(self, days):
        """Send emails every X days."""
        schedule.every(days).days.do(self.generate_invoice_send_email)
        self.logger.info(f"Email scheduler set to send every {days} days")

    def start_scheduler(self):
        """Start the scheduler."""
        self.logger.info("Scheduler started")
        while True:
            now = datetime.now()
            self.logger.info(f"Running Scheduler at {now}")
            schedule.run_pending()
            time.sleep(1)  # Check every second
