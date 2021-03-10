#!/usr/bin/python
# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')

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
    #print("soup=", soup)

    title = soup.find_all('a', class_='list-title')


    print('{:^55}'.format('百度热搜榜'))
    print('{:^5}\t{:^40}'.format('排名', '标题'))

    num = 1
    lst = []
    for i in range(num):
        # print("title[i]=", title[i])
        # print("title[i]2=", title[i].attrs)
        print("title[i]3=", title[i]['href'])

        r = requests.get(title[i]['href'], timeout=30, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        # print("soup=", soup)
        result_container = soup.find_all('a', class_='op_sp_realtime_new_group_title_text', limit=1)
        print("result_container=", result_container)
        print("result_container[0].attrs=", result_container[0].attrs)


    #print('{:^5}\t{:^40}'.format(i + 1, title[i].string))
        # lst.append([i + 1, title[i].string])
    # df = pd.DataFrame(lst, columns=['排名', '标题'])
    # rank = r'rank.xlsx'
    # df.to_excel(rank)


# [<div class="result c-container new-pmd" data-click="{'rsv_bdr':'' }" id="4" srcid="1599" tpl="se_com_default"><h3 class="t"><a data-click="{\n\t\t\t'F':'778F37EA',\n\t\t\t'F1':'9D63F1E4',\n\t\t\t'F2':'4CA6DE6B',\n\t\t\t'F3':'54E5263F',\n\t\t\t'T':'1612666391',\n\t\t\t\t\t\t'y':'FF7F1FFA'\n\t\t\t\t\t\t\t\t\t\t\t\t}" href="http://www.baidu.com/link?url=aFWvNvggPt55DjQYg0nddtvbzSWJFO7f1lYwpUA0LqSqfessziVH4YaOi8_t5WNwQ9WhyCpmbICiAjhrsK_BI_" target="_blank"><em>31\u7701\u533a\u5e02\u65b0\u589e\u786e\u8bca</em>\u75c5\u4f8b<em>11\u4f8b</em>,\u5176\u4e2d<em>\u672c\u571f</em>\u75c5\u4f8b<em>1\u4f8b</em>_\u4eac\u62a5\u7f51</a></h3><div class="c-row c-gap-top-small"><div class="general_image_pic c-span3" style="position:relative;top:2px;"><a class="c-img c-img3 c-img-radius-large" href="http://www.baidu.com/link?url=aFWvNvggPt55DjQYg0nddtvbzSWJFO7f1lYwpUA0LqSqfessziVH4YaOi8_t5WNwQ9WhyCpmbICiAjhrsK_BI_" style="height:85px" target="_blank"><img class="c-img c-img3 c-img-radius-large" src="http://t7.baidu.com/it/u=793971196,4273795572&amp;fm=218&amp;app=2&amp;f=JPEG?w=121&amp;h=75&amp;s=F10BB0544C8108CA5D927D9B0300508A" style="height:85px;"><span class="c-img-border c-img-radius-large"></span></img></a></div><div class="c-span9 c-span-last"><div class="c-abstract"><span class="newTimeFactor_before_abs c-color-gray2 m">2\u5c0f\u65f6\u524d\xa0</span>2\u67086\u65e50\u201424\u65f6,31\u4e2a\u7701(\u81ea\u6cbb\u533a\u3001\u76f4\u8f96\u5e02)\u548c\u65b0\u7586\u751f\u4ea7\u5efa\u8bbe\u5175\u56e2\u62a5\u544a<em>\u65b0\u589e\u786e\u8bca</em>\u75c5\u4f8b<em>11\u4f8b</em>,\u5176\u4e2d\u5883\u5916\u8f93\u5165\u75c5\u4f8b10\u4f8b(\u4e0a\u6d773\u4f8b,\u5317\u4eac2\u4f8b,\u6c5f\u82cf2\u4f8b,\u5e7f\u4e1c2\u4f8b,\u6e56\u53571\u4f8b),<em>\u672c\u571f</em>\u75c5\u4f8b...</div><style>.user-avatar {\n\tdisplay: flex;\n\tflex-direction: row;\n\talign-items: center;\n\tjustify-content: flex-start;\n}</style><div class="f13 c-gap-top-xsmall se_st_footer user-avatar"><a class="c-showurl c-color-gray" href="http://www.baidu.com/link?url=aFWvNvggPt55DjQYg0nddtvbzSWJFO7f1lYwpUA0LqSqfessziVH4YaOi8_t5WNwQ9WhyCpmbICiAjhrsK_BI_" style="text-decoration:none;position:relative;" target="_blank">news.bjd.com.cn/2021/02/07/482...</a><div class="c-tools c-gap-left" data-tools='{"title":"31\u7701\u533a\u5e02\u65b0\u589e\u786e\u8bca\u75c5\u4f8b11\u4f8b,\u5176\u4e2d\u672c\u571f\u75c5\u4f8b1\u4f8b_\u4eac\u62a5\u7f51","url":"http://www.baidu.com/link?url=aFWvNvggPt55DjQYg0nddtvbzSWJFO7f1lYwpUA0LqSqfessziVH4YaOi8_t5WNwQ9WhyCpmbICiAjhrsK_BI_"}' id="tools_4411860119102395523_4"><i class="c-icon f13">\ue62b</i></div><span class="c-icons-outer"><span class="c-icons-inner"></span></span><style>.snapshoot, .snapshoot:visited {\n        color: #9195A3!important;\n    }\n    .snapshoot:active, .snapshoot:hover {\n        color: #626675!important;\n    }</style><a class="m c-gap-left c-color-gray kuaizhao snapshoot" data-click="{'rsv_snapshot':'1'}" href="http://cache.baiducontent.com/c?m=uAVjNMc8YZlbfSx9_ZNe3SmH2gvS6v7p8xPSNW0tujV5pEx-8wqN9BZswmcEwt9BJFKT8SX2TXN8tVNfQ2p5pzcJ_TQh8psgAjh0JwQGaiXizR0BVC1YYjuIqrOE05WQNkDGMGo5_ZaR_n-lM2gmGDCtju-KhjjhMJdrTGmoL8N-XvgsqRe6ffRpTxUAFkpd0w833G7zVpeicu3TvhuupDml_4SqLxp3ThWacpNGJSDWMglXCyu_IR83V7JVsO0P&amp;p=8b2a9753839411a058e8dd621749&amp;newp=833dc64ad4945bb90ebd9b7e085792695912c10e36d6c44324b9d71fd325001c1b69e3b823281603d4c6786c15e9241dbdb239256b5577ad8d9e&amp;s=45c48cce2e2d7fbd&amp;user=baidu&amp;fm=sc&amp;query=31%CA%A1%C7%F8%CA%D0%D0%C2%D4%F6%C8%B7%D5%EF11%C0%FD+%B1%BE%CD%C11%C0%FD&amp;qid=caf502ca0034dd39&amp;p1=4" target="_blank">\u767e\u5ea6\u5feb\u7167</a></div></div></div></div>]

# http://www.baidu.com/baidu?cl=3&amp;tn=SE_baiduhomet8_jmjb7mjw&amp;rsv_dl=fyb_top&amp;fr=top1000&amp;wd=31%CA%A1%C7%F8%CA%D0%D0%C2%D4%F6%C8%B7%D5%EF11%C0%FD%20%B1%BE%CD%C11%C0%FD

# https://www.baidu.com/detail?b=1&amp;c=513&amp;w=31%CA%A1%C7%F8%CA%D0%D0%C2%D4%F6%C8%B7%D5%EF11%C0%FD%20%B1%BE%CD%C11%C0%FD

# https://baijiahao.baidu.com/s?id=1690993588487316354&wfr=spider&for=pc
# https://baijiahao.baidu.com/s?id=1691000047256628177&wfr=spider&for=pc
