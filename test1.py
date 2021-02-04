#!/usr/bin/python
#-*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'http://www.chinanews.com/gn/2021/02-04/9404354.shtml'
    res = requests.get(url)
    #res.encoding='GBK'  # html: ISO-8859-1 (2012)
    res.encoding = 'utf-8' # (2019)
    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.find('h1')
    print(title.text.strip())

    news_contents = ''
    contents = soup.find('div', 'left_zw').find_all('p')
    for content in contents:
        if 'function' in content.text:
            continue
        news_contents = news_contents + content.text.strip()
    print(news_contents)
