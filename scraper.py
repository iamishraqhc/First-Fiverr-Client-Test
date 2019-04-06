import requests
import pandas as pd
import datetime
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

now = datetime.datetime.now()
todays_date = str(now).split()[0]
previous_date = str(datetime.datetime.now()-datetime.timedelta(days=1)).split()[0]

words = ['bando di gara', 'bando', 'gara', 'diario scolastico', 'diari']
rows = pd.read_csv('testwebsite.csv') # siti web scuole
writer = pd.ExcelWriter('output.xlsx')
for i,word in enumerate(words):
    print("Scraping for ", word, '\n')
    websites = []
    word_founds = []
    for index, row in rows.iterrows():
        print(str(row['websites']))
        try:
            response = requests.get('http://' + row['websites']).text
            result = response.find(word)
            if result == -1:
                result = 0
            print(result)
            websites.append(row['websites'])
            word_founds.append(result)
        except Exception as e:
            print("Bad Request")
            websites.append(row['websites'])
            word_founds.append("Bad Request")
            pass
    # df = pd.read_excel('output.xlsx')  #, sheet_name=f'Sheet{i}')
    if os.path.exists('./output.xlsx'):
        df = pd.read_excel('output.xlsx')
        df2 = pd.DataFrame({f"{todays_date}": word_founds})
        df3 = df.join(df2)
        print(df3)
        df3.to_excel(writer, f'Sheet{i}', index=False)
    else:
        keyword_data_frame = pd.DataFrame({"Websites": websites,f"{todays_date}":word_founds}) 
        print(keyword_data_frame)
        keyword_data_frame.to_excel(writer, f'Sheet{i}', index=False)
writer.save()


for i,word in enumerate(words):
    if os.path.exists('./output.xlsx'):
        df = pd.read_excel('output.xlsx', sheet_name=f'Sheet{i}')
        if previous_date in df.columns:
            data = df[todays_date]-df[previous_date]
            for key, val in enumerate(data):
                if val != 0:
                    print('You are notified!!!')


message = Mail(
    from_email='ishraq_josephite@yahoo.com',
    to_emails='ishraq.h.c@gmail.com',
    subject='Sending with SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)