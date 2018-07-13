#-*-coding:utf-8-*-
__author__ = 'zhonglingling'
from mysql import connector

# 连接数据库
try:
    conn = connector.Connect(
    host='127.0.0.1',
    port='3306',
    user='root',
    password='',
    database='rdb',
    charset='utf8'
)
except connector.Error as e:
    print("connect fail",e)
cursor = conn.cursor()

#select
try:
    sql_query = 'select * from user_define'
    cursor.execute(sql_query)
    for i,name,passwd in cursor:
        print(i,name,passwd)
except connector.Error as e:
    print("select fail",e)

#insert
try:
    sql_query = "insert into user_define(user_login,user_passwd) VALUES('wew','weq')"
    cursor.execute(sql_query)
except connector.Error as e:
    print("insert fail",e)
finally:
    cursor.close()
    conn.close()