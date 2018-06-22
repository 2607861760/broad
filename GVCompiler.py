
import numpy as np
from scipy import stats

def read_excel(IVlistac,mvlist,IVlistin):
    def data(IVlist,state,list):
        allResults=[]
        for IVlistindex in range(len(IVlist)):
            results=[]
            for IVlistindexs in range(len(IVlist[IVlistindex])):
                listx=mvlist[-3:]
                listy = [list[-3][IVlistindexs],list[-2][IVlistindexs],list[-1][IVlistindexs]]
                slope, intercept, r_value, p_value, std_err = stats.linregress(listx, listy)
                num1=IVlist[IVlistindex][IVlistindexs]
                for mvlistindex in range(len(mvlist)):
                    if mvlist[mvlistindex] == -20:
                        numindex = mvlistindex
                if state == 'active':
                     num2 = mvlist[IVlistindex]
                     result = - num1 / (num2 - (- intercept / slope))
                elif state == 'inactive':
                    num2=list[numindex][IVlistindexs]
                    result = num1 / (num2 - (- intercept / slope))
                results.append(result)
            allResults.append(results)
        return allResults
    return data(IVlistac,"active",IVlistac),data(IVlistin,"inactive",IVlistac)


