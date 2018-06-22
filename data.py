import numpy as np
from scipy import optimize

def func(x, a, b, c,d):
    return (a+((b-a)/(1+np.exp((c-x)/d))))


def curve_fit(file):
    newfile=[[r[col] for r in file] for col in range(len(file[0]))]
    fitlist=[]
    cfitlist=[]
    for newfileitem in newfile:
        y0 = newfileitem
        x0 = np.linspace(-120, 20, 15)
        lists=[]
        try:
            A3, B3, C3, D3 = optimize.curve_fit(func, x0, y0)[0]
            lists.append(A3)
            lists.append(B3)
            lists.append(C3)
            lists.append(D3)
            fitlist.append(lists)
            cfitlist.append(C3)
        except RuntimeError:
            fitlist.append(['NAN']*4)
            cfitlist.append('NAN')
            continue
    return fitlist

def avg_curve_fit(file,filter,comqc):
    newfile=[[r[col] for r in file] for col in range(len(file[0]))]
    fitlist=[]
    for index in range(len(newfile)):
        if filter[index]>=comqc:
            fitlist.append(newfile[index])
    newfitlist = [[r[col] for r in fitlist] for col in range(len(fitlist[0]))]
    avglist=[np.average(item) for item in newfitlist]
    x0 = np.linspace(-120, 20, 15)
    A3, B3, C3, D3 = optimize.curve_fit(func, x0, avglist)[0]
    avgfit={}
    avgfit["alist"]=A3
    avgfit["blist"] = B3
    avgfit["clist"] = C3
    avgfit["dlist"] = D3
    return avgfit













