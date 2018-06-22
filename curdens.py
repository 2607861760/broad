import numpy as np
import scipy.stats as stats
import math

def maxdata(list,QCScore,start,curqc,indexs):
    k = 0
    allmaxlist=[]
    newmaxlist=[]
    semlist=[]
    indexlists=[]
    newlist=[]
    nmaxlist=[]
    stdmaxlist=[]
    semmaxlist=[]
    obj={}
    for n,item in enumerate(list):
        nowlist = tran(item)
        interval,indexlist=intervals(nowlist,indexs[n])
        indexlists.append(indexlist)
        j=0
        maxlist=[]
        nowslist=[]
        for newitem in nowlist:
            if j>=start and j<=start+32:
                if j in indexlist and QCScore[k][j] >= curqc :
                    h=0
                    for items in newitem:
                        if items!='NAN' and items<10000:
                            h+=1
                    if h==len(newitem):
                        nowslist.append(newitem)
                        maxlist.append(max(newitem))
            j+=1
        allmaxlist.append(np.average(maxlist))
        nmaxlist.append(len(maxlist))
        stdmaxlist.append(np.std(maxlist))
        semmaxlist.append(np.std(maxlist)/math.sqrt(len(maxlist)))
        semlist.append(Sample_Mean(maxlist))
        newlist.append(nowslist)

    for items in allmaxlist:
        newmaxlist.append(items/max(allmaxlist)*100)
    obj['avglist'] = allmaxlist
    obj['nlist'] = nmaxlist
    obj['stdlist'] = stdmaxlist
    obj['semlist'] = semmaxlist
    return newmaxlist,semlist,indexlists,newlist,obj

def tran(list):
    return [[r[col] for r in list] for col in range(len(list[0]))]

def intervals(list,indexs):
    indexlist = []
    newlist=[]
    intervallist=[]
    for k,items in enumerate(list):
        nowlist = []
        j = 0
        if k in indexs:
            for now in items:
                if now != 'NaN':
                    nowlist.append(now)
                    j += 1
        if j == len(items):
            indexlist.append(k)
        newlist.append(nowlist)
    for item in newlist:
        mean = np.average(item)
        std = np.std(item)
        interval = stats.t.interval(0.95, len(item) - 1, mean, std)
        intervallist.append(interval)
    return intervallist,indexlist

def Sample_Mean(list):
    std = np.std(list)
    sem = std / math.sqrt(len(list))
    return sem

def CurDens_Pvt(accurrentlist,incurrentlist,QCScorelist,curqc,acindexs,inacindexs):
    indexlist = [0, 32, 64, 96, 128, 160, 191, 223, 255, 287, 319, 351]
    acmaxlist=[]
    sslmaxlist=[]
    acsemlist=[]
    insemlist=[]
    acindexlists=[]
    inacindexlists=[]
    acnowlists=[]
    inacnowlists=[]
    acobjlist=[]
    inobjlist=[]

    for n,item in enumerate(indexlist):
        nowac,acsem,acindexlists,acnowlist,acobj=maxdata(accurrentlist,QCScorelist,item,curqc,acindexs)
        acmaxlist.append(nowac)
        acsemlist.append(acsem)
        acnowlists.append(acnowlist)
        acobjlist.append(acobj)
        nowin,insem,inacindexlists,inacnowlist,inacobj=maxdata(incurrentlist, QCScorelist, item,curqc,inacindexs)
        sslmaxlist.append(nowin)
        insemlist.append(insem)
        inacnowlists.append(inacnowlist)
        inobjlist.append(inacobj)
    return acmaxlist,sslmaxlist,acsemlist,insemlist,acindexlists,inacindexlists,acnowlists,inacnowlists,acobjlist,inobjlist





