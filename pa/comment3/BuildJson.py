#-*-coding:utf-8-*-
__author__ = 'zhonglingling'

from bs4 import BeautifulSoup

class BuildJson:
    def __init__(self,list):
        self.list = list
        self.str = ""


    @property
    def build(self):
        for i in self.list:
            #print (i)
            votes = i.find(class_='votes').string
            comment_info = i.find(class_='comment-info')
            name = comment_info.find("a").string
            date = comment_info.find(class_='comment-time')['title']
            try:
                rating = comment_info.find(class_='rating')['title']
            except:
                rating = " "
            try:
                content = i.find("p").string.strip()
            except:
                content = ""
            self.str += ',{"votes":"'+ votes + '","name":"'+name+'","date":"'+date+'","rating":"'+rating+'","content":"'+content+'"}'
        return self.str
