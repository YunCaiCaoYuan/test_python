#!/usr/bin/python
#-*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup

NewCnt = 5

def get_url(date, category_list):
    url = 'http://www.chinanews.com/scroll-news/' + date +'/news.shtml'
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    li_tag = soup.find('div','content_list').find_all('li')
    news_dict = {}
    for li in li_tag:
        try:
            info = li.find_all('a')
            category = info[0].text
            if category in category_list:
                news_title = info[1].text
                title_list = news_dict.get(category, [])
                if len(title_list) == NewCnt:
                    continue
                title_list.append(news_title)
                news_dict[category] = title_list
        except:
            continue

    for key,value in news_dict.items():
        print key
        for k,v in enumerate(news_dict[key]):
           print k+1,"、",v


if __name__ == '__main__':
    date = "2021/0204"
    print date
    get_url(date, [u'国内', u'娱乐'])



