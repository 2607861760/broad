# -*- coding: utf-8 -*-
import xlrd
from openpyxl import load_workbook


def read_excel(dataIVlist,filter,QCData):
    # sheet的名称，行数，列数
    def data(content):
        oap = []
        # 循环获取所需行的序列号
        for j in range(len(dataIVlist[1])):
            if dataIVlist[1][j] == content:  # ,"OA Function Peak ac" content
                oap.append(j)
        # 获取对应的数据，存放在lists和list2中
        items = filter[oap[0]-3]
        items2 = filter[oap[0]]
        sumData = []
        for itemIndex in range(len(items)):
            sum = float(items[itemIndex]) - float(items2[itemIndex]) * QCData
            sumData.append(sum)
        return sumData

    return data("OA Function Peak ac"),data("OA Function Peak in")