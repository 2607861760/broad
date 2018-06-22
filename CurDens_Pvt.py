import xlrd
import numpy as np
from openpyxl import Workbook
import matplotlib.pyplot as plt
import scipy.stats as stats



def CurDens_Pvt(sheetname):

	workbook = xlrd.open_workbook(r"E:\learn\readexcel\python\new\data.xlsx")
	part_sheet = workbook.sheet_by_name(sheetname)

	n_of_rows = part_sheet.nrows
	n_of_cols = part_sheet.ncols

	acmaxlist=[]
	for rows in range(2,n_of_rows):
		if 'NaN' not in part_sheet.row_values(rows)[1:16]:
			if max(part_sheet.row_values(rows)[1:16])<10000:
				acmaxlist.append(max(part_sheet.row_values(rows)[1:16]))
		# else:
		# 	acmaxlist.append(0)
	sslmaxlist = []
	for rows in range(2, n_of_rows):
		if 'NaN' not in part_sheet.row_values(rows)[17:32]:
			if max(part_sheet.row_values(rows)[17:32]) < 10000:
				sslmaxlist.append(max(part_sheet.row_values(rows)[17:32]))
		# else:
		# 	sslmaxlist.append(0)
	# print(acmaxlist)
	# print(np.average(acmaxlist))
	# return acmaxlist,sslmaxlist

	return np.average(acmaxlist),np.average(sslmaxlist)
# def intervals(list):
# 	mean = np.average(list)
# 	std = np.std(list)
# 	interval = stats.t.interval(0.95, len(list) - 1, mean, std)
# 	newlist=[]
# 	for item in list:
# 		if item>interval[0] and item>interval[1]:
# 			newlist.append(item)
# 	return np.average(newlist)


def plot(acmaxlist,sslmaxlist):
	x=[1,2,3,4]
	plt.title("Peak Current Density")
	plt.plot(x,acmaxlist,label="Max Current Density (Ac)",color="b")
	plt.plot(x, sslmaxlist, label="Max Current Density (SSI)", color="darkorange")
	plt.xticks([1,2,3,4],["IV1","IV2","IV3","IV4"])
	plt.ylabel("Current Density (pA/pF)")
	plt.legend()
	plt.show()




if __name__ == '__main__':
	list=["Current Density(1)","Current Density(2)","Current Density(3)","Current Density(4)"]
	avglist=[]
	ssllist=[]
	for item in list:
		avg,ssl=CurDens_Pvt(item)
		avglist.append(avg)
		ssllist.append(ssl)
	print(avglist)
	print(ssllist)
	plot(avglist,ssllist)

    
