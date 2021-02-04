#!/usr/bin/python
#-*- coding:UTF-8 -*-（添加）

import requests
from bs4 import BeautifulSoup
import json

NewCnt = 5

def get_url(date):
    url = 'http://www.chinanews.com/scroll-news/' + date +'/news.shtml'
    res = requests.get(url)
    #res.encoding='GBK'  # html: ISO-8859-1 (2012)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    li_tag = soup.find('div','content_list').find_all('li')
    category_list = []
    title_list = []
    url_list = []
    for li in li_tag:
        try:
            info = li.find_all('a')
            category = info[0].text
            if category in [u'国内']:
                category_list.append(category)
                news_title = info[1].text
                if len(title_list) == NewCnt:
                    break
                title_list.append(news_title)
                news_url = 'http://www.chinanews.com'+str(info[1].get('href'))
                url_list.append(news_url)
                #print("have done!"+ news_title+":"+news_url)
        except:
            continue
    # c = {
    #     'class':category_list, #类别
    #      'title':title_list,      #标题
    #      'url':url_list
    #      }
    for k,v in enumerate(title_list):
        print k+1,"、",v
    #dic = json.dumps(c, ensure_ascii = False, encoding = 'utf-8')
    #print(dic)


if __name__ == '__main__':
    date = "2021/0204"
    print date
    print "国内要闻"
    get_url(date)



