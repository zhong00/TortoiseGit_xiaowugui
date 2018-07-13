#-*-coding:utf-8-*-
__author__ = 'zhonglingling'

import os,re,time,sys

createLog()
def createLog(path):
    os.chdir(path)
    path = os.getcwd()
    fileList = os.listdir(os.curdir)
    for i in fileList:
        if re.match("\d+\.log",i):
            os.remove(i)
    logName = 1
    while len(os.listdir(os.curdir))<5:
        f = open(str(logName)+".log","w")
        f.close()
        print(logName)
        logName = logName+1

createLog(sys.argv[1])
#/users/log/svc_netbus
# listx = os.listdir('E:/TortoiseGit_xiaowugui/pa/Gui/')
# print listx
# for i in listx:
#     print i
#     if re.match(r'\d\d\.log',i):
#         print "success"
#         os.remove(i)
# num = os.listdir('E:/TortoiseGit_xiaowugui/pa/Gui/')
# x = 1
# while x<50:
#     f = open(str(x)+'.log','w')
#     f.close()
#     time.sleep(2)
#     x = x+1