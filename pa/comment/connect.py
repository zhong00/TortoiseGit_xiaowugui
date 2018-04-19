#-*- coding:utf-8 -*-
__author__ = 'zhonglingling'
from urllib import request
from urllib import parse
from bs4 import BeautifulSoup
from comment.common import *

class Connect(object):
    def __init__(self):
        self.data = None #原始数据
        self.soup = None #原始汤数据
        self.bigItem = None #要用的一大块item
        self.items = None #一类items
        self.filetedItems = [] #筛选投票大于100后的items

    @log
    def urlopen(self,url,begin):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        values = {
            'start':begin,
            'limit':'20'
        }
        headers = {'User-Agent':user_agent}
        data = bytes(parse.urlencode(values),encoding='utf-8')
        req = request.Request(url,data,headers)

        res = request.urlopen(req)
        self.data = res.read()
        print(res.status,res.reason)
        # for k,v in res.getheaders():
        #       print('%s:%s' %(k,v))
        #print('Data',self.data.decode('utf-8'))
        res.close()

    @log
    def getItemById(self,id):
        self.soup = BeautifulSoup(self.data)
        #printInfo("本汤",self.soup)
        self.bigItem = self.soup.find_all(id=id)
        #printInfo("本大段",self.bigItem)

    @log
    def getItemsByClass(self,classname):
        self.items = self.bigItem[0].find_all(class_=classname)
        #printInfo("所有类的items",self.items)

    @log
    def filterItems(self,classname,num):
        for i in self.items:
            if int(i.find(class_=classname).string)>num:
                self.filetedItems.append(i)
        #printInfo("符合条件的item列表",self.filetedItems)
        #self.filetedItems = "".join(self.filetedItems)

    def getItems(self,url,id,classname,subname,num,begin):
        self.urlopen(url,begin)
        self.getItemById(id)
        self.getItemsByClass(classname)
        self.filterItems(subname,num)

class CommentInfo(object):
    def __init__(self):
        self.votes = None
        self.name = None
        self.time = None
        self.rating = None
        self.content = None

    def getInfo(self,i):
        self.votes = i.find(class_='votes').string
        commentInfo = i.find(class_='comment-info')
        self.name = commentInfo.find("a").string
        self.rating = commentInfo.find(class_='rating')['title']
        self.time = commentInfo.find(class_='comment-time')['title']
        self.content = i.find("p").string.strip()

    def buildJson(self,list):
        m = "["
        for i in list:
            self.getInfo(i)
            m += '{"votes":"'
            m += self.votes
            m += '","name":"'
            m += self.name
            m += '","rating":"'
            m += self.rating
            m += '","time":"'
            m += self.time
            m += '","content":"'
            m += self.content
            m += '"},'
        m = m[0:-1]
        m +="]"
        return m

if __name__== "__main__":
    #a =Connect()
    #a.urlopen("https://movie.douban.com/subject/4920389/comments?")
    # a.getItemById("comments")
    # a.getItemsByClass("comment-item")
    # a.filterItems('votes',100)
    #a.getItems("https://movie.douban.com/subject/4920389/comments?start=0&limit=20&sort=new_score&status=P&percent_type=","comments","comment-item","votes",1000)
    url = 'https://movie.douban.com/subject/4920389/comments'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {
        'start':'0',
        'limit':'20'
    }
    headers = {'User-Agent':user_agent}
    data = bytes(parse.urlencode(values),encoding='utf-8')
    req = request.Request(url,data)
    response = request.urlopen(req)
    the_page = response.read()
    print(the_page)
