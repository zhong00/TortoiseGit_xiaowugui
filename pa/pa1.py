#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zhonglingling'

from urllib import request

import requests,mysql.connector
from bs4 import BeautifulSoup

with request.urlopen("https://movie.douban.com/") as f:
    data = f.read()
    # print("status:",f.status,f.reason)
    # for k,v in f.getheaders():
    #     print("%s:%s" %(k,v))
    # print("Data:",data.decode("utf-8"))
r = requests.get("https://movie.douban.com/")
print(r.status_code)
soup = BeautifulSoup(r.content)
items = soup.find_all("li","ui-slide-item")
print(len(items))
with open("movie.txt","w") as f:
    for item in items:
        # print("这个item",item)
        # print("____________________")
        try:
            f.write("%s,地区:%s,导演:%s,演员:%s,评分:%s\r\n" %(item["data-title"],item["data-region"],item["data-director"],item["data-actors"],item["data-rate"]))
        except KeyError:
            continue

def conMysql(host,user,passwd,dbName):
    conn = mysql.connector.connect(user,passwd,dbName)
    cursor = conn.cursor()