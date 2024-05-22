import json
import os
from dotenv import load_dotenv
from scheduler import EmailScheduler
from logger_setup import setup_logger

# Load environment variables from .env file
load_dotenv()

# Setup logger
logger = setup_logger('EmailSchedulerLogger')

if __name__ == '__main__':
    # Load JSON data for email configuration
    email_config_path = 'examples/email.json'
    with open(email_config_path, 'r') as file:
        email_config = json.load(file)

    # Load JSON data for invoice
    invoice_params_path = 'examples/invoice.json'
    with open(invoice_params_path, 'r') as file:
        invoice_config = json.load(file)

    
    # Create an instance of EmailScheduler
    scheduler = EmailScheduler(email_config, invoice_config, logger)
    
    # Schedule the emails
    #scheduler.send_monthly_emails()
    # Optionally, you can use the other scheduling functions like below:
    scheduler.send_every_x_seconds(1)
    # scheduler.send_every_x_minutes(1)
    # scheduler.send_every_x_hours(1)
    # scheduler.send_every_x_days(1)
    
    # Start the scheduler
    scheduler.start_scheduler()