#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#__author__ = 'zhonglingling'

import requests
from bs4 import BeautifulSoup
from mysqlCon import MySQLConn

r = requests.get("https://movie.douban.com/")
print(r.status_code)
soup = BeautifulSoup(r.content)
items = soup.find_all("li","ui-slide-item")
print(len(items))

class server:
    IP="bdm257820613.my3w.com"
    Port=3306
    dbName = "bdm257820613_db"
    User="bdm257820613"
    Password="q1w2e3r4t5"

c =MySQLConn(server())
c.connection()
for item in items:
    if(not hasattr(item,'data-title')):
        print("break")

        item['data-title'] = " "
    print(item['data-title'],item['data-region'],item['data-director'],item['data-actors'],item['data-rate'])

    c.insert("movie",["title","region","director","actors","rate"],[item['data-title'],item['data-region'],item['data-director'],item['data-actors'],item['data-rate']])
# s = c.get_records("movie",0)
# for i in s:
#     for j in i:
#         print(j)

c.insert("Persons",["FirstName","LastName"],["miao","wang"])
c.close()
