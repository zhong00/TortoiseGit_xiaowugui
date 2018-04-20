#-*- coding:utf-8 -*-
__author__ = 'zhonglingling'
import comment.connect,comment.save
from datetime import datetime
import random

def filename():
    now = datetime.now()
    strNow = now.strftime('%Y%m%d%H%M%S')
    strNow += str(random.randint(10,99))
    #print(strNow)
    return strNow+".json"
x=0
while x<400:
    print("------------------------------------------x=",x)
    douban = comment.connect.Connect()
    if not douban.getItems("https://movie.douban.com/subject/4920389/comments","comments","comment-item","votes",100,x):
        break
    #print(douban.filetedItems)
    if(len(douban.filetedItems) ==0):
        x+=20
        continue
    if x==0:
        file = filename()
        method = "w"
        start = True
    else :
        method = "a"
        start = False
    s = comment.connect.CommentInfo().buildJson(douban.filetedItems,start)
    comment.save.writeToFile(file,method,s)
    x+=20
    print("-----------------------x",x)
#comment.save.writeToFile(file,'a',']')