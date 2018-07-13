#-*-coding:utf-8-*-
__author__ = 'zhonglingling'

from bs4 import BeautifulSoup

class ParseHtml(object):
    def __init__(self,html,level1,level2,level3,votes):
        self.soup = BeautifulSoup(html)
        self.level1 = level1
        self.level2 = level2
        self.level3 = level3
        self.votes = votes
        self._itemlist = []

    @staticmethod
    def get_ele_by_id(el,id):
        return el.find(id=id)

    @staticmethod
    def get_ele_by_class(el,classname):
        return el.findAll(class_=classname)

    @property
    def _get_level1(self):
        lev1 = self.get_ele_by_id(self.soup,self.level1)
        #print("get level1",lev1)
        return lev1

    @property
    def _get_level2(self):
        lev2 = self.get_ele_by_class(self._get_level1,self.level2)
        #print("get level2",lev2)
        return lev2

    @property
    def get_level3(self):
        try:
            for i in self._get_level2:
                #print("i",i)
                if int(self.get_ele_by_class(i,self.level3)[0].string) > self.votes:
                    self._itemlist.append(i)
                    #print("8888888888888888itemlist",len(self._itemlist),self._itemlist)
            return self._itemlist
        except:
            return False

