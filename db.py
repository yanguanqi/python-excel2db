# /usr/bin
# -*- coding=utf-8 -*-

import sqlite3

class db(object):

    def __init__(self,dbPath=""):
        self.path = dbPath
        self.conn =  sqlite3.connect(self.path)
        self.cur = self.conn.cursor()

    def createTable(self,name="",colName = [],colType=[]):
        fields="";
        for index  in range(0,len(colName)):
            fields  += colName[index] +  colType[index]+","
        self.conn.execute("create table "+name +"("+fields[:-1]+")")


