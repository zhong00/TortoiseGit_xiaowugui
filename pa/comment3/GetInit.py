#-*-coding:utf-8-*-
__author__ = 'zhonglingling'
import configparser

class get_init(object):
    def __init__(self):
        self._url = ""
        self._limit = 0
        self._level1 = ""
        self._level2 = ""
        self._level3 = ""
        self._votes = 0
        self.parse_init()

    def parse_init(self):
        cf = configparser.ConfigParser()
        cf.read('config.ini')
        self._url = cf.get("address","url")
        self._limit = cf.getint("address","limit")
        self._level1 = cf.get("parse","level1")
        self._level2 = cf.get("parse","level2")
        self._level3 = cf.get("parse","level3")
        self._votes = cf.getint("parse","para")

    @property
    def get_url(self):
        return self._url

    @property
    def get_limit(self):
        return self._limit

    @property
    def get_level1(self):
        return self._level1

    @property
    def get_level2(self):
        return self._level2

    @property
    def get_level3(self):
        return self._level3

    @property
    def get_votes(self):
        return self._votes


if __name__ =="__main__":
    a = get_init()
    print(a.get_url)
    print(a.get_limit)
    print(a.get_level1)
    print(a.get_level2)
    print(a.get_level3)
    print(a.get_votes)
