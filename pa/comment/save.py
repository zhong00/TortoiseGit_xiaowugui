#-*- coding:utf-8 -*-
__author__ = 'zhonglingling'

import random
from datetime import datetime

def filename():
    now = datetime.now()
    strNow = now.strftime('%Y%m%d%H%M%S')
    strNow += str(random.randint(10,99))
    #print(strNow)
    return strNow+".json"

def writeToFile(content):
    name = filename()
    try:
        f = open('2018041919525971.json','a',encoding='utf-8')
        f.write(content)
    except:
        print("出错了")
    finally:
        f.close()

if __name__=="__main__":
    writeToFile("jjjjjjj")
