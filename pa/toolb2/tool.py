#-*-coding:utf-8-*-
__author__ = 'zhonglingling'

from toolb2.log import *
import yaml
from tkinter import *
from mysql import connector

class MySQLConn:
    def __init__(self):
        self.conn = None

    @property
    def config(self):
        try:
            f = open('tool.yaml','r')
            y = yaml.load(f)
            config_db = y['db']
            db = {}
            db['host'] = config_db['host']
            db['port'] = config_db['port']
            db['database'] = config_db['database']
            db['user'] = config_db['user']
            db['password'] = config_db['password']
            db['charset'] = config_db['charset']
            logger.info('config success')
            return db
        except:
            logger.error('config error')
        finally:
            f.close()

    @property
    def connection(self):
        if self.conn is None :
            try:
                db = self.config
                self.conn = connector.connect(**db)
                logger.info('connect success')
                return self.conn
            except:
                logger.error('connect error')
                return None

    def update(self,input1,input2):
        try:
            int(input1)
        except:
            print("必须为数字")
            return False
        if (input1 and input2):
        #疑问input1的类型是
            sql = "update setting set num="+str(input1)+",str='"+input2+"' where id=1"
            try:
                co = self.connection #疑问self.connection 是none
                c = co.cursor()
                c.execute(sql)
                co.commit()
                logger.info('update success')
            except connector.Error as e:
                logger.error('update fail',e)
            finally:
                c.close()
                co.close()

    def select(self):
        sql = "select * from setting where id=1"
        try:
            co = self.connection
            c = co.cursor()
            c.execute(sql)
            return c.fetchone()
        except connector.Error as e:
            print('select fail',e)
        finally:
            c.close()
            co.close()

class Show:
    def __init__(self):
        self.E1 = None
        self.E2 = None
        self.show()

    def show(self):
        root = Tk()

        #标题
        root.wm_title('配置工具')
        #主体
        Label(text='参数设置').grid(row=0)
        Label(text='数字参数').grid(row=1)
        self.E1 = Entry()
        self.E1.grid(row=1,column=1)
        Label(text='字符串参数').grid(row=2)
        self.E2 = Entry()
        self.E2.grid(row=2,column=1)
        Button(text='保存',command=lambda :MySQLConn().update(self.E1.get(),self.E2.get())).grid(row=3)
        Button(text='刷新',command=self.get).grid(row=3,column=1)
        root.mainloop()

    def get(self):
        t = MySQLConn().select()
        s = StringVar()
        s.set(t[1])
        self.E1['textvariable'] = s
        s = StringVar()
        s.set(t[2])
        self.E2['textvariable'] = s

    def set(self,s1,s2):
        pass

if __name__=='__main__':

    Show()

    # try:
    #     conn = connector.connect(
    #         host='127.0.0.1',
    #         port=3306,
    #         database='rdb',
    #         user='root',
    #         password='',
    #         charset='utf8'
    #     )
    #     print("0#",type(conn))
    #     cursor = conn.cursor()
    #     cursor.execute("update setting set num=55,str='55' where id=1")
    #     print(cursor.rowcount)
    #     conn.commit()
    #     print("1#",type(conn))
    #     #cursor.close()
    #     #cursor = conn.cursor()
    #     cursor.execute("delete from setting where id=0")
    #     #cursor.execute('insert into setting(num,str) VALUES (32,23)')
    #     conn.commit()
    #     print("3#",type(conn))
    #     cursor.execute('select * from setting')
    #     mm = cursor.fetchone()
    #     print(type(mm),mm)
    #     cursor.close()
    #     conn.close()
    # except connector.Error as e:
    #     print("wewe",e)