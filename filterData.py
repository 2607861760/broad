import xlrd
from openpyxl import load_workbook
import math
from scipy import stats

def filterData(list,Capacitance,Trim):
    n_of_rows = len(list)
    allData=[]
    orderNum=3
    Seallists=[]
    alllists = []
    Caplists=[]
    acCurDenslist=[]
    inCurDenslist=[]
    for j in range(1,16):
        Seallist = []
        for i in range(orderNum, orderNum+9):
            if (i - 3) % 10 == 0: #Seal Resistance
                for k in range(3,n_of_rows):
                    if list[k][i]=='NaN':
                        nowValue=list[k][i]
                    else:
                        nowValue = float(list[k][i]) / 1000000
                    Seallist.append(nowValue)
        Seallists.append(Seallist)

        alllist = []
        for i in range(orderNum, orderNum+9):
            nowlist=[]
            if (i - 3) % 10 > 0 and (i - 3) % 10 < 6:
                for k in range(3,n_of_rows):
                    if list[k][i]=='NaN':
                        nowValue=list[k][i]
                    else:
                        nowValue = float(list[k][i]) *(-1000000000000)
                    nowlist.append(nowValue)
                alllist.append(nowlist)
        alllists.append(alllist)

        Caplist=[]
        for i in range(orderNum, orderNum + 9):
            if (i - 3) % 10 == 6:  # OA Function Cap
                for k in range(3, n_of_rows):
                    if list[k][i]=='NaN':
                        nowValue=list[k][i]
                    else:
                        nowValue = float(list[k][i]) * float((math.pow(10, 12)))
                    Caplist.append(nowValue)
        Caplists.append(Caplist)
        orderNum = orderNum + 10

    Num=3
    for f in range(15):
        acCurDens=[]
        inCurDens=[]
        for i in range(Num, Num + 9):
            if (i - 3) % 10 == 7:  #OA Function CurDens ac
                for k in range(n_of_rows-3):
                    if list[k+3][i] == 'NaN':
                        nowValue=list[k+3][i]
                    else:
                        if float(Caplists[f][k]) < Capacitance:
                            Qlist = []
                            for Caplistsitem in Caplists[f]:
                                Qlist.append(float(Caplistsitem))
                            nowValue = Seallists[f][k] / stats.trim_mean(Qlist, Trim)
                        else:
                            nowValue=float(list[k+3][i])*(-1)
                    acCurDens.append(nowValue)
            if (i - 3) % 10 == 8:  #OA Function CurDens in
                for k in range(n_of_rows-3):
                    if list[k+3][i] == 'NaN':
                        nowValue=list[k+3][i]
                    else:
                        if float(Caplists[f][k]) < Capacitance:
                            Qlist = []
                            for Caplistsitem in Caplists[f]:
                                Qlist.append(float(Caplistsitem))
                            nowValue = Seallists[f][k] / stats.trim_mean(Qlist, Trim)
                        else:
                            nowValue=float(list[k+3][i])*(-1)
                    inCurDens.append(nowValue)
        acCurDenslist.append(acCurDens)
        inCurDenslist.append(inCurDens)
        Num = Num + 10

    for n in range(len(Seallists)):
        nowlist=[]
        nowlist.append(Seallists[n])
        for items in alllists[n]:
            nowlist.append(items)
        nowlist.append(Caplists[n])
        nowlist.append(acCurDenslist[n])
        nowlist.append(inCurDenslist[n])
        allData.append(nowlist)
    return allData

