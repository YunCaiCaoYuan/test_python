#!/usr/bin/env python
#-*- coding:UTF-8 -*-

from bs4 import BeautifulSoup

if __name__ == '__main__':
    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """

    #soup = BeautifulSoup(html)
    soup = BeautifulSoup(open('index.html'))  #使用本地文件创建对象

    print soup.prettify()
