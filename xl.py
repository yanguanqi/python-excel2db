# /usr/bin
# -*- coding=utf-8 -*-

import xlrd


class xl(object):

    def __init__(self, name=""):
        self.name = name

    def load(self):
        rd = xlrd.open_workbook(filename=self.name)
        self.data = {}
        self.colName = [];
        for index in range(0, len(rd.sheet_names())):
            sheet = rd.sheet_by_index(index)
            # print("sheet:" + sheet.name)
            # print("col:" + str(sheet.ncols), "row:" + str(sheet.nrows))
            self.data[sheet.name] = {}
            if sheet.ncols >= 1 & sheet.nrows >= 1:
                for col in sheet.row_values(0):
                    self.colName.append(col)
                for rowIndex in range(1, sheet.nrows):
                    row = sheet.row_values(rowIndex)
                    self.data[sheet.name][rowIndex - 1] = row

    def asyncLoad(self):
        rd = xlrd.open_workbook(filename=self.name)
