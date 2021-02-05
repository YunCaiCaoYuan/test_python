# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class FirstPipeline:
#     def process_item(self, item, spider):
#         return item

from scrapy import Spider

class Test1ProPipeline(object):
    def __int__(self):
        print('~~~~~~~~~~init~~~~~~~~~~')

    # 每一个item都会执行一次
    def process_item(self, item, spider:Spider):
        print('++++++++++')
        print(item)
        self.file.write('{},\n'.format(json.dumps(dict(item))))
        return item

    # 所有过程在起始的时候执行一次
    def open_spider(self, spider):
        print('==========open spider {}=========='.format(spider))
        # file_name = '/Users/dannihong/Documents/leetcode/scrapy_project/file/books.json'
        file_name = spider.settings['file_name']
        self.file = open(file_name, 'w', encoding='utf-8')
        self.file.write('[\n')

    # 所有过程结束的时候执行一次
    def close_spider(self, spider):
        print('==========close spider {}=========='.format(spider))
        self.file.write(']')
        self.file.close()
