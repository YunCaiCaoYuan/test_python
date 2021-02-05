# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse

# class BookSpider(scrapy.Spider):
#     name = 'book'  # 爬虫名
#     allowed_domains = ['douban.com']  # 域名。爬虫爬取范围
#     start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T']  # 起始url，从第一页开始爬取
#
#     # 下载器获取WebServer的response，parse就是解析响应response的内容
#     def parse(self, response: HtmlResponse):  # 如何解析html;返回一个可迭代对象：利用yiled
#         print(type(response))  # scrapy.http.response.html.HtmlResponse
#         print(type(response.text))  # str
#         print(type(response.body))  # bytes
#         print(response.encoding)  # utf-8
#         # 将网页内容写入book.html文件内
#         with open('/Users/dannihong/Documents/leetcode/scrapy_project/file/book.html', 'w', encoding='utf-8') as f:
#             f.write(response.text)
#             f.flush()
#         except Exception as e:
#         print(e)


from ..items import Test1ProItem

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T']
    custom_settings = {'file_name': '/Users/sunbin/Documents/scrapy_project/file/books.json'}  # spider上自定义配置信息

    def parse(self, response: HtmlResponse):  # 如何解析html;返回一个可迭代对象：利用yiled
        subjects = response.xpath('//li[@class="subject-item"]')
        for subject in subjects:
            item =FirstProItem()
            title = subject.xpath('.//h2/a/text()').extract()
            item['title'] = title[0].strip()
            rate = subject.css('span.rating_nums::text').extract()
            item['rate'] = rate[0].strip()
            yield item  # 返回一个可迭代对象生成器
