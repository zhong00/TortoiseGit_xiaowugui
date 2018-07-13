#-*-coding:utf-8-*-
__author__ = 'zhonglingling'
from tkinter import *
from mysql import connector
import yaml,logging

#log
logger = logging.getLogger()
logger.setLevel(logging.INFO)

fh = logging.FileHandler('tool.log',mode='a')
fh.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

format = logging.Formatter('%(asctime)s-%(filename)s-line%(lineno)d-[%(levelname)s]-%(message)s')
fh.setFormatter(format)
ch.setFormatter(format)
logger.addHandler(fh)
logger.addHandler(ch)

def getYamlValue():
    try:
        f = open('tool.yaml')
        x = yaml.load(f)
        db = x['db']
        config = {}
        config['host']=db['host']
        config['port']=db['port']
        config['user']=db['user']
        config['password']=db['password']
        config['database']=db['dbname']
        config['charset']=db['charset']
        logger.info('read config success')
        return config
    except:
        return None
    finally:
        f.close()
#print(getYamlValue())

def select():
    try:
        conn = connector.connect(**getYamlValue())  #一个*表示接收的参数作为元祖来处理，两个*表示接收的参数作为字典来处理
        cursor = conn.cursor()
        print("connect success")

    except connector.Error as e:
        print("connect fail",e)

    try:
        mysql_query = "select * from user_define"
        cursor.execute(mysql_query)
        L3['text']=""
        for i,n,p in cursor:
            if n and p:
                L3['text']+=n
                L3['text']+="\n"
    except connector.Error as e:
        print("select fail",e)
    finally:
        cursor.close()
        conn.close()

def insert(name,passwd):
    try:
        conn = connector.connect(**getYamlValue())
        cursor = conn.cursor()
        print("connect success")

    except connector.Error as e:
        print("connect fail",e)
    try:
        mysql_query = "insert into user_define(user_login,user_passwd) values ('"+name+"','"+passwd+"')"
        cursor.execute(mysql_query)
    except connector.Error as e:
        print("insert fail",e)
    finally:
        cursor.close()
        conn.close()

class some:
    def __init__(self):
        self.a = 'a'
    def pr(self,b):
        print(self.a,b)
s = some()
root = Tk()
Label(root,text='账号：').grid(row=0,sticky=W)
E1 = Entry(root)
E1.grid(row=0,column=1,sticky=E)
Label(root,text='密码:').grid(row=1,sticky=W)
E2 = Entry(root)
E2.grid(row=1,column=1,sticky=E)
Button(root,text='登录',command = lambda :s.pr(E1.get())).grid(row=2,sticky=E) #command 带参数的函数需要用lambda
Button(root,text='显示',command = select).grid(row=2,column=1,sticky=E)

L3 = Label(root)
L3.grid(row=3)
root.mainloop()



