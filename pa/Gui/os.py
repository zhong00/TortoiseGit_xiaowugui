#-*-coding:utf-8-*-
__author__ = 'zhonglingling'

#os 常用方法
import os
import time

#返回当前工作目录
print(os.getcwd())

#改变工作目录
os.chdir("E:/TortoiseGit_xiaowugui/pa/autotest")
print(os.getcwd())

#返回指定路径(例子是当前目录）下的所有文件和目录
print(os.listdir(os.curdir))

#新建文件
fp = open("test.txt",'w')
time.sleep(3)
fp.close()
time.sleep(3)
#删除文件
os.remove('test.txt')

#os.path常有方法

#指定文件是否存在
print(os.path.exists("1.log"))

#是否存在指定文件夹
print(os.path.isdir("1.log"))

#是否存在指定文件
print(os.path.isfile("1.log"))

if not os.path.exists("t1"):
    os.mkdir("t1")
