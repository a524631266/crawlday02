#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Zhangll
@software: PyCharm Community Edition
@time: 2016/9/25 23:28
"""
import requests
import json
import pymongo
import time
from bs4 import BeautifulSoup
from multiprocessing import Pool

# client=pymongo.MongoClient('localhost',27017)

#数据库
# sense=client['sense']
#创建表
# url_list=sense['url_list']

client=pymongo.MongoClient('localhost',27017)
sense=client.sense
url_list=sense.url_list1

def get_city():
    # url="http://www.senseluxury.com/destinations/2"
    url="http://www.senseluxury.com/destnav"
    response=requests.get(url)
    # print(response.text)
    soup=BeautifulSoup(response.text,"lxml")
    # lists=soup.find_all('dl','dl-list')
    lists=soup.find_all('a')
    print lists
    # urls=soup.select("div > div > dl.dl-list> dd > a")
    return [list.get("href") for list in lists]
    # for list in lists:
    #         # print(list)   #<a href="/destinations/690" title="坦桑尼亚 度假别墅">坦桑尼亚</a>
    #         ll=list.get("href")
    #         print ll



def get_json_list(city,page=1):
    now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    url="http://www.senseluxury.com/destinations_list/%s" % city.split("/")[-1].strip()
    # url= 'http://www.senseluxury.com/destinations_list/%s?page=%s' % (city.split('/')[-1], page)
    print(city)
    # payload={'page':page,'callback':'jsonp'}
    # respons=requests.get(url,params=payload)
    respons=requests.get(url)
    # print respons.text[6:-1]#http://www.bejson.com/   http://jsoneditoronline.org/ looking the list of json
    wb_data=json.loads(respons.text[1:-1])
    # print wb_data 会出现很多乱码
    # print json.dumps(wb_data,encoding='utf-8',ensure_ascii=False)
    print type(respons.text),type(wb_data)

    for i in wb_data['val']['data']:
        title=i['title']
        url='http://www.senseluxury.com'+i['url']
        server=i['server'].replace('&nbsp;'," ").split()
        memo=i['memo']
        price=i['price']
        address=i['address']
        subject=i['subject']
        data={'title':title,'url':url,'server':server,
              'memo':memo,'price':price,'address':address,'subject':subject,'time':now,'url_num':city.split("/")[-1]}
        print title,url
        url_list.insert_one(data)

if __name__=='__main__':
    # get_json_list(1)
    # print get_city()
    # get_json_list("/483")
    city=get_city()
    print(city)
    #map函数
    pool=Pool(processes=1)
    pool.map(get_json_list,city)
    pool.close()
    pool.join()#主要是用于防止主程序被close前于子进程结束
    # [get_json_list(citys) for citys in city]