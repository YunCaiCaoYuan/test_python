#!/usr/bin/python
# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd

if __name__ == '__main__':
    # 获取html网页
    url = 'http://top.baidu.com/buzz.php?p=top10&tdsourcetag=s_pctim_aiomsg&qq-pf-to=pcqq.c2c?'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Referer': 'http://top.baidu.com/'}
    # 请求超时时间为30秒
    r = requests.get(url, timeout=30, headers=header)
    # 如果状态码不是200，则引发日常
    r.raise_for_status()
    # 配置编码
    r.encoding = r.apparent_encoding
    # 获取源代码
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')


    title = soup.find_all('a', class_='list-title')
    #print("title=", title)
    point = soup.find_all('span', class_='icon-rise')
    print('{:^55}'.format('百度热搜榜'))
    print('{:^5}\t{:^40}\t{:^10}'.format('排名', '标题', '热度'))
    num = 20
    lst = []
    for i in range(num):
        print('{:^5}\t{:^40}\t{:^10}'.format(i + 1, title[i].string, point[i].string))
        lst.append([i + 1, title[i].string, point[i].string])
    df = pd.DataFrame(lst, columns=['排名', '标题', '热度'])
    rank = r'rank.xlsx'
    df.to_excel(rank)
