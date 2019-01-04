# /usr/bin
# -*- coding=utf-8 -*-

import sqlite3


class db(object):

    def __init__(self, dbPath=""):
        self.path = dbPath
        self.conn = sqlite3.connect(self.path)
        self.cur = self.conn.cursor()
        self.colname = {}

    def createtable(self, name="", colname=[], coltype=[]):
        fields = "";
        if len(colname) == 0:
            return
        self.colname[name] = []
        if len(coltype) != len(colname):
            for index in range(0, len(colname)):
                if colname[index].strip() == "":
                    continue
                fields += colname[index] + " text,"
                self.colname[name].append(colname[index])
        else:
            for index in range(0, len(colname)):
                if colname[index].strip() == "":
                    continue
                fields += colname[index] + coltype[index] + ","
                self.colname[name].append(colname[index])
        try:
            self.conn.execute("create table " + name + " (" + fields[:-1] + ")")
        except Exception as e:
            print("Exception location:" + name + "_" + str(e))

    def importdata(self, name="", datas=[]):
        if len(datas) == 0 or len(self.colname[name]) == 0:
            return
        for sheet in datas.values():
            sum = len(sheet.values())
            pro = 0
            newdatas = []
            for data in sheet.values():
                sqlkey = '';
                newdata = []
                pro += 1
                if len(self.colname[name]) >= len(data):
                    newdata.extend(data)
                    for i in range(0, len(self.colname[name]) - len(data)):
                        newdata.append("")
                elif len(self.colname[name]) < len(data):
                    newdata.extend(data[:len(self.colname[name]) - 1])
                    lm = "";
                    for meta in data[len(self.colname[name]):]:
                        lm += meta + ","
                    newdata.append(lm)
                else:
                    newdata.extend(data)
                newdatas.append(newdata)
            try:
                self.conn.executemany("INSERT INTO " + name + " VALUES(" + ("?," * len(self.colname[name]))[:-1] + ")",
                                      newdatas)
                self.conn.commit()
            except Exception as e:
                print("Insert data erro :" + name + "/n" + str(e))
        print("Insert datas to " + name + " completed!")

    def createview(self):
        

    def close(self):
        self.conn.close()
