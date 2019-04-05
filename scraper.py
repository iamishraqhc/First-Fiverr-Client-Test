# Python3 code implementing web scraping using lxml

# import requests

# import only html class
# from lxml import html
#
# # url to scrape data from
# url = 'http://www.graaho.net/'
#
# # path to particular element
# path = '//*[@id="service-para"]'
#
# # get response object
# response = requests.get(url)
#
# # get byte string
# byte_data = response.content
#
# # get filtered source code
# source_code = html.fromstring(byte_data)
#
# # jump to preferred html element
# tree = source_code.xpath(path)
#
# # print texts in first element in list
# print(tree[0].text_content())

# import csv
#
# with open('testwebsite.csv', 'r') as csvFile:
#     reader = csv.reader(csvFile)
#     for row in reader:
#         print(type(str(row)))
#         response = requests.get(str(row))
#         print(response)
#
# csvFile.close()

# import requests

import requests
import pandas as pd
# import logging
import datetime


# logging.basicConfig(filename='myapp.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.INFO)
# logging.info('Started')
# logger = logging.getLogger(__name__)
count = 0

# siti web scuole || testwebsite

words = ['bando di gara', 'bando', 'gara', 'diario scolastico', 'diari']
rows = pd.read_csv('testwebsite.csv')

file_name_excel = f'output.xlsx'
writer = pd.ExcelWriter(file_name_excel)
for i,word in enumerate(words):
    print("Scraping for ", word, '\n')
    # dictionary
    words_to_append = {}
    for index, row in rows.iterrows():
        print(str(row['websites']))
        try:
            response = requests.get('http://' + row['websites']).text
            print(response.find(word))
            words_to_append[row['websites']] = response.find(word)
        except Exception as e:
            # logger.log(logging.ERROR,f'Exception from: start_driver {e}')
            print("Bad Request")
            words_to_append[row['websites']] = "Bad Request"
            pass
    keyword_data_frame = pd.DataFrame([words_to_append])
    print(keyword_data_frame)
    keyword_data_frame.to_excel(writer,f'Sheet{i}')
writer.save()

# for ind, row in rows.iterrowa():
#     rows.loc[index, datetime.date.today()] = response.find(word)