import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='ishraq_josephite@yahoo.com',
    to_emails='ishraq.h.c@gmail.com',
    subject='Sending with SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)