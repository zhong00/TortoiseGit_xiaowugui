#-*-coding:utf-8-*-
__author__ = 'zhonglingling'

from urllib import request
from urllib import parse

class Connect(object):
    def __init__(self,url,start):
        self.url = url
        self.start = start


    @property
    def get_html(self):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        values = {
            'start': self.start,
            'limit':'20'
        }
        headers = {'User-Agent':user_agent}
        data = bytes(parse.urlencode(values),encoding='utf-8')
        #print(data,headers)
        #try:
        req = request.Request(self.url,data,headers)
        #print("1")
        res = request.urlopen(req)
        #print("2")
        mm = res.read()
        #print (res.status)
        res.close()
        return mm

        #except ,e:
            # print(e.message)
            # return False

if __name__=="__main__":
    print(Connect("https://movie.douban.com/subject/4920389/comments",3).get_html)