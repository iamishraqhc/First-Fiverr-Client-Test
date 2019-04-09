import requests
import pandas as pd
import datetime
import os
import logging

now = datetime.datetime.now()
todays_date = str(now).split()[0]
previous_date = str(datetime.datetime.now() -
                    datetime.timedelta(days=1)).split()[0]

words = ['bando di gara', 'bando', 'gara', 'diario scolastico', 'diari']
rows = pd.read_csv(os.path.join('script\\testwebsite.csv'))
writer = pd.ExcelWriter(os.path.join('output.xlsx'))
for i, word in enumerate(words):
    print("Scraping for ", word, '\n')
    websites = []
    word_founds = []
    for index, row in rows.iterrows():
        print(str(row['websites']))
        try:
            response = requests.get('http://' + row['websites']).text
            result1 = response.count(word.lower())
            result2 = response.count(word.upper())
            result3 = response.count(word.capitalize())
            result = result1 + result2 + result3
            if result < 0:
                result = 0
            print(result)
            websites.append(row['websites'])
            word_founds.append(result)
        except Exception as e:
            print("Bad Request")
            websites.append(row['websites'])
            word_founds.append("Bad Request")
            pass
            
    if os.path.exists(os.path.join('output.xlsx')):
        df = pd.read_excel(os.path.join('output.xlsx'))
        if str(todays_date) in df.columns:
            df1 = df.drop([str(todays_date)], axis=1)
            df2 = pd.DataFrame({f"{todays_date}": word_founds})
            df3 = df1.join(df2)
            print(df3)
            df3.to_excel(writer, f'Sheet{i}', index=False)
        else:
            pass
    else:
        keyword_data_frame = pd.DataFrame({"Websites": websites, f"{todays_date}": word_founds})
        print(keyword_data_frame)
        keyword_data_frame.to_excel(writer, f'Sheet{i}', index=False)
writer.save()

if os.path.exists(os.path.join('output.xlsx')):
    logging.basicConfig(filename=os.path.join(
        f'found_keywords_at_{str(now).split()[0]}.log'), format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
for i, word in enumerate(words):
    if os.path.exists(os.path.join('output.xlsx')):
        df = pd.read_excel(os.path.join('output.xlsx'), sheet_name=f'Sheet{i}')
        if previous_date in df.columns:
            data = df[todays_date]-df[previous_date]
            for key, val in enumerate(data):
                if val != 0:
                    logging.warning(f'{df.loc[key,"Websites"]} ===> {word}')

# if os.path.exists(os.path.join(f'found_keywords_at_{str(now).split()[0]}.log')):
#     file_name = f'found_keywords_at_{str(now).split()[0]}.log'
#     os.system(f'start {file_name}')
