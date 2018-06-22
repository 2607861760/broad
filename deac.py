import math

def pm(sheet):
    nlist=[]
    for n in range(len(sheet[1])):
        if sheet[1][n]=="OA Function TL1_DeMax":
            nlist.append(n)
    pmlist=[]
    for j in range(nlist[-1],nlist[-1]+9):
        explist=[]
        for i in range(3,len(sheet)):
            exps=float(sheet[i][j])*float(math.pow(10,12))*(-1)
            explist.append(exps)
        pmlist.append(explist)
    perlist=[]
    try:
        for pmitem in tran(pmlist):
            if pmitem[0]!=0:
                newperlist=[item/pmitem[0]*100 for item in pmitem]
            else:
                newperlist = [0 for item in pmitem]
            perlist.append(newperlist)
    except Exception as e:
        print('Got an error ', e)
    return perlist,pmlist

def tran(list):
    return [[r[col] for r in list] for col in range(len(list[0]))]

