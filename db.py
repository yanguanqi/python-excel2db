# /usr/bin
# -*- coding=utf-8 -*-

import sqlite3


class db(object):

    def __init__(self, dbPath=""):
        self.path = dbPath
        self.conn = sqlite3.connect(self.path)
        self.cur = self.conn.cursor()

    def createtable(self, name="", colname=[], coltype=[]):
        fields = "";
        if len(colname) == 0:
            return
        if len(coltype) != len(colname):
            for index in range(0, len(colname)):
                if colname[index].strip() == "":
                    continue
                fields += colname[index] + " text,"
        else:
            for index in range(0, len(colname)):
                if colname[index].strip() == "":
                    continue
                fields += colname[index] + coltype[index] + ","
        try:
            self.conn.execute("create table " + name + " (" + fields[:-1] + ")")
        except Exception as e:
            print("Exception location:" + name + "_" + str(e))

    def importdata(self, name="", datas=[]):
        if name == "TJ1_DJWDQ_MXYSB":
            print("djw")
        if len(datas) == 0:
            return

        for sheet in datas.values():
            for data in sheet.values():
                sqlkey = '';
                for col in data:
                    if isinstance(col, str):
                        sqlkey += "'" + col.strip() + "',"
                    else:
                        sqlkey += str(col) + ","

                try:
                    sql = "INSERT INTO " + name + " VALUES (" + sqlkey[:-1] + ")"

                    self.conn.execute(sql)
                except Exception as e:

                    print("Exception location:" + name + "_" + str(e))

        print("Insert datas to " + name + " completed!")

    def close(self):
        self.conn.close()
