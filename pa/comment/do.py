#-*- coding:utf-8 -*-
__author__ = 'zhonglingling'
import comment.connect,comment.save
x=0
while x<400:
    douban = comment.connect.Connect()
    douban.getItems("https://movie.douban.com/subject/4920389/comments","comments","comment-item","votes",1000,x)
    s = comment.connect.CommentInfo().buildJson(douban.filetedItems)
#print(douban.filetedItems)
    comment.save.writeToFile(s)
    x+=20