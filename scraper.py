# Python3 code implementing web scraping using lxml

import requests

# import only html class
from lxml import html
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
import logging


logging.basicConfig(filename='myapp.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.INFO)
logging.info('Started')

rows = pd.read_csv('testwebsite.csv')
for index, row in rows.iterrows():
    print(str(row['websites']))

    response = requests.get('http://' + row['websites']).text
    print(response.find('gov'))
    logging.info(response.find('gov'))