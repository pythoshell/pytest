
"""
In this code:

Replace the placeholders with your SMTP server details, email addresses, and email content.

The code uses the smtplib library to connect to the SMTP server and send the email.

The email.mime modules are used to compose the email message, including the subject and content.

The starttls() method is used to upgrade the connection to a secure TLS connection for secure email transmission.

The email is sent using the sendmail method of the SMTP server.

Make sure to use an email account with the appropriate SMTP server settings and ensure that you provide your email credentials securely.
Additionally, you may need to enable "less secure apps" or generate an "App Password" for your email account, depending on your email service provider's security settings.

Always exercise caution when handling email credentials and sending automated emails.

"""



import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
smtp_server = "smtp.example.com"  # Replace with your SMTP server
smtp_port = 587  # Replace with the appropriate SMTP port
sender_email = "your_email@example.com"
sender_password = "your_password"
recipient_email = "recipient@example.com"

# Compose the email message
subject = "Hello from Python"
message = "This is a test email sent using Python."

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject
msg.attach(MIMEText(message, "plain"))

# Connect to the SMTP server and send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Upgrade the connection to a secure TLS connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
    print("Email sent successfully.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
