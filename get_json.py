#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Zhangll
@software: PyCharm Community Edition
@time: 2016/9/25 23:28
"""
import requests
import json

def get_json_list(page):
    url="http://www.senseluxury.com/destinations_list/85"
    payload={'page':page,'callback':'jsonp'}
    respons=requests.get(url,params=payload)
    print respons.text[6:-1]#http://www.bejson.com/   http://jsoneditoronline.org/ looking the list of json
    wb_data=json.loads(respons.text[6:-1])
    # print wb_data 会出现很多乱码
    print json.dumps(wb_data,encoding='utf-8',ensure_ascii=False)
    print type(respons.text),type(wb_data)

    for i in wb_data['val']['data']:
        title=i['title']
        url='http://www.senseluxury.com'+i['url']
        print title,url

if __name__=='__main__':
    get_json_list(1)