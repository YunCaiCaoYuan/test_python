#!/usr/bin/env python
#-*- coding:UTF-8 -*-

from bs4 import BeautifulSoup
import bs4
import re

if __name__ == '__main__':
    # 待分析字符串
    html_doc = """ 
    <html> 
        <head> 
            <title>The Dormouse's story</title> 
        </head> 
        <body> 
        <p class="title aq"> 
            <b> 
                The Dormouse's story 
            </b> 
        </p> 
    
        <p class="story">Once upon a time there were three little sisters; and their names were 
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>, 
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>  
            and 
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; 
            and they lived at the bottom of a well. 
        </p> 
    
        <p class="story">...</p> 
        </body>
    </html>
    """
    # 每一段代码中注释部分即为运行结果
    # html字符串创建BeautifulSoup对象
    soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

    # 输出第一个 title 标签
    print(soup.title)
    # <title>The Dormouse's story</title>

    # 输出第一个 title 标签的标签名称
    print(soup.title.name)
    # title

    # 输出第一个 title 标签的包含内容
    print(soup.title.string)
    # The Dormouse's story

    # 输出第一个 title 标签的父标签的标签名称
    print(soup.title.parent.name)
    # head

    # 输出第一个 p 标签
    print(soup.p)
    """
    <p class="title aq">
    <b> 
                The Dormouse's story 
            </b>
    </p>
    """
    # 输出第一个 p 标签的 class 属性内容
    print(soup.p['class'])
    # ['title', 'aq']

    # 输出第一个 a 标签的  href 属性内容
    print(soup.a['href'])
    # http://example.com/elsie

    ''''' 
    soup的属性可以被添加,删除或修改. 操作方法与字典一样 
    '''
    # 修改第一个 a 标签的href属性为 http://www.baidu.com/
    # soup.a['href'] = 'http://www.baidu.com/'

    # 给第一个 a 标签添加 name 属性
    # soup.a['name'] = u'百度'

    # 删除第一个 a 标签的 class 属性为
    # del soup.a['class']

    ##输出第一个 p 标签的所有子节点
    print(soup.p.contents)
    """
    ['\n', <b> 
                The Dormouse's story 
            </b>, '\n']
    """

    # 输出第一个 a 标签
    print(soup.a)
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    # 输出所有的 a 标签，以列表形式显示
    print(soup.find_all('a'))
    """
    [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
    <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
    """

    # 输出第一个 id 属性等于  link3 的  a 标签
    print(soup.find(id="link3"))
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

    # 获取所有文字内容
    print(soup.get_text())
    """
    The Dormouse's story
                The Dormouse's story 
    Once upon a time there were three little sisters; and their names were 
            Elsie, 
            Lacie  
            and 
            Tillie; 
            and they lived at the bottom of a well. 
    ...
    """
    # 输出第一个  a 标签的所有属性信息
    print(soup.a.attrs)
    # {'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}

    for link in soup.find_all('a'):
        # 获取 link 的  href 属性内容
        print(link.get('href'))
    """
     http://example.com/elsie
     http://example.com/lacie
     http://example.com/tillie
    """
    # 对soup.p的子节点进行循环输出
    for child in soup.p.children:
        print("对soup.p的子节点进行循环输出", child)
    """
    对soup.p的子节点进行循环输出 
    
    对soup.p的子节点进行循环输出 <b> 
                The Dormouse's story 
            </b>
    对soup.p的子节点进行循环输出 
    
    """
    # 正则匹配，名字中带有b的标签
    for tag in soup.find_all(re.compile(r"b")):
        print(tag.name)
    """
    body
    b
    """

    print type(soup.a)

    print soup.name
    print soup.head.name

    print soup.p.attrs

    print type(soup.p.string)

    print type(soup.name)
    #<type 'unicode'>
    print soup.name
    # [document]
    print soup.attrs
    #{} 空字典

    print soup.a
    print soup.a.string
    print type(soup.a.string)
