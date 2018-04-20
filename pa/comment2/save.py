#-*- coding:utf-8 -*-
__author__ = 'zhonglingling'

import random,os
from datetime import datetime



def writeToFile(file,method,content):
    try:
        f = open(file,method,encoding='utf-8')
        f.write(content)
    except:
        print("出错了")
    finally:
        f.close()

if __name__=="__main__":
    writeToFile("jjjjjjj")
