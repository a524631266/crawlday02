#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Zhangll
@software: PyCharm Community Edition
@time: 2016/9/25 22:35
"""
#aimto download data from www.mailiangwang.com/biz/list 买粮网
#用css路径去获取元素的时候很容易出现错误，当没有元素的时候，所以考虑json
import requests
from bs4 import BeautifulSoup


def get_search_list(keyword=None,pageid=1):
    url="http://www.mailiangwang.com/biz/list"
    payload={'keyword':keyword,'pageid':pageid}
    response=requests.get(url,payload)
    print response.url
    print response.status_code
    soup=BeautifulSoup(response.text,'lxml')#parse
    # body > div.wrap > div.merchantList > div.p_dataList > div:nth-child(3) > span.n1 > a
    names=soup.select("body > div.wrap > div.merchantList > div.p_dataList > div.p_dataItem > span.n1 > a")
    print names
    capitals=soup.select("body > div.wrap > div.merchantList > div.p_dataList > div.p_dataItem > span.n3")
    print capitals
    addrs=soup.select("body > div.wrap > div.merchantList > div.p_dataList > div.p_dataItem > span.n5")
    categorys=soup.select("body > div.wrap > div.merchantList > div.p_dataList > div.p_dataItem > span.n6")


    with open('data.txt','w') as f:
        f.write('公司名称|注册资本|公司地址|主营品类\n')
        #要获取属性值
        for name,capital,addr,category in zip(names,capitals,addrs,categorys):
            name=name.get('title').strip()#strip() clear backnum
            # print name
            capital=capital.text
            addr=addr.text
            category=category.text

            data=[name,capital,addr,category,'\n']`
            # print '|'.join(data)
            f.write('|'.join(data).encode('utf-8'))
            print '写入成功'

if __name__=='__main__':
    get_search_list(u'玉米',pageid=1)