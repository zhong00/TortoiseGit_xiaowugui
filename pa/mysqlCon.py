# -*- coding:utf-8 -*-
__author__ = 'zhonglingling'
import mysql.connector
class MySQLConn(object):
    def __init__(self,dbServer):
        self.dbServer = dbServer
        self._conn =None

    def connection(self):
        if(self.dbServer):
            self._conn = mysql.connector.connect(host=self.dbServer.IP,
                                    port=self.dbServer.Port,
                                    database=self.dbServer.dbName,
                                    user=self.dbServer.User,
                                    password=self.dbServer.Password,
                                    charset ="utf8")
            return self._conn

    def execute(self,sql):
        try:
            c = self._conn.cursor()
            c.execute(sql)
            self.connection.commit()
        except mysql.connector.Error as e:
            print(e)
        finally:self.connection.close()

    def _buildSelect(self,table,limit=0):
        sql = "SELECT * FROM "+table
        if limit>0:
            sql +="limit "+str(limit)
        return sql

    def get_records(self,table,limit):
        self.execute(self._buildSelect(table,limit))

    def _buildInsert(self,table,cols,values):
        return "INSERT INTO "+table+" ("+",".join(cols)+") "+'VALUES("'+'","'.join(values)+'");'

    def insert(self,table,cols,values):
        self.execute(self._buildInsert(table,cols,values))

    def _close(self):
        self.connection.