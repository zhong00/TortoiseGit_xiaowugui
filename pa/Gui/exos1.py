#-*-coding:utf-8-*-
__author__ = 'zhonglingling'

import time,os,re

print(int(time.time()))
print(time.strftime("%Y%m%d%H%M%S"))

print(os.getcwd())
os.chdir(r"E:\TortoiseGit_xiaowugui\pa\autotest")
print(os.getcwd())

lista = os.listdir(os.curdir)
print(len(lista))
for i in lista:
    if re.match('\d+',i):
        os.remove(i)

for m in range(2):
    print (time.strftime("%Y%m%d%H%M%S"))
    f = open(time.strftime("%Y%m%d%H%M%S"),'w')
    f.close()
    time.sleep(2)
    print(time.strftime("%Y%m%d%H%M%S"))
    f = open(time.strftime("%Y%m%d%H%M%S"),'w')
    f.close()
    time.sleep(1)

if not os.path.exists("t1"):
    os.mkdir("t1")
if not os.path.exists(r"aa\bb"):
    os.makedirs(r"aa\bb")
os.chdir(r"aa\bb")
if not os.path.exists("ccc"):
    os.mkdir("ccc")