#!/usr/bin/python
#-*- coding:UTF-8 -*-（添加）

import requests
from bs4 import BeautifulSoup
import json

'''
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
'''

def get_url(date):
    url = 'http://www.chinanews.com/scroll-news/' + date +'/news.shtml'
    res = requests.get(url)
    #res.encoding='GBK'  # html: ISO-8859-1 (2012)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    ret = soup.find('div','content_list')
    li_tag = ret.find_all('li')
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
                title_list.append(news_title)
                news_url = 'http://www.chinanews.com'+str(info[1].get('href'))
                url_list.append(news_url)
                #print("have done!"+ news_title+":"+news_url)
        except:
            continue
    c = {
        #'class':category_list, #类别
         'title':title_list,      #标题
         #'url':url_list
         }
    dic = json.dumps(c, ensure_ascii = False, encoding = 'utf-8')
    print(dic)

    # data=DataFrame(c)
    # print(data)

if __name__ == '__main__':
    date = "2021/0204"
    print date
    get_url(date)
