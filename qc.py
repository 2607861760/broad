import xlrd
from openpyxl import load_workbook
import numpy as np
def qc(dataIVs,filterDatas,IVcompliers,Activations,QCparameter,weightlist):
    Blist= weightlist #[5,2,1,1,0.5,0.5]
    preQC=[]
    sealQC=[]
    newdataIVs = []
    for index in range(len(dataIVs[0])):
        newlists = []
        for n in range(len(dataIVs)):
            newlists.append(dataIVs[n][index])
        newdataIVs.append(newlists)
    B4=newdataIVs[1][3:]
    for B4item in B4:
        preQC.append(float(Blist[0])) if B4item=="T" else preQC.append(0)
    K4=filterDatas[0][0]
    for K4item in K4:
        sealQC.append(float(Blist[2])) if K4item>float(QCparameter['Seal']) else sealQC.append(0)
    IVF4=[]
    IVMax=[]
    for index in range(len(IVcompliers[0])):
        newlists = []
        for n in range(len(IVcompliers)):
            newlists.append(IVcompliers[n][index])
        IVF4.append(max(newlists))
    for IVF4item in IVF4:
        IVMax.append(float(Blist[3])) if IVF4item>float(QCparameter['Peak']) else IVMax.append(0)
    Good=[]
    AcIMax=[]
    for index in range(len(Activations[0])):
        nowValue = []
        for n in range(len(Activations)):
            nowValue.append(Activations[n][index])
        Dvalue = []
        for nowIndex in range(1,len(nowValue)):
            Dvalue.append(abs(nowValue[nowIndex]-nowValue[nowIndex-1]))
        AcIMax.append(max(Dvalue))
    for AcIMaxitem in AcIMax:
        Good.append(float(Blist[1])) if AcIMaxitem<float(QCparameter['IVJ']) else Good.append(0)
    Leak=[]
    Current=[]
    filter=[]
    sfilter=[]
    for lens in range(len(filterDatas)):
        filter.append(filterDatas[lens][4])
        sfilter.append(filterDatas[lens][5])
    for index in range(len(filter[0])):
        newlists = []
        for n in range(len(filter)):
            newlists.append(filter[n][index])
        Leak.append(float(Blist[4])) if abs(max(newlists)) < float(QCparameter['Pre']) else Leak.append(0)
    for index in range(len(sfilter[0])):
        newCurrent = []
        for n in range(len(sfilter)):
            newCurrent.append(sfilter[n][index])
        aver = float(np.average(newCurrent))
        maxr=IVF4[index]
        if abs(aver / maxr *100)<float(QCparameter['Steady']):
            Current.append(float(Blist[5]))
        else:
            Current.append(0)
    QCScore=[]
    for rowIndex in range(len(Leak)):
        sum=sealQC[rowIndex]+preQC[rowIndex]+IVMax[rowIndex]+Good[rowIndex]+Leak[rowIndex]+Current[rowIndex]
        QCScore.append(sum)

    a={}
    for r in QCScore:
        if QCScore.count(r) >= 1:
            a[r] = QCScore.count(r)
    m=10.5
    Score=[]
    while m>0:
        m-=0.5
        Score.append(m)
    count=[]
    for Scoreitem in Score:
        count.append(0) if a.__contains__(Scoreitem)==False else count.append(a[Scoreitem])
    success="%.0f%%" %(float(np.sum(count[0:5]))/float(np.sum(count))*100)
    Manual=float(np.sum(count[11:]))
    total=float(np.sum(count[0:]))
    return count,total,success,Manual,QCScore

