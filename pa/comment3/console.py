#-*-coding:utf-8-*-
__author__ = 'zhonglingling'
import comment3.GetInit,comment3.connect,comment3.parse,comment3.BuildJson
import random,datetime

class startMelody(object):
    def __init__(self):
        init = comment3.GetInit.get_init()
        self.url = init.get_url
        self.limit = init.get_limit
        self.start = 0
        self.page = 1
        self.level1 = init.get_level1
        self.level2 = init.get_level2
        self.level3 = init.get_level3
        self.votes = init.get_votes

        self.itemlist = []
        self.content = ""
        self.file = None

        self.control()

    def control(self):
        while self.page<11:
            print("page",self.page)
            self.content = ""
            self.start = (self.page-1) * self.limit
            self.get_itemlist()
            if self.itemlist and len(self.itemlist)>0 :
                if self.page ==1:
                    self.create_file()
                    self.content += "["
                self.content += comment3.BuildJson.BuildJson(self.itemlist).build
                if self.page ==1:
                    print("page111111111111111111111111111",self.content)
                    self.content = self.content.replace("[,","[")
                    print("page22211111111111111111111111",self.content)
                self.write_file()
            self.page +=1
            print("page",self.page)
        self.content ="]"
        self.write_file()

    def get_itemlist(self):
        self.html = comment3.connect.Connect(self.url,self.start).get_html
        print("html:",self.html)
        if self.html:
            self.itemlist = comment3.parse.ParseHtml(self.html,self.level1,self.level2,self.level3,self.votes).get_level3
            print("cosole的itemlist",self.itemlist)
        else :
            print("can not get html,quit")

    def create_file(self):
        now = datetime.datetime.now().strftime('%y%m%d%H%M%S')
        now += str(random.randint(10,99))
        now += ".json"
        self.file = now
        print(self.file)

    def write_file(self):
        if self.page>1:
            fp = open(self.file, 'a', encoding='utf-8')
        else :
            fp = open(self.file, 'w',encoding='utf-8')
        fp.write(self.content)
        fp.close()

if __name__ == "__main__":
    startMelody()
