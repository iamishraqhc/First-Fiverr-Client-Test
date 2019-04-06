# import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

# message = Mail(
#     from_email='ishraq_josephite@yahoo.com',
#     to_emails='ishraq.h.c@gmail.com',
#     subject='Sending with SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')
# try:
#     sg = SendGridAPIClient('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')
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e)


# import sendgrid
# import os
# from sendgrid.helpers.mail import *
# import json

# sg = sendgrid.SendGridAPIClient('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')

# from_email = Email('ishraq_josephite@yahoo.com')
# to_email = Email('ishraq.h.c@gmail.com')
# subject = "Query from graaho website"
# text = "Test Message"
# content = Content("text/plain", text)
# mail = Mail(from_email, subject, to_email, content)
# response = sg.client.mail.send.post(request_body=mail.get())
# print(response.status_code)
# print(response.body)
# print(response.headers)
# result = {"success": True}

# response_headers = {
#     "Access-Control-Allow-Origin": "*",
#     "Access-Control-Allow-Methods": "PUT, GET, POST, DELETE, OPTIONS",
#     "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept,X-Requested-With, X-CSRF-Token,Authorization,"
# }

# return {'statusCode': 200, 'body': json.dumps(result), "headers": response_headers, "isBase64Encoded": False}


# import sendgrid
# import os
# from sendgrid.helpers.mail import *
# import json

# print(os.environ.get('SENDGRID_API_KEY'))
# sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
# # sg = sendgrid.SendGridAPIClient('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')
# from_email = Email("ishraq_josephite@yahoo.com")
# to_email = Email("ishraq.h.c@gmail.com")
# subject = "Sending with SendGrid is Fun"
# content = Content("text/plain", "and easy to do anywhere, even with Python")
# mail = Mail(from_email, subject, to_email, content)
# print(mail)
# var = "{'from': {'email': 'ishraq_josephite@yahoo.com'}, 'subject': "", 'personalizations': [{'to': [{'name': 'Sending', 'email': 'ishraq.h.c@gmail.com'}]}], 'content': [{'type': 'text/plain', 'value': 'and easy to do anywhere, even with Python'}]}"
# # json_var = json.loads(var)

# response = sg.client.mail.send.post(request_body= var)
# print(response)
# print(response.status_code)
# print(response.body)
# print(response.headers)

# setx SENDGRID_API_KEY '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'


# sg = sendgrid.SendGridAPIClient('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')
# from_email = Email('ishraq_josephite@yahoo.com', 'Ishraq')
# to_email = Email('ishraq.h.c@gmail.com')
# cc_email = Email('mobasshirbhuiyan.shagor@gmail.com')
# p = Personalization()
# p.add_to(to_email)
# p.add_cc(cc_email)
# subject = "check"
# content = Content("text/plain", "Hello")
# mail = Mail(from_email, subject, to_email, content)
# mail.add_personalization(p)
# response = sg.client.mail.send.post(request_body=mail.get())
# print(response)
# print(response.status_code)
# print(response.body)
# print(response.headers)


import os
from sendgrid import SendGridAPIClient

message = {
    'personalizations': [
        {
            'to': [
                {
                    'email': 'mobasshir.bhuiya@graaho.com'
                }
            ],
            # 'cc': [
            #     {
            #         'email': 'mobasshir.bhuiya@graaho.com'
            #     }
            # ],
            'subject': 'Sending with Twilio SendGrid is Fun'
        }
    ],
    'from': {
        'email': 'ishraq_josephite@yahoo.com'
    },
    'content': [
        {
            'type': 'text/plain',
            'value': 'and easy to do anywhere, even with Python'
        }
    ]
}
try:
    # print(os.environ.get('SENDGRID_API_KEY'))
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    # result = {"success": True}

    # response_headers = {
    #     "Access-Control-Allow-Origin": "*",
    #     "Access-Control-Allow-Methods": "PUT, GET, POST, DELETE, OPTIONS",
    #     "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept,X-Requested-With, X-CSRF-Token,Authorization,"
    # }

    # return {'statusCode': 200, 'body': json.dumps(result), "headers": response_headers, "isBase64Encoded": False}
except Exception as e:
    print(e.message)
