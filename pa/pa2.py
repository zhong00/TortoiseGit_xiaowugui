#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zhonglingling'

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
# for item in items:
#     try:
#         c.execute(c.buildInsert("movie",["title","region","director","actors","rate"],
#               [item['data-title'],item['data-region'],item['data-director'],item['data-actors'],item['data-rate']]))
#     except KeyError:
#         continue

print(c.get_records("movie",10))


