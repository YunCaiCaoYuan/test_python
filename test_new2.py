import requests
import pprint
import re
import urllib.parse

url = 'https://www.baidu.com/'

if __name__ == '__main__':
    headers = {
        'Host': 'www.baidu.com',
        'Referer': 'https://www.baidu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        # 'Cookie': 你的Cookie
    }

    response = requests.get(url, headers=headers).content.decode('utf-8')
    # 获取关键字
    pat = '"pure_title": "(.*?)"'
    keyword = re.findall(pat, response, re.S)
    print(len(keyword))

    for hot_word in keyword:
        # 汉字不符合url标准，所以这里需要进行url编码
        i = urllib.parse.quote(hot_word, encoding='utf-8', errors='replace')
        # url构建
        link = f'https://www.baidu.com/s?cl=3&tn=baidutop10&fr=top1000&wd={i}&rsv_idx=2&rsv_dl=fyb_n_homepage&hisfilter=1'
        print(link)
