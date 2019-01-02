
from xl import xl
from db import db
import pinyin
import os


def convert():
    path = '.\\data\\提交表格数据\\'
    print(os.path.dirname(path))
    # ex = xl(path)
    # ex.load()
    # sdb = db(dbPath="./data/bim.db")
    # print(pinyin.get_initial(os.path.split(path)[1],delimiter=''))
    # #sdb.createTable()