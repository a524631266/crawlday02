#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Zhangll
@software: PyCharm Community Edition
@time: 2016/9/26 0:20
"""
import requests
import json


def get_translate_data(word=None):
    url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    payload={'type':'AUTO','i':word,'doctype':'json','xmlVersion':'1.8','keyfrom':'fanyi.web','ue':'UTF-8','action':'FY_BY_ENTER','typoResult':'true'}
    response=requests.post(url,data=payload)
    content=json.loads(response.text)
    # print json.dumps(content,encoding='utf-8',ensure_ascii=False)
    print content['translateResult'][0][0]['tgt']

if __name__=='__main__':
    get_translate_data('橘子')