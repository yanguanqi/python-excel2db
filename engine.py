import os

import pinyin

from db import db
from xl import xl


def convert():
    path = '.\\data\\提交表格数据\\'
    tjs = os.listdir(path)
    sdb = db(dbPath="./data/bim.db")
    sum = 0
    for tj in tjs:
        xlss = findexcel(path + tj + "\\")
        sum += len(xlss)
        for xls in xlss:
            ex = xl(xls)
            ex.load()
            name = pinyin.get_initial(os.path.split(xls)[1][:len(os.path.splitext(xls)[1]) * -1], delimiter='').upper()
            if name.find("MXYSB") != -1:
                name = tj.upper() + "_" + name.replace("MXYSB", "") + "_MXYSB"
            else:
                name = tj.upper() + "_" + name + "_JLYSB"
            sdb.createtable(name, ex.colName)
            sdb.importdata(name, ex.data)
    sdb.close()
    print("Create " + str(sum) + " tables, completed!")


def findexcel(path):
    results = []
    if os.path.isfile(path):
        if os.path.splitext(path):
            results.append(path)
    else:
        for sub in os.listdir(path):
            results.extend(findexcel(path + "\\" + sub))
    return results
