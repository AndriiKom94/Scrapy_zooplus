import requests
from bs4 import BeautifulSoup
import csv
from fake_useragent import UserAgent

import numpy as np


def get_random_ua():
    random_ua = ''
    ua_file = 'ua_file.txt'
    try:
        with open(ua_file) as f:
            lines = f.readlines()
        if len(lines) > 0:
            prng = np.random.RandomState()
            index = prng.permutation(len(lines) - 1)
            idx = np.asarray(index, dtype=np.integer)[0]
            random_ua = lines[int(idx)]
    except Exception as ex:
        print('Exception in random_ua')
        print(str(ex))
    finally:
        return random_ua

user_agent = get_random_ua()

ua = UserAgent()
HOST = 'https://www.zooplus.de/'
URL = 'https://www.zooplus.de/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'referer': 'https://www.zooplus.de/tierarzt/results',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,uk;q=0.8',
    'cache-control': 'max-age=0',
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


# def get_content(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('div', class_='result-intro__details')
#     doctors = []
#     print(items)


my_html = get_html(URL)
# get_content(my_html.text)
print(my_html.text)
