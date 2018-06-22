from openpyxl import load_workbook
import xlrd

def current(IVlist,filterData):
    # print(filterData)
    n=0
    aclist = []
    inlist=[]
    for name in IVlist[1]:
        if name == "OA Function CurDens ac":
            aclist.append(n)
        if name=="OA Function CurDens in":
            inlist.append(n)
        n+=1
    accurrent=[]
    incurrent = []
    acindex=aclist[0]-3
    inindex=inlist[0]-3
    for n in range(len(filterData)):
        accurrent.append(filterData[n][acindex])
        incurrent.append(filterData[n][inindex])
    return accurrent,incurrent

