# -*- coding:utf-8 -*-
__author__ = 'zhonglingling'
import mysql.connector
class MySQLConn(object):
    def __init__(self,dbServer):
        self.dbServer = dbServer
        self._conn =None
        self._cursor = None

    def connection(self):
        if(self.dbServer):
            try:
                self._conn = mysql.connector.connect(host=self.dbServer.IP,
                                        port=self.dbServer.Port,
                                        database=self.dbServer.dbName,
                                        user=self.dbServer.User,
                                        password=self.dbServer.Password,
                                        charset ="utf8")
            except mysql.connector.Error as e:
                print("connect",e)
            self._cursor = self._conn.cursor()

    def execute(self,sql):
        try:
            self._cursor.execute(sql)
            self._conn.commit()
        except mysql.connector.Error as e:
            print("excute",e)

    def _buildSelect(self,table,limit=0):
        sql = "SELECT * FROM `"+table+"`"
        if limit>0:
            sql +=" limit "+str(limit)
        sql +=";"
        print("build",sql)
        return sql

    def get_records(self,table,limit):
        self._cursor.execute(self._buildSelect(table,limit))
        list = self._cursor.fetchall()
        # for i in list:
        #     print(i)
        return list

    def _buildInsert(self,table,cols,values):
        m = "INSERT INTO "+table+" ("+",".join(cols)+") "+'VALUES("'+'","'.join(values)+'");'
        print(m)
        return m

    def insert(self,table,cols,values):
        self.execute(self._buildInsert(table,cols,values))

    def close(self):
        self._conn.close()