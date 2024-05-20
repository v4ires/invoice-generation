import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

class EmailService:
    def __init__(self, logger):
        self.logger = logger

    def send_email(self, email_config, attachment_path):
        """Send an email with the provided attachment using the email configuration."""
        message = Mail(
            from_email=email_config['from_email'],
            to_emails=email_config['to_email'],
            subject=email_config['subject'],
            html_content=email_config['body']
        )

        # Attach the PDF file
        with open(attachment_path, 'rb') as f:
            data = f.read()
        encoded_file = base64.b64encode(data).decode()
        attachment = Attachment()
        attachment.file_content = FileContent(encoded_file)
        attachment.file_name = FileName(os.path.basename(attachment_path))
        attachment.file_type = FileType('application/pdf')
        attachment.disposition = Disposition('attachment')
        message.attachment = attachment

        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            self.logger.info(f"Email sent to {email_config['to_email']} with attachment {attachment_path}.")
            self.logger.info(f"Response status code: {response.status_code}")
        except Exception as e:
            self.logger.error(f"Failed to send email: {e}")
