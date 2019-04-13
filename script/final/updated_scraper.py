import requests
import pandas as pd
import datetime
import os
import logging
from bs4 import BeautifulSoup
import re

now = datetime.datetime.now()
todays_date = str(now).split()[0]
previous_date = str(datetime.datetime.now() -
                    datetime.timedelta(days=1)).split()[0]

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}
                
print("Welcome to Keywords Scraper v0.20.3")

# New code snippet 
def scrape(search_url):
    """ Scrape raw text from given link and returns only contents """
    try:
        if 'http://' in search_url or 'https://' in search_url:
            response = requests.get(search_url,headers=headers).text
        else:
            response = requests.get('http://' + search_url,headers=headers).text
        return response
    except Exception as e:
        print(f"Got this exception from scraper: {e}")

def crawl(search_url):
    """ Crawl all the links in the given domain and returns as a list """
    try:
        if 'http://' in search_url or 'https://' in search_url:
            response = requests.get(search_url,headers=headers)
        else:
            response = requests.get('http://' + search_url, headers=headers)
    except Exception as e:
        print(f"Got this exception from crawl request function: {e}")
        return None 

    link_list = []
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content,"lxml")
        links = soup.find_all('a')
        links = [a for a in links if "href" in str(a)]
        for link in links:
            # print(link)
            if search_url in link['href']:
                link_list.append(link['href'])
            else:
                exp = re.match(r'^[a-zA-Z\d-]{,63}(\.[a-zA-Z\d-]{,63}).$',link['href'])
                if exp:
                    print(exp.groups())
                    pass
                else:
                    if link['href'].startswith('/'):
                        print(link['href'])
                        link_list.append(search_url + link['href'])
                    else:
                        print(link['href'])
                        pass
        return link_list
    return link_list


# words = ['bando di gara', 'bando', 'gara', 'diario scolastico', 'diari']
words = pd.read_csv(os.path.join('keywords_input.csv'))
words = [str(row['keywords']) for index, row in words.iterrows()]
rows = pd.read_csv(os.path.join('sitemap_input.csv'))
writer = pd.ExcelWriter(os.path.join('output.xlsx'))
for i, word in enumerate(words):
    print("Scraping for ", word, '\n')
    websites = []
    word_founds = []
    for index, row in rows.iterrows():
        print(str(row['websites']))
        # try:
        total_result = 0 ## Changes start
        crawl_domain_links = crawl(row['websites'])
        # print(crawl_domain_links)
        if crawl_domain_links:
            print(f"scraping {len(crawl_domain_links)} website pages under this domain: {str(row['websites'])}")
            crawl_domain_links.append(str(row['websites']))
            count = 0
            for link in crawl_domain_links:
                print(f" Counting on website no. : {count}")
                count += 1
                try:
                    raw_text = scrape(link)
                    if raw_text is not None:
                        raw_text = raw_text.lower()
                        word = word.lower()
                        total_result += raw_text.count(word)
                    else:
                        pass   ### Changes end
                except Exception as e2:
                    print(f" Got exception from scraper for loop: {e2}")
        # response = requests.get('http://' + row['websites']).text
        # result1 = response.find(word.lower())
        # result2 = response.find(word.upper())
        # result3 = response.find(word.capitalize())
        # result = result1 + result2 + result3
        result = total_result
        if result < 0:
            result = 0
        print(result)
        websites.append(row['websites'])
        word_founds.append(result)
        # except Exception as e:
        #     print("Bad Request")
        #     websites.append(row['websites'])
        #     word_founds.append("Bad Request")
        #     pass
            
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
