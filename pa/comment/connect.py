__author__ = 'zhonglingling'
from urllib import request
from bs4 import BeautifulSoup

class Connect(object):
    def __init__(self):
        self.data = None
        self.soup = None
        self.bigItem = None
        self.items = None
        self.filetedItems = []

    def urlopen(self,url):
        res = request.urlopen(url)
        self.data = res.read()
        res.close()

    def getItemById(self,id):
        self.soup = BeautifulSoup(self.data)
        print(self.soup)
        self.bigItem = self.soup.find_all(id=id)
        print(self.bigItem)

    def getItemByClass(self,classname):
        self.items = self.bigItem[0].find_all(class_=classname)
        print(self.items)

    def filterItems(self):
        for i in self.items:
            if int(i.find_all(class_='votes').string())>100:
                self.filetedItems.push(i)
        print(self.filetedItems)


if __name__== "__main__":
    a =Connect()
    a.urlopen("https://movie.douban.com/subject/4920389/comments?start=0&limit=20&sort=new_score&status=P&percent_type=")
    a.getItemById("comments")
    a.getItemByClass("comment-item")
    a.filetedItems()