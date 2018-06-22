import numpy as np
import scipy.stats as stats
import math

def qc8(file,filterfile,start,comqc):
    indexlist=[]
    for index in range(len(filterfile)):
        if filterfile[index]>=comqc:
            indexlist.append(index)
    newlist=[]
    for n in range(len(file)):
        newlists=[]
        for j in range(start,start+32):
            for indexlistitem in indexlist:
                if j==indexlistitem:
                    newlists.append(file[n][j])
        newlist.append(newlists)
    return newlist

def avg(list,alllist):
    listavg=[]
    nlist=[]
    intervals=Interval(alllist)
    newlist=tran(list)
    nowlist=[]
    for n,item in enumerate(newlist):
        j=0
        for items in item:
            if items>intervals[j][0] and items<intervals[j][1] and abs(items)<=100 and abs(items)>=0:
                j+=1
        if j==len(item):
            nlist.append(n)
            nowlist.append(item)
    avglist=tran(nowlist)
    listindex=[]
    liststd=[]
    listsem=[]
    for listitem in avglist:
        listavg.append(np.average(listitem))
        listindex.append(len(listitem))
        liststd.append(np.std(listitem))
        listsem.append(np.std(listitem)/math.sqrt(len(listitem)))
    outdata={}
    outdata['listavg']=listavg
    outdata['nlist']=nlist
    outdata['listindex']=listindex
    outdata['liststd']=liststd
    outdata['listsem']=listsem
    return outdata

def tran(list):
    return [[r[col] for r in list] for col in range(len(list[0]))]

def Interval(alllist):
    intervals = []
    for alllistitem in alllist:
        mean = np.average(alllistitem)
        std = np.std(alllistitem)
        interval = stats.t.interval(0.95, len(alllistitem) - 1, mean, std)
        intervals.append(interval)
    return intervals

def nList(list):
    newlist=tran(list)
    intervals = Interval(list)
    nlist=[]
    n=0
    for item in newlist:
        j=0
        for items in item:
            if items>intervals[j][0] and items<intervals[j][1] and abs(items)<=100 and abs(items)>=0:
                j+=1
        if j==len(item):
            nlist.append(n)
        n+=1
    return nlist

def allNlist(aclist,inaclist):
    acnlist=[]
    inacnlist=[]
    for item in aclist:
        acnlist.append(nList(item))
    for item in inaclist:
        inacnlist.append(nList(item))
    return acnlist,inacnlist

def compound(aclist,inaclist,scorelist,comqc):
    indexlist=[0,32,64,96,128,160,191,223,255,287,319,351]
    acylists=[]
    inylists=[]
    acindexs = []
    inacindexs =[]
    acstds=[]
    instds=[]
    acsems=[]
    insems=[]
    acnums=[]
    innums=[]
    for n,item in enumerate(indexlist):
        acobj1=avg(qc8(aclist[0],scorelist[0],item,comqc),aclist[0])
        acobj2=avg(qc8(aclist[1],scorelist[1],item,comqc),aclist[1])
        acobj3=avg(qc8(aclist[2],scorelist[2],item,comqc),aclist[2])
        acobj4=avg(qc8(aclist[3],scorelist[3],item,comqc),aclist[3])
        inobj1 = avg(qc8(inaclist[0], scorelist[0], item, comqc), inaclist[0])
        inobj2 = avg(qc8(inaclist[1], scorelist[1], item, comqc), inaclist[1])
        inobj3 = avg(qc8(inaclist[2], scorelist[2], item, comqc), inaclist[2])
        inobj4 = avg(qc8(inaclist[3], scorelist[3], item, comqc), inaclist[3])
        acylist=[acobj1['listavg'],acobj2['listavg'],acobj3['listavg'],acobj4['listavg']]
        inylist = [inobj1['listavg'], inobj2['listavg'],inobj3['listavg'], inobj4['listavg']]
        acindex=[acobj1['listindex'],acobj2['listindex'],acobj3['listindex'],acobj4['listindex']]
        inacindex=[inobj1['listindex'],inobj2['listindex'],inobj3['listindex'],inobj4['listindex']]
        acstd = [acobj1['liststd'], acobj2['liststd'], acobj3['liststd'], acobj4['liststd']]
        instd = [inobj1['liststd'], inobj2['liststd'], inobj3['liststd'], inobj4['liststd']]
        acsem = [acobj1['listsem'], acobj2['listsem'], acobj3['listsem'], acobj4['listsem']]
        insem = [inobj1['listsem'], inobj2['listsem'], inobj3['listsem'], inobj4['listsem']]
        acnum = [acobj1['nlist'], acobj2['nlist'], acobj3['nlist'], acobj4['nlist']]
        innum = [inobj1['nlist'], inobj2['nlist'], inobj3['nlist'], inobj4['nlist']]
        acylists.append(acylist)
        inylists.append(inylist)
        acindexs.append(acindex)
        inacindexs.append(inacindex)
        acstds.append(acstd)
        instds.append(instd)
        acsems.append(acsem)
        insems.append(insem)
        acnums.append(acnum)
        innums.append(innum)
    return acylists,inylists,acindexs,inacindexs,acstds,instds,acsems,insems,acnums,innums




