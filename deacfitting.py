import numpy as np
from scipy import optimize

def func(x, a, b, c):
    return (c+(a*np.exp(((-1)*b)*x)))

def deac_fit(list):
    newfile = [[r[col] for r in list] for col in range(len(list[0]))]
    fitlist = []
    bfitlist = []
    for newfileitem in newfile:
        y0 = newfileitem
        x0 = [0,0.5,1,1.5,2.5,3.5,4.5,9.5,29.5]
        lists = []
        try:
            A3, B3, C3= optimize.curve_fit(func, x0, y0)[0]
            lists.append(A3)
            lists.append(B3)
            lists.append(C3)
            fitlist.append(lists)
            bfitlist.append(B3)
        except RuntimeError:
            fitlist.append(['NAN'] * 3)
            bfitlist.append('NAN')
            continue
    return bfitlist,fitlist
