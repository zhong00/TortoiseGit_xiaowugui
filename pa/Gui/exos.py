#-*-coding:utf-8-*-
__author__ = 'zhonglingling'
import os,time,re

print(int(time.time())) #时间戳取整

print(os.getcwd())#获取当前工作目录
os.chdir(r"E:\TortoiseGit_xiaowugui\pa\autotest")#改变当前脚本工作目录
print(os.curdir)#返回当前目录.

print(os.listdir(os.curdir))
for i in os.listdir(os.curdir):
    if re.match('[0-9]+',i): #re.match从开头匹配，re.search整个匹配，
        os.remove(i)
print(time.strftime("%Y%m%d%H%M%S"))#年月日时分秒
f = open(time.strftime('%Y%m%d%H%M%S'),'w')
f.close()

f = open("test",'r')
content = f.readlines()
print(content)
f.close()

x = open("testw",'w')
for i in content:
    x.write(i)
x.close()