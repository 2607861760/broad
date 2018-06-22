import numpy as np
import scipy.stats as stats
def averg_ac_inc(list):
	averglist=[]
	interval=Interval(list)

	newlist = []
	for listitem in tran(list):
		j=0
		n = 0
		for listitems in listitem:
			# if abs(listitems)<10000:
			# 	newlist.append(listitems)
			if listitems<=interval[n][1] and listitems>=interval[n][0]:
				j+=1
			n+=1
		if j==len(listitem):
			newlist.append(listitem)
	for item in tran(newlist):
		averg=np.average(item)
		averglist.append(averg)
	return averglist

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










