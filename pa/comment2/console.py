#-*- coding:utf-8 -*-
__author__ = 'zhonglingling'
import comment2.connect,comment2.save
from datetime import datetime
import random

def filename():
    now = datetime.now()
    strNow = now.strftime('%Y%m%d%H%M%S')
    strNow += str(random.randint(10,99))
    #print(strNow)
    return strNow+".json"
x=0
file = filename()
while x<400:
    print("------------------------------------------x=",x)
    douban = comment2.connect.Connect()
    if not douban.getItems("https://movie.douban.com/subject/4920389/comments","comments","comment-item","votes",100,x):
        break
    #print(douban.filetedItems)
    if(len(douban.filetedItems) ==0):
        x+=20
        continue
    if x==0:
        method = "w"
        start = True
    else :
        method = "a"
        start = False
    s = comment2.connect.CommentInfo().buildJson(douban.filetedItems,start)
    comment2.save.writeToFile(file,method,s)
    x+=20
    print("-----------------------x",x)
comment2.save.writeToFile(file,'a',']')