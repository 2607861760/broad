from broadui import Ui_MainWindow
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import datamain
import curdes_pvt
import avg_plot
import cur_plot
import deac_tau
import GV_Ac_Inc_Pvt
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import os

btnArr = []
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        self.setupUi(self)
        self.center()
        self.acdomslist=[]
        self.aconelist=[]
        self.actenlist=[]
        self.indomslist=[]
        self.inonelist=[]
        self.intenlist=[]
        self.filePathList = []
        self.QCparameter = {}
        self.weight=[]
        self.description=''
        self.outaddress=None
        self.tableWidget.cellClicked.connect(self.cellClicked)
        self.actionInput_File.triggered.connect(self.inputFile)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.rightMenu)
        self.run.clicked.connect(self.running)
        self.curdes_pvt.clicked.connect(self.curdes)
        self.avg_plot.clicked.connect(self.avg)
        self.cur.clicked.connect(self.curplot)
        self.deac.clicked.connect(self.deactau)
        self.report.clicked.connect(self.reports)
        self.subWindow = curdes_pvt.curdespvt()
        self.subWindow2 = avg_plot.avgplot()
        self.subWindow3 = cur_plot.curplot()
        self.subWindow4 = deac_tau.deactau()


    def center(self):  #窗口居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def rightMenu(self, pos):  # 右键菜单
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        meun = QMenu()
        item1 = meun.addAction(u"deleteRow")
        item2 = meun.addAction(u"addRow")
        action = meun.exec_(self.tableWidget.mapToGlobal(pos))
        if action == item1:
            self.tableWidget.removeRow(row_num)
        elif action == item2:
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        else:
            return

    def cellClicked(self, row, column):  # 当前单元格导入文件
        if column == 0 or column == 1:
            filePath = QFileDialog.getOpenFileName(self, 'open file', r'C:\\',
                                                   "CSV Files (*.csv)")
            tt = filePath[0]
            fileName = tt[tt.rfind('/') + 1:]
            if (len(self.filePathList) != 0):
                if column == 0:
                    self.filePathList[0][row] = filePath[0]
                elif column == 1:
                    self.filePathList[1][row] = filePath[0]
            else:
                self.filePathList.append([0] * self.tableWidget.rowCount())
                self.filePathList.append([0] * self.tableWidget.rowCount())
                if column == 0:
                    self.filePathList[0][row] = filePath[0]
                elif column == 1:
                    self.filePathList[1][row] = filePath[0]
            self.tableWidget.setItem(row, column, QTableWidgetItem(fileName))

    def inputFile(self):  # 导入多个文件
        filePath = QFileDialog.getOpenFileNames(self, 'open file', r'C:\\',
                                                "CSV Files (*.csv)")
        IVlist = [0] * self.tableWidget.rowCount()
        PMlist = [0] * self.tableWidget.rowCount()
        self.filePathList=[]
        for i in range(len(filePath[0])):
            tt = filePath[0][i]
            fileName = tt[tt.rfind('/') + 1:]
            if fileName.find("IV") != -1:
                s = fileName[fileName.rfind("IV") + 2]
                tableRow = int(s)
                IVlist[tableRow - 1] = tt
                tableRows = self.tableWidget.rowCount()
                if tableRows < tableRow:
                    self.tableWidget.setRowCount(tableRow)
                self.tableWidget.setItem(tableRow - 1, 0, QTableWidgetItem(fileName))
            if fileName.find("PM") != -1:
                s = fileName[fileName.rfind("PM") + 2]
                tableRow = int(s)
                PMlist[tableRow - 1] = tt
                tableRows = self.tableWidget.rowCount()
                if tableRows < tableRow:
                    self.tableWidget.setRowCount(tableRow)
                self.tableWidget.setItem(tableRow - 1, 1, QTableWidgetItem(fileName))
        self.filePathList.append(IVlist)
        self.filePathList.append(PMlist)

    def running(self):  # 运行

        if self.IVJ.text()!='0' and self.Seal.text()!='0' and self.Peak.text()!='0' and self.Pre.text()!='0' and self.Steady.text()!='0':
            self.QCparameter['IVJ'] = self.IVJ.text()
            self.QCparameter['Seal'] = self.Seal.text()
            self.QCparameter['Peak'] =self.Peak.text()
            self.QCparameter['Pre'] = self.Pre.text()
            self.QCparameter['Steady'] = self.Steady.text()
        else:
            self.QCparameter={}
        if self.wed1.text()!='0.00' and self.wed2.text()!='0.00' and self.wed3.text()!='0.00' and self.wed4.text()!='0.00' and self.wed5.text()!='0.00' and self.wed6.text()!='0.00':
            self.weight=[self.wed1.text(),self.wed2.text(),self.wed3.text(),self.wed4.text(),self.wed5.text(),self.wed6.text()]
        else:
            self.weight=[]
        cutoffs=float(self.cutoff.text())
        trims=float(self.trim.text())
        comqc=float(self.compoundqc.text())
        curqc=float(self.curdenqc.text())
        deacqc=float(self.deacqc.text())
        self.description=self.address.text()
        self.outaddress = os.getcwd() + '\\'+self.description+'\\'
        if not os.path.exists(self.outaddress):
            os.makedirs(self.outaddress)
        datamain.main.legend=[]
        for items in self.filePathList:
            nowfile=[]
            for item in items:
                nowfile.append(item.split('/')[-1].split('.')[0])
            datamain.main.legend.append(nowfile)
        print(datamain.main.legend)
        datamain.main.datarun(self.filePathList, trims, cutoffs, self.QCparameter,self.weight,comqc,curqc,deacqc)
        self.cur.setEnabled(True)
        self.avg_plot.setEnabled(True)
        self.curdes_pvt.setEnabled(True)
        self.deac.setEnabled(True)
        self.report.setEnabled(True)


    def curdes(self):
        self.subWindow.initUI()
        self.subWindow.show()

    def avg(self):
        self.subWindow2.initUI()
        self.subWindow2.show()

    def curplot(self):
        self.subWindow3.initUI()
        self.subWindow3.show()

    def deactau(self):
        self.subWindow4.initUI()
        self.subWindow4.show()


    def reports(self):
        # 导出gv数据
        allAcGV=self.tran(datamain.main.allAcGV)
        allInGV=self.tran(datamain.main.allInGV)
        self.IVoutdata(allAcGV,allInGV,datamain.main.acnlists,datamain.main.innlists,self.description+" GV Complier.csv")
        # 导出deac数据
        perlists=datamain.main.perlists

        self.PMoutdata(perlists)
        # 导出current数据
        accurrentlist=self.tran(datamain.main.accurrentlist)
        incurrentlist=self.tran(datamain.main.incurrentlist)
        self.IVoutdata(accurrentlist, incurrentlist,datamain.main.acindexlists,datamain.main.inacindexlists, self.description+" current.csv")
        self.dataout()
        self.compound_plot()
        self.avgplots()
        # self.ivcurpvts()
        # self.gvcurpvts()
        # self.deactaus()
        self.curdespvts()
        self.deacplot()
        self.count()
        self.normalize()
        self.hitting()

    def PMoutdata(self,list):
        deacfile=open(self.outaddress+self.description+' deac.csv', 'w', newline='')
        writer = csv.writer(deacfile)
        for n in range(len(datamain.main.compoundlist)):
            for j in range(32):
                nowlist=list[0][j+32*n]
                nowlist.append('')
                nowlist[len(nowlist):len(nowlist)] = list[1][j+32*n]
                nowlist.append('')
                nowlist[len(nowlist):len(nowlist)] = list[2][j+32*n]
                nowlist.append('')
                nowlist[len(nowlist):len(nowlist)] = list[3][j+32*n]
                nowlist.insert(0,datamain.main.compoundlist[n])
                if j==0:
                    nowlist.insert(0, n+1)
                else:
                    nowlist.insert(0, '')
                writer.writerow(nowlist)
        print(22222)
        deacfile.close()

    def IVoutdata(self,list1,list2,indexlist1,indexlist2,filename):
        filepath=self.outaddress+filename
        csvfile = open(filepath, 'w', newline='')
        writer = csv.writer(csvfile)
        nullist = [''] * 14
        voltage=[-120,-110,-100,-90,-80,-70,-60,-50,-40,-30,-20,-10,0,10,20]
        firstcol=['','',datamain.main.legend[0][0], 'Activation']
        firstcol.extend(nullist)
        firstcol.extend(['', '', 'Inactivation'])
        firstcol.extend(nullist)
        firstcol.extend(['', datamain.main.legend[0][1], 'Activation'])
        firstcol.extend(nullist)
        firstcol.extend(['', '','', 'Inactivation'])
        firstcol.extend(nullist)
        firstcol.extend(['', datamain.main.legend[0][2], 'Activation'])
        firstcol.extend(nullist)
        firstcol.extend(['', '','', 'Inactivation'])
        firstcol.extend(nullist)
        firstcol.extend(['', datamain.main.legend[0][3], 'Activation'])
        firstcol.extend(nullist)
        firstcol.extend(['', '','', 'Inactivation'])
        title = ['','Compound','QC Score',]
        title.extend(voltage)
        title.extend(['confidence', ''])
        title.extend(voltage)
        title.extend(['confidence','', 'QC Score'])
        title.extend(voltage)
        title.extend(['confidence',''])
        title.extend(voltage)
        title.extend(['confidence','','QC Score'])
        title.extend(voltage)
        title.extend(['confidence', ''])#Inactivation
        title.extend(voltage)
        title.extend(['confidence','', 'QC Score'])
        title.extend(voltage)
        title.extend(['confidence', ''])
        title.extend(voltage)
        title.append('confidence')
        writer.writerow(firstcol)
        writer.writerow(title)
        for n in range(len(datamain.main.compoundlist)):
            for j in range(32):
                slist = list1[0][j + 32 * n]
                if j + 32 * n in indexlist1[0]:
                    slist.append('T')
                else:
                    slist.append('F')
                slist.append('')
                slist[len(slist):len(slist)] = list2[0][j + 32 * n]
                if j + 32 * n in indexlist2[0]:
                    slist.append('T')
                else:
                    slist.append('F')
                slist.extend(['',datamain.main.QCScorelist[1][j + 32 * n]])
                slist[len(slist):len(slist)] = list1[1][j + 32 * n]
                if j + 32 * n in indexlist1[1]:
                    slist.append('T')
                else:
                    slist.append('F')
                slist.append('')
                slist[len(slist):len(slist)] = list2[1][j + 32 * n]
                if j + 32 * n in indexlist2[1]:
                    slist.append('T')
                else:
                    slist.append('F')
                slist.extend(['', datamain.main.QCScorelist[2][j + 32 * n]])
                slist[len(slist):len(slist)] = list1[2][j + 32 * n]
                if j + 32 * n in indexlist1[2]:
                    slist.append('T')
                else:
                    slist.append('F')
                slist.append('')
                slist[len(slist):len(slist)] = list2[2][j + 32 * n]
                if j + 32 * n in indexlist2[2]:
                    slist.append('T')
                else:
                    slist.append('F')
                slist.extend(['', datamain.main.QCScorelist[3][j + 32 * n]])
                slist[len(slist):len(slist)] = list1[3][j + 32 * n]
                if j + 32 * n in indexlist1[3]:
                    slist.append('T')
                else:
                    slist.append('F')
                slist.append('')
                slist[len(slist):len(slist)] = list2[3][j + 32 * n]
                if j + 32 * n in indexlist2[3]:
                    slist.append('T')
                else:
                    slist.append('F')
                slist.insert(0, datamain.main.compoundlist[n])
                slist.insert(1, datamain.main.QCScorelist[0][j + 32 * n])
                if j==0:
                    slist.insert(0, n+1)
                else:
                    slist.insert(0, '')
                writer.writerow(slist)
        print(111111)
        csvfile.close()

    def tran(self,list):
        newlist=[]
        for n in range(len(list)):
            lists = []
            for j in range(len(list[0][0])):
                newlists = []
                for i in range(len(list[0])):
                    newlists.append(list[n][i][j])
                lists.append(newlists)
            newlist.append(lists)
        return newlist

    def dataout(self):
        acdiflist=datamain.main.acdiflists
        indiflist=datamain.main.indiflists
        acfitlist=self.listtran(datamain.main.acfitlist)
        infitlist=self.listtran(datamain.main.infitlist)
        taulist=self.trans(datamain.main.taulist)
        deacfitlist=self.listtran(datamain.main.deacfitlist)
        newlist=[]
        title=['','Compound','QC Score(1)','QC Score(2)','QC Score(3)','QC Score(4)',
               'Delta DMSO_Ac','Delta 1uM_Ac','Delta 10uM_Ac',
               'Delta DMSO_Inact','Delta 1uM_Inact','Delta 10uM_Inact',
               'Max_Ac(GV1)','Min_Ac(GV1)','V(1/2)_Ac(GV1)','Slope_Ac(GV1)',
               'Max_Ac(GV2)','Min_Ac(GV2)','V(1/2)_Ac(GV2)','Slope_Ac(GV2)',
               'Max_Ac(GV3)','Min_Ac(GV3)','V(1/2)_Ac(GV3)','Slope_Ac(GV3)',
               'Max_Ac(GV4)','Min_Ac(GV4)','V(1/2)_Ac(GV4)','Slope_Ac(GV4)',
               'Max_Inact(GV1)', 'Min_Inact(GV1)', 'V(1/2)_Inact(GV1)', 'Slope_Inact(GV1)',
               'Max_Inact(GV2)', 'Min_Inact(GV2)', 'V(1/2)_Inact(GV2)', 'Slope_Inact(GV2)',
               'Max_Inact(GV3)', 'Min_Inact(GV3)', 'V(1/2)_Inact(GV3)', 'Slope_Inact(GV3)',
               'Max_Inact(GV4)', 'Min_Inact(GV4)', 'V(1/2)_Inact(GV4)', 'Slope_Inact(GV4)',
               'Pre-DMSO_PM1_Tau1','DMSO_Ac_PM2_Tau2','1uM_Ac_PM3_Tau3','10uM_Ac_PM4_Tau4',
               'Pre-DMSO_PM1_A', 'Pre-DMSO_PM1_B', 'Pre-DMSO_PM1_C',
               'DMSO_Ac_PM2_A', 'DMSO_Ac_PM2_B', 'DMSO_Ac_PM2_C',
               '1uM_Ac_PM3_A', '1uM_Ac_PM3_B', '1uM_Ac_PM3_C',
               '10uM_Ac_PM4_A','10uM_Ac_PM4_B','10uM_Ac_PM4_C']
        for i in range(len(datamain.main.compoundlist)):
            for j in range(32):
                if j==0:
                    newlist.append([i+1,datamain.main.compoundlist[i]])
                else:
                    newlist.append(['', datamain.main.compoundlist[i]])
        for h in range(len(datamain.main.QCScorelist[0])):
            newlist[h].append(datamain.main.QCScorelist[0][h])
            newlist[h].append(datamain.main.QCScorelist[1][h])
            newlist[h].append(datamain.main.QCScorelist[2][h])
            newlist[h].append(datamain.main.QCScorelist[3][h])
        for n in range(len(acdiflist)):
            nowlist=acdiflist[n].copy()
            nowlist.extend(indiflist[n])
            nowlist.extend(acfitlist[n])
            nowlist.extend(infitlist[n])
            nowlist.extend(taulist[n])
            nowlist.extend(deacfitlist[n])
            newlist[n].extend(nowlist)
        file = open(self.outaddress+self.description+' all.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(title)
        writer.writerows(newlist)
        print(3333)
        file.close()

    def achitcalling(self,list1,list2):
        hit = []
        for n in range(12):
            if list1[n] == 0.0:
                hit.append('')
            elif abs(list1[n]) > 2 * list2[0]['std'] and list1[n] > 0:
                hit.append('-1')
            elif abs(list1[n]) > 2 * list2[0]['std'] and list1[n] < 0:
                hit.append('1')
            else:
                hit.append('0')
        return hit

    def inhitcalling(self,list1,list2):
        hit = []
        for n in range(12):
            if list1[n] == 0.0:
                hit.append('')
            elif abs(list1[n]) > 2 * list2[0]['std'] and list1[n] > 0:
                hit.append('1')
            elif abs(list1[n]) > 2 * list2[0]['std'] and list1[n] < 0:
                hit.append('-1')
            else:
                hit.append('0')
        return hit

    def listtran(self,list):
        newlist=[]
        for n in range(len(list[0])):
            nowlist=list[0][n]
            nowlist.extend(list[1][n])
            nowlist.extend(list[2][n])
            nowlist.extend(list[3][n])
            newlist.append(nowlist)
        return newlist

    def trans(self,list):
        return [[r[col] for r in list] for col in range(len(list[0]))]

    def ratio(self,list):
        value = list[3] / list[1]
        newvalue = float("%.2f" % value)
        return newvalue

    def compound_plot(self):
        x1 = np.linspace(-120, 20, 15)
        x2 = [1, 2, 3, 4]
        xnew = np.linspace(x1.min(), x1.max(), 500)
        acmaxlists = np.asarray(datamain.main.acmaxlist)
        sslmaxlists = np.asarray(datamain.main.sslmaxlist)
        compoundlist = np.asarray(datamain.main.compoundlist)
        acsemlist = np.asarray(datamain.main.acsemlist)
        sslsemlist = np.asarray(datamain.main.insemlist)
        acylists=np.asarray(datamain.main.acylists)
        inylists=np.asarray(datamain.main.inylists)
        for j in range(len(compoundlist)):
            fig1 = plt.figure(figsize=(18, 4), dpi=80)
            st = fig1.suptitle(compoundlist[j])
            legendline = []
            labels = datamain.main.legend[0]
            colors = ["g", "b", "r", "olive"]
            fax11 = fig1.add_subplot(1, 3, 1)
            for n in range(len(acylists[j])):
                newacy = spline(x1, acylists[j][n], xnew)
                newiny = spline(x1, inylists[j][n], xnew)
                line, = fax11.plot(xnew, newacy, color=colors[n])
                fax11.plot(xnew, newiny, color=colors[n])
                fax11.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[j]), size=12)
                fax11.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[j]), size=12)
                fax11.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[j]), size=12)
                fax11.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[j]), size=12)
                legendline.append(line, )
            fax11.set_title('avg_plot')
            fax11.legend(legendline, labels,loc=9)

            fax12 = fig1.add_subplot(1, 3, 2)
            fax12.errorbar(x2, acmaxlists[j], yerr=acsemlist[j], color="b", ecolor="r")
            fax12.errorbar(x2, sslmaxlists[j], yerr=sslsemlist[j], color="darkorange", ecolor="g")
            fax12.set_title('curdens_pvt')
            fax12.set_xticks(x2)
            fax12.set_xticklabels(['IV1', 'IV2', 'IV3', 'IV4'])
            fax12.set_ylim(0, 200)
            fax12.text(1, 35, "Ac:" + str(self.ratio(acmaxlists[j])), size=15)
            fax12.text(1, 15, "SSI:" + str(self.ratio(sslsemlist[j])), size=15)

            listname = ["Pre-DMSO_PM1", "DMSO_Ac_PM2", "1uM_Ac_PM3", "10uM_Ac_PM4"]
            x = [0, 0.5, 1, 1.5, 2.5, 3.5, 4.5, 9.5, 29.5]
            colors = ['g', 'b', 'darkorange', 'gold']
            fax13 = fig1.add_subplot(1, 3, 3)
            fax13.errorbar(x, datamain.main.deacallavglist[0][j], yerr=datamain.main.deacallsemlist[0][j], label=listname[0],
                               color=colors[0], ecolor="thistle")
            fax13.errorbar(x, datamain.main.deacallavglist[1][j], yerr=datamain.main.deacallsemlist[1][j], label=listname[1],
                               color=colors[1], ecolor="thistle")
            fax13.errorbar(x, datamain.main.deacallavglist[2][j], yerr=datamain.main.deacallsemlist[2][j], label=listname[2],
                               color=colors[2], ecolor="thistle")
            fax13.errorbar(x, datamain.main.deacallavglist[3][j], yerr=datamain.main.deacallsemlist[3][j], label=listname[3],
                               color=colors[3], ecolor="thistle")
            fax13.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][j]), size=12)
            fax13.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][j]), size=12)
            fax13.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][j]), size=12)
            fax13.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][j]), size=12)
            fax13.legend()
            fax13.set_ylim(0, 100)
            fig1.savefig(self.outaddress+str(compoundlist[j]), dpi=80)

    def deacplot(self):
        listname = datamain.main.legend[0]
        x = [0, 0.5, 1, 1.5, 2.5, 3.5, 4.5, 9.5, 29.5]
        colors = ['g', 'b', 'darkorange', 'gold']
        fig1 = plt.figure(figsize=(16, 12), dpi=80)
        st = fig1.suptitle("Deactivation Kinetics Curve", fontsize="x-large")
        ax1 = fig1.add_subplot(4, 3, 1)
        ax1.errorbar(x, datamain.main.deacallavglist[0][0], yerr=datamain.main.deacallsemlist[0][0],
                     label=listname[0],
                     color=colors[0], ecolor="thistle")
        ax1.errorbar(x, datamain.main.deacallavglist[1][0], yerr=datamain.main.deacallsemlist[1][0],
                     label=listname[1],
                     color=colors[1], ecolor="thistle")
        ax1.errorbar(x, datamain.main.deacallavglist[2][0], yerr=datamain.main.deacallsemlist[2][0],
                     label=listname[2],
                     color=colors[2], ecolor="thistle")
        ax1.errorbar(x, datamain.main.deacallavglist[3][0], yerr=datamain.main.deacallsemlist[3][0],
                     label=listname[3],
                     color=colors[3], ecolor="thistle")
        ax1.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][0]), size=12)
        ax1.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][0]), size=12)
        ax1.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][0]), size=12)
        ax1.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][0]), size=12)
        ax1.legend(bbox_to_anchor=(2.2, 1.02, 1.05, 0.102), loc=4, borderaxespad=0)
        ax1.set_ylim(0, 100)
        ax1.set_xlabel('TIME(ms)')

        ax2 = fig1.add_subplot(4, 3, 2)
        ax2.errorbar(x, datamain.main.deacallavglist[0][1], yerr=datamain.main.deacallsemlist[0][1],
                     label=listname[0],
                     color=colors[0], ecolor="thistle")
        ax2.errorbar(x, datamain.main.deacallavglist[1][1], yerr=datamain.main.deacallsemlist[1][1],
                     label=listname[1],
                     color=colors[1], ecolor="thistle")
        ax2.errorbar(x, datamain.main.deacallavglist[2][1], yerr=datamain.main.deacallsemlist[2][1],
                     label=listname[2],
                     color=colors[2], ecolor="thistle")
        ax2.errorbar(x, datamain.main.deacallavglist[3][1], yerr=datamain.main.deacallsemlist[3][1],
                     label=listname[3],
                     color=colors[3], ecolor="thistle")
        ax2.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][1]), size=12)
        ax2.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][1]), size=12)
        ax2.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][1]), size=12)
        ax2.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][1]), size=12)
        ax2.set_ylim(0, 100)
        ax2.set_xlabel('TIME(ms)')

        ax3 = fig1.add_subplot(4, 3, 3)
        ax3.errorbar(x, datamain.main.deacallavglist[0][2], yerr=datamain.main.deacallsemlist[0][2],
                     label=listname[0],
                     color=colors[0], ecolor="thistle")
        ax3.errorbar(x, datamain.main.deacallavglist[1][2], yerr=datamain.main.deacallsemlist[1][2],
                     label=listname[1],
                     color=colors[1], ecolor="thistle")
        ax3.errorbar(x, datamain.main.deacallavglist[2][2], yerr=datamain.main.deacallsemlist[2][2],
                     label=listname[2],
                     color=colors[2], ecolor="thistle")
        ax3.errorbar(x, datamain.main.deacallavglist[3][2], yerr=datamain.main.deacallsemlist[3][2],
                     label=listname[3],
                     color=colors[3], ecolor="thistle")
        ax3.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][2]), size=12)
        ax3.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][2]), size=12)
        ax3.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][2]), size=12)
        ax3.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][2]), size=12)
        ax3.set_ylim(0, 100)
        ax3.set_xlabel('TIME(ms)')

        ax4 = fig1.add_subplot(4, 3, 4)
        ax4.errorbar(x, datamain.main.deacallavglist[0][3], yerr=datamain.main.deacallsemlist[0][3],
                     label=listname[0],
                     color=colors[0], ecolor="thistle")
        ax4.errorbar(x, datamain.main.deacallavglist[1][3], yerr=datamain.main.deacallsemlist[1][3],
                     label=listname[1],
                     color=colors[1], ecolor="thistle")
        ax4.errorbar(x, datamain.main.deacallavglist[2][3], yerr=datamain.main.deacallsemlist[2][3],
                     label=listname[2],
                     color=colors[2], ecolor="thistle")
        ax4.errorbar(x, datamain.main.deacallavglist[3][3], yerr=datamain.main.deacallsemlist[3][3],
                     label=listname[3],
                     color=colors[3], ecolor="thistle")
        ax4.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][3]), size=12)
        ax4.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][3]), size=12)
        ax4.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][3]), size=12)
        ax4.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][3]), size=12)
        ax4.set_ylim(0, 100)
        ax4.set_xlabel('TIME(ms)')

        ax5 = fig1.add_subplot(4, 3, 5)
        ax5.errorbar(x, datamain.main.deacallavglist[0][4], yerr=datamain.main.deacallsemlist[0][4],
                     label=listname[0],
                     color=colors[0], ecolor="thistle")
        ax5.errorbar(x, datamain.main.deacallavglist[1][4], yerr=datamain.main.deacallsemlist[1][4],
                     label=listname[1],
                     color=colors[1], ecolor="thistle")
        ax5.errorbar(x, datamain.main.deacallavglist[2][4], yerr=datamain.main.deacallsemlist[2][4],
                     label=listname[2],
                     color=colors[2], ecolor="thistle")
        ax5.errorbar(x, datamain.main.deacallavglist[3][4], yerr=datamain.main.deacallsemlist[3][4],
                     label=listname[3],
                     color=colors[3], ecolor="thistle")
        ax5.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][4]), size=12)
        ax5.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][4]), size=12)
        ax5.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][4]), size=12)
        ax5.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][4]), size=12)
        ax5.set_ylim(0, 100)
        ax5.set_xlabel('TIME(ms)')

        ax6 = fig1.add_subplot(4, 3, 6)
        ax6.errorbar(x, datamain.main.deacallavglist[0][5], yerr=datamain.main.deacallsemlist[0][5],
                     label=listname[0],
                     color=colors[0], ecolor="thistle")
        ax6.errorbar(x, datamain.main.deacallavglist[1][5], yerr=datamain.main.deacallsemlist[1][5],
                     label=listname[1],
                     color=colors[1], ecolor="thistle")
        ax6.errorbar(x, datamain.main.deacallavglist[2][5], yerr=datamain.main.deacallsemlist[2][5],
                     label=listname[2],
                     color=colors[2], ecolor="thistle")
        ax6.errorbar(x, datamain.main.deacallavglist[3][5], yerr=datamain.main.deacallsemlist[3][5],
                     label=listname[3],
                     color=colors[3], ecolor="thistle")
        ax6.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][5]), size=12)
        ax6.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][5]), size=12)
        ax6.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][5]), size=12)
        ax6.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][5]), size=12)
        ax6.set_ylim(0, 100)
        ax6.set_xlabel('TIME(ms)')

        ax7 = fig1.add_subplot(4, 3, 7)
        ax7.errorbar(x, datamain.main.deacallavglist[0][6], yerr=datamain.main.deacallsemlist[0][6],
                     label=listname[0],
                     color=colors[0], ecolor="thistle")
        ax7.errorbar(x, datamain.main.deacallavglist[1][6], yerr=datamain.main.deacallsemlist[1][6],
                     label=listname[1],
                     color=colors[1], ecolor="thistle")
        ax7.errorbar(x, datamain.main.deacallavglist[2][6], yerr=datamain.main.deacallsemlist[2][6],
                     label=listname[2],
                     color=colors[2], ecolor="thistle")
        ax7.errorbar(x, datamain.main.deacallavglist[3][6], yerr=datamain.main.deacallsemlist[3][6],
                     label=listname[3],
                     color=colors[3], ecolor="thistle")
        ax7.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][6]), size=12)
        ax7.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][6]), size=12)
        ax7.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][6]), size=12)
        ax7.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][6]), size=12)
        ax7.legend()
        ax7.set_ylim(0, 100)
        ax7.set_xlabel('TIME(ms)')

        ax8 = fig1.add_subplot(4, 3, 8)
        ax8.errorbar(x, datamain.main.deacallavglist[0][7], yerr=datamain.main.deacallsemlist[0][7],
                     label=listname[0],
                     color=colors[0], ecolor="thistle")
        ax8.errorbar(x, datamain.main.deacallavglist[1][7], yerr=datamain.main.deacallsemlist[1][7],
                     label=listname[1],
                     color=colors[1], ecolor="thistle")
        ax8.errorbar(x, datamain.main.deacallavglist[2][7], yerr=datamain.main.deacallsemlist[2][7],
                     label=listname[2],
                     color=colors[2], ecolor="thistle")
        ax8.errorbar(x, datamain.main.deacallavglist[3][7], yerr=datamain.main.deacallsemlist[3][7],
                     label=listname[3],
                     color=colors[3], ecolor="thistle")
        ax8.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][7]), size=12)
        ax8.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][7]), size=12)
        ax8.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][7]), size=12)
        ax8.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][7]), size=12)
        ax8.set_ylim(0, 100)
        ax8.set_xlabel('TIME(ms)')

        ax9 = fig1.add_subplot(4, 3, 9)
        ax9.errorbar(x, datamain.main.deacallavglist[0][8], yerr=datamain.main.deacallsemlist[0][8],
                     label=listname[0],
                     color=colors[0], ecolor="thistle")
        ax9.errorbar(x, datamain.main.deacallavglist[1][8], yerr=datamain.main.deacallsemlist[1][8],
                     label=listname[1],
                     color=colors[1], ecolor="thistle")
        ax9.errorbar(x, datamain.main.deacallavglist[2][8], yerr=datamain.main.deacallsemlist[2][8],
                     label=listname[2],
                     color=colors[2], ecolor="thistle")
        ax9.errorbar(x, datamain.main.deacallavglist[3][8], yerr=datamain.main.deacallsemlist[3][8],
                     label=listname[3],
                     color=colors[3], ecolor="thistle")
        ax9.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][8]), size=12)
        ax9.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][8]), size=12)
        ax9.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][8]), size=12)
        ax9.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][8]), size=12)
        ax9.set_ylim(0, 100)
        ax9.set_xlabel('TIME(ms)')

        ax10 = fig1.add_subplot(4, 3, 10)
        ax10.errorbar(x, datamain.main.deacallavglist[0][9], yerr=datamain.main.deacallsemlist[0][9],
                      label=listname[0],
                      color=colors[0], ecolor="thistle")
        ax10.errorbar(x, datamain.main.deacallavglist[1][9], yerr=datamain.main.deacallsemlist[1][9],
                      label=listname[1],
                      color=colors[1], ecolor="thistle")
        ax10.errorbar(x, datamain.main.deacallavglist[2][9], yerr=datamain.main.deacallsemlist[2][9],
                      label=listname[2],
                      color=colors[2], ecolor="thistle")
        ax10.errorbar(x, datamain.main.deacallavglist[3][9], yerr=datamain.main.deacallsemlist[3][9],
                      label=listname[3],
                      color=colors[3], ecolor="thistle")
        ax10.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][9]), size=12)
        ax10.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][9]), size=12)
        ax10.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][9]), size=12)
        ax10.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][9]), size=12)
        ax10.set_ylim(0, 100)
        ax10.set_xlabel('TIME(ms)')

        ax11 = fig1.add_subplot(4, 3, 11)
        ax11.errorbar(x, datamain.main.deacallavglist[0][10], yerr=datamain.main.deacallsemlist[0][11],
                      label=listname[0],
                      color=colors[0], ecolor="thistle")
        ax11.errorbar(x, datamain.main.deacallavglist[1][10], yerr=datamain.main.deacallsemlist[1][11],
                      label=listname[1],
                      color=colors[1], ecolor="thistle")
        ax11.errorbar(x, datamain.main.deacallavglist[2][10], yerr=datamain.main.deacallsemlist[2][11],
                      label=listname[2],
                      color=colors[2], ecolor="thistle")
        ax11.errorbar(x, datamain.main.deacallavglist[3][10], yerr=datamain.main.deacallsemlist[3][11],
                      label=listname[3],
                      color=colors[3], ecolor="thistle")
        ax11.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][10]), size=12)
        ax11.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][10]), size=12)
        ax11.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][10]), size=12)
        ax11.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][10]), size=12)
        ax11.set_ylim(0, 100)
        ax11.set_xlabel('TIME(ms)')

        ax12 = fig1.add_subplot(4, 3, 12)
        ax12.errorbar(x, datamain.main.deacallavglist[0][11], yerr=datamain.main.deacallsemlist[0][11],
                      label=listname[0],
                      color=colors[0], ecolor="thistle")
        ax12.errorbar(x, datamain.main.deacallavglist[1][11], yerr=datamain.main.deacallsemlist[1][11],
                      label=listname[1],
                      color=colors[1], ecolor="thistle")
        ax12.errorbar(x, datamain.main.deacallavglist[2][11], yerr=datamain.main.deacallsemlist[2][11],
                      label=listname[2],
                      color=colors[2], ecolor="thistle")
        ax12.errorbar(x, datamain.main.deacallavglist[3][11], yerr=datamain.main.deacallsemlist[3][11],
                           label=listname[3],
                           color=colors[3], ecolor="thistle")
        ax12.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][11]), size=12)
        ax12.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][11]), size=12)
        ax12.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][11]), size=12)
        ax12.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][11]), size=12)
        ax12.set_ylim(0, 100)
        ax12.set_xlabel('TIME(ms)')

        fig1.tight_layout()
        st.set_y(0.98)
        fig1.subplots_adjust(top=0.92, bottom=0.08)
        fig1.savefig(self.outaddress + 'deac_plot.png', dpi=80)

    def avgplots(self):
        acylists=datamain.main.acylists
        inylists=datamain.main.inylists
        compoundlist=datamain.main.compoundlist
        x = np.linspace(-120, 20, 15)
        fig1 = plt.figure(figsize=(16, 12), dpi=80)
        st = fig1.suptitle("Mean curve of 12 compounds", fontsize="x-large")
        legendline = []
        labels = datamain.main.legend[0]
        xnew = np.linspace(x.min(), x.max(), 500)

        ax1 = fig1.add_subplot(4, 3, 1)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[0][n], xnew)
            newiny = spline(x, inylists[0][n], xnew)
            line, = ax1.plot(xnew,newacy , color=datamain.main.colors[n])
            ax1.plot(xnew, newiny, color=datamain.main.colors[n])
            ax1.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[0]), size=12)
            ax1.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[0]), size=12)
            ax1.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[0]), size=12)
            ax1.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[0]), size=12)
            legendline.append(line, )
        ax1.set_title(compoundlist[0])
        ax1.set_xlabel('Voltage(mV)')

        ax2 = fig1.add_subplot(432)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[1][n], xnew)
            newiny = spline(x, inylists[1][n], xnew)
            ax2.plot(xnew, newacy, color=datamain.main.colors[n])
            ax2.plot(xnew, newiny, color=datamain.main.colors[n])
            ax2.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[1]), size=12)
            ax2.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[1]), size=12)
            ax2.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[1]), size=12)
            ax2.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[1]), size=12)
        ax2.set_title(compoundlist[1])
        ax2.set_xlabel('Voltage(mV)')

        ax3 = fig1.add_subplot(433)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[2][n], xnew)
            newiny = spline(x, inylists[2][n], xnew)
            ax3.plot(xnew, newacy, color=datamain.main.colors[n])
            ax3.plot(xnew, newiny, color=datamain.main.colors[n])
            ax3.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[2]), size=12)
            ax3.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[2]), size=12)
            ax3.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[2]), size=12)
            ax3.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[2]), size=12)
        ax3.set_title(compoundlist[2])
        ax3.set_xlabel('Voltage(mV)')

        ax4 = fig1.add_subplot(434)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[3][n], xnew)
            newiny = spline(x, inylists[3][n], xnew)
            ax4.plot(xnew, newacy, color=datamain.main.colors[n])
            ax4.plot(xnew, newiny, color=datamain.main.colors[n])
            ax4.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[3]), size=12)
            ax4.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[3]), size=12)
            ax4.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[3]), size=12)
            ax4.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[3]), size=12)
        ax4.set_title(compoundlist[3])
        ax4.set_xlabel('Voltage(mV)')

        ax5 = fig1.add_subplot(435)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[4][n], xnew)
            newiny = spline(x, inylists[4][n], xnew)
            ax5.plot(xnew, newacy, color=datamain.main.colors[n])
            ax5.plot(xnew, newiny, color=datamain.main.colors[n])
            ax5.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[4]), size=12)
            ax5.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[4]), size=12)
            ax5.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[4]), size=12)
            ax5.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[4]), size=12)
        ax5.set_title(compoundlist[4])
        ax5.set_xlabel('Voltage(mV)')

        ax6 = fig1.add_subplot(436)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[5][n], xnew)
            newiny = spline(x, inylists[5][n], xnew)
            ax6.plot(xnew, newacy, color=datamain.main.colors[n])
            ax6.plot(xnew, newiny, color=datamain.main.colors[n])
            ax6.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[5]), size=12)
            ax6.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[5]), size=12)
            ax6.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[5]), size=12)
            ax6.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[5]), size=12)
        ax6.set_title(compoundlist[5])
        ax6.set_xlabel('Voltage(mV)')

        ax7 = fig1.add_subplot(437)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[6][n], xnew)
            newiny = spline(x, inylists[6][n], xnew)
            ax7.plot(xnew, newacy, color=datamain.main.colors[n])
            ax7.plot(xnew, newiny, color=datamain.main.colors[n])
            ax7.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[6]), size=12)
            ax7.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[6]), size=12)
            ax7.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[6]), size=12)
            ax7.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[6]), size=12)
        ax7.set_title(compoundlist[6])
        ax7.set_xlabel('Voltage(mV)')

        ax8 = fig1.add_subplot(438)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[7][n], xnew)
            newiny = spline(x, inylists[7][n], xnew)
            ax8.plot(xnew, newacy, color=datamain.main.colors[n])
            ax8.plot(xnew, newiny, color=datamain.main.colors[n])
            ax8.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[7]), size=12)
            ax8.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[7]), size=12)
            ax8.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[7]), size=12)
            ax8.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[7]), size=12)
        ax8.set_title(compoundlist[7])
        ax8.set_xlabel('Voltage(mV)')

        ax9 = fig1.add_subplot(439)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[8][n], xnew)
            newiny = spline(x, inylists[8][n], xnew)
            ax9.plot(xnew, newacy, color=datamain.main.colors[n])
            ax9.plot(xnew, newiny, color=datamain.main.colors[n])
            ax9.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[8]), size=12)
            ax9.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[8]), size=12)
            ax9.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[8]), size=12)
            ax9.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[8]), size=12)
        ax9.set_title(compoundlist[8])
        ax9.set_xlabel('Voltage(mV)')

        ax10 = fig1.add_subplot(4, 3, 10)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[9][n], xnew)
            newiny = spline(x, inylists[9][n], xnew)
            ax10.plot(xnew, newacy, color=datamain.main.colors[n])
            ax10.plot(xnew, newiny, color=datamain.main.colors[n])
            ax10.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[9]), size=12)
            ax10.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[9]), size=12)
            ax10.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[9]), size=12)
            ax10.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[9]), size=12)
        ax10.set_title(compoundlist[9])
        ax10.set_xlabel('Voltage(mV)')

        ax11 = fig1.add_subplot(4, 3, 11)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[10][n], xnew)
            newiny = spline(x, inylists[10][n], xnew)
            ax11.plot(xnew, newacy, color=datamain.main.colors[n])
            ax11.plot(xnew, newiny, color=datamain.main.colors[n])
            ax11.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[10]), size=12)
            ax11.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[10]), size=12)
            ax11.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[10]), size=12)
            ax11.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[10]), size=12)
        ax11.set_title(compoundlist[10])
        ax11.set_xlabel('Voltage(mV)')

        ax12 = fig1.add_subplot(4, 3, 12)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[11][n], xnew)
            newiny = spline(x, inylists[11][n], xnew)
            ax12.plot(xnew, newacy, color=datamain.main.colors[n])
            ax12.plot(xnew, newiny, color=datamain.main.colors[n])
            ax12.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[11]), size=12)
            ax12.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[11]), size=12)
            ax12.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[11]), size=12)
            ax12.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[11]), size=12)
        ax12.set_title(compoundlist[11])
        ax12.set_xlabel('Voltage(mV)')

        fig1.tight_layout()
        st.set_y(0.98)
        fig1.subplots_adjust(top=0.92, bottom=0.08)
        ax1.legend(legendline, labels, bbox_to_anchor=(2.2, 1.02, 1.05, 0.102), loc=4, borderaxespad=0)
        fig1.savefig(self.outaddress+'avg_plot.png', dpi=80)

    # def ivcurpvts(self):
    #     aclines = []
    #     x = np.linspace(-120, 20, 15)
    #     xnew = np.linspace(x.min(), x.max(), 500)
    #     fig = plt.figure(figsize=(5, 4), dpi=80)
    #     axes = fig.add_subplot(111)
    #     for pvtindex in range(len(datamain.main.aclabels)):
    #         newacy = spline(x, GV_Ac_Inc_Pvt.averg_ac_inc(datamain.main.allAcIV[pvtindex]), xnew)
    #         newiny = spline(x, GV_Ac_Inc_Pvt.averg_ac_inc(datamain.main.allInIV[pvtindex]), xnew)
    #         line, = axes.plot(xnew, newacy, color=datamain.main.colors[pvtindex])
    #         axes.plot(xnew, newiny, color=datamain.main.colors[pvtindex])
    #         aclines.append(line)
    #     axes.set_title('Activation/Inactivation IV Cur')
    #     axes.set_ylabel("I/Imax %")
    #     axes.set_xlabel('Voltage(mV)')
    #     axes.legend(labels=datamain.main.legend[0], handles=aclines)
    #     fig.savefig(self.outaddress + 'Ac_In_IV.png', dpi=80)

    # def gvcurpvts(self):
    #     inaclines = []
    #     x = np.linspace(-120, 20, 15)
    #     fig = plt.figure(figsize=(5, 4), dpi=80)
    #     axes = fig.add_subplot(111)
    #     xnew = np.linspace(x.min(), x.max(), 500)
    #     for pvtindex in range(len(datamain.main.aclabels)):
    #         newacy = spline(x, GV_Ac_Inc_Pvt.averg_ac_inc(datamain.main.allAcGV[pvtindex]), xnew)
    #         newiny = spline(x, GV_Ac_Inc_Pvt.averg_ac_inc(datamain.main.allInGV[pvtindex]), xnew)
    #         line, = axes.plot(xnew, newacy, color=datamain.main.colors[pvtindex])
    #         axes.plot(xnew, newiny, color=datamain.main.colors[pvtindex])
    #         inaclines.append(line)
    #     axes.set_title('Activation/Inactivation GV Cur')
    #     axes.set_ylabel("G/Gmax %")
    #     axes.set_xlabel('Voltage(mV)')
    #     axes.legend(labels=datamain.main.legend[0], handles=inaclines)
    #     fig.savefig(self.outaddress + 'Ac_In_GV.png', dpi=80)

    # def deactaus(self):
    #     listname = datamain.main.legend[1]
    #     x = [0, 0.5, 1, 1.5, 2.5, 3.5, 4.5, 9.5, 29.5]
    #     colors = ['g', 'b', 'darkorange', 'gold']
    #     fig = plt.figure(figsize=(5, 4), dpi=80)
    #     axes = fig.add_subplot(111)
    #     axes.errorbar(x, datamain.main.deacavglists[0], yerr=datamain.main.deacsemlists[0], label=listname[0],
    #                        color=colors[0], ecolor="thistle")
    #     axes.errorbar(x, datamain.main.deacavglists[1], yerr=datamain.main.deacsemlists[1], label=listname[1],
    #                        color=colors[1], ecolor="thistle")
    #     axes.errorbar(x, datamain.main.deacavglists[2], yerr=datamain.main.deacsemlists[2], label=listname[2],
    #                        color=colors[2], ecolor="thistle")
    #     axes.errorbar(x, datamain.main.deacavglists[3], yerr=datamain.main.deacsemlists[3], label=listname[3],
    #                        color=colors[3], ecolor="thistle")
    #     axes.legend()
    #     axes.set_ylim(0, 100)
    #     # self.axes.set_xticks(x)
    #     fig.savefig(self.outaddress + 'deau_tau.png', dpi=80)

    def curdespvts(self):
        x = [1, 2, 3, 4]
        acmaxlists=np.asarray(datamain.main.acmaxlist)
        sslmaxlists=np.asarray(datamain.main.sslmaxlist)
        compoundlist=np.asarray(datamain.main.compoundlist)
        acsemlist=np.asarray(datamain.main.acsemlist)
        sslsemlist=np.asarray(datamain.main.insemlist)
        xlabel = ["IV1", "IV2", "IV3", "IV4"]
        fig = plt.figure(figsize=(16, 12), dpi=80)
        st = fig.suptitle("Peak Current Density", fontsize="x-large")
        legendline = []
        labels = ["Max Current Density (Ac)", "Max Current Density (SSI)"]
        axes1 = fig.add_subplot(431)
        axes1.errorbar(x, acmaxlists[0], yerr=acsemlist[0], color="b", ecolor="r")
        axes1.errorbar(x, sslmaxlists[0], yerr=sslsemlist[0], color="darkorange", ecolor="g")
        line1, =axes1.plot(x, acmaxlists[0],color="b")
        line2, =axes1.plot(x, sslmaxlists[0],color="darkorange")
        axes1.set_title(compoundlist[0])
        axes1.set_xticks(x)
        axes1.set_ylim(0,200)
        axes1.text(1, 35, "Ac:"+str(self.ratio(acmaxlists[0])), size = 15)
        axes1.text(1, 15, "SSI:"+str(self.ratio(sslmaxlists[0])), size = 15)
        legendline.append(line1, )
        legendline.append(line2, )
        axes1.legend(labels=labels, handles=legendline)
        axes1.set_xticklabels(xlabel)


        axes2 = fig.add_subplot(432)
        axes2.errorbar(x, acmaxlists[1],yerr=acsemlist[1], color="b",ecolor="r")
        axes2.errorbar(x, sslmaxlists[1],yerr=sslsemlist[1], color="darkorange",ecolor="g")
        axes2.set_title(compoundlist[1])
        axes2.set_xticks(x)
        axes2.set_ylim(0, 200)
        axes2.text(1, 35, "Ac:" + str(self.ratio(acmaxlists[1])), size=15)
        axes2.text(1, 15, "SSI:" + str(self.ratio(sslmaxlists[1])), size=15)
        axes2.set_xticklabels(xlabel)

        axes3 = fig.add_subplot(433)
        axes3.errorbar(x, acmaxlists[2],yerr=acsemlist[2], color="b", ecolor="r")
        axes3.errorbar(x, sslmaxlists[2],yerr=sslsemlist[2], color="darkorange", ecolor="g")
        axes3.set_title(compoundlist[2])
        axes3.set_xticks(x)
        axes3.set_ylim(0, 200)
        axes3.text(1, 35, "Ac:" + str(self.ratio(acmaxlists[2])), size=15)
        axes3.text(1, 15, "SSI:" + str(self.ratio(sslmaxlists[2])), size=15)
        axes3.set_xticklabels(xlabel)

        axes4 = fig.add_subplot(434)
        axes4.errorbar(x, acmaxlists[3],yerr=acsemlist[3],  color="b", ecolor="r")
        axes4.errorbar(x, sslmaxlists[3],yerr=sslsemlist[3], color="darkorange", ecolor="g")
        axes4.set_title(compoundlist[3])
        axes4.set_xticks(x)
        axes4.set_ylim(0, 200)
        axes4.text(1, 35, "Ac:" + str(self.ratio(acmaxlists[3])), size=15)
        axes4.text(1, 15, "SSI:" + str(self.ratio(sslmaxlists[3])), size=15)
        axes4.set_xticklabels(xlabel)

        axes5 = fig.add_subplot(435)
        axes5.errorbar(x, acmaxlists[4],yerr=acsemlist[4],  color="b", ecolor="r")
        axes5.errorbar(x, sslmaxlists[4],yerr=sslsemlist[4], color="darkorange", ecolor="g")
        axes5.set_title(compoundlist[4])
        axes5.set_xticks(x)
        axes5.set_ylim(0, 200)
        axes5.text(1, 35, "Ac:" + str(self.ratio(acmaxlists[4])), size=15)
        axes5.text(1, 15, "SSI:" + str(self.ratio(sslmaxlists[4])), size=15)
        axes5.set_xticklabels(xlabel)

        axes6 = fig.add_subplot(436)
        axes6.errorbar(x, acmaxlists[5],yerr=acsemlist[5],  color="b", ecolor="r")
        axes6.errorbar(x, sslmaxlists[5],yerr=sslsemlist[5], color="darkorange", ecolor="g")
        axes6.set_title(compoundlist[5])
        axes6.set_xticks(x)
        axes6.set_ylim(0, 200)
        axes6.text(1, 35, "Ac:" + str(self.ratio(acmaxlists[5])), size=15)
        axes6.text(1, 15, "SSI:" + str(self.ratio(sslmaxlists[5])), size=15)
        axes6.set_xticklabels(xlabel)

        axes7 = fig.add_subplot(437)
        axes7.errorbar(x, acmaxlists[6],yerr=acsemlist[6],  color="b", ecolor="r")
        axes7.errorbar(x, sslmaxlists[6],yerr=sslsemlist[6], color="darkorange", ecolor="g")
        axes7.set_title(compoundlist[6])
        axes7.set_xticks(x)
        axes7.set_ylim(0, 200)
        axes7.text(1, 35, "Ac:" + str(self.ratio(acmaxlists[6])), size=15)
        axes7.text(1, 15, "SSI:" + str(self.ratio(sslmaxlists[6])), size=15)
        axes7.set_xticklabels(xlabel)

        axes8 = fig.add_subplot(438)
        axes8.errorbar(x, acmaxlists[7],yerr=acsemlist[7],  color="b", ecolor="r")
        axes8.errorbar(x, sslmaxlists[7],yerr=sslsemlist[7], color="darkorange", ecolor="g")
        axes8.set_title(compoundlist[7])
        axes8.set_xticks(x)
        axes8.set_ylim(0, 200)
        axes8.text(1, 35, "Ac:" + str(self.ratio(acmaxlists[7])), size=15)
        axes8.text(1, 15, "SSI:" + str(self.ratio(sslmaxlists[7])), size=15)
        axes8.set_xticklabels(xlabel)

        axes9 = fig.add_subplot(439)
        axes9.errorbar(x, acmaxlists[8],yerr=acsemlist[8],  color="b", ecolor="r")
        axes9.errorbar(x, sslmaxlists[8],yerr=sslsemlist[8], color="darkorange", ecolor="g")
        axes9.set_title(compoundlist[8])
        axes9.set_xticks(x)
        axes9.set_ylim(0, 200)
        axes9.text(1, 35, "Ac:" + str(self.ratio(acmaxlists[8])), size=15)
        axes9.text(1, 15, "SSI:" + str(self.ratio(sslmaxlists[8])), size=15)
        axes9.set_xticklabels(xlabel)

        axes10 = fig.add_subplot(4, 3, 10)
        axes10.errorbar(x, acmaxlists[9],yerr=acsemlist[9],  color="b", ecolor="r")
        axes10.errorbar(x, sslmaxlists[9],yerr=sslsemlist[9], color="darkorange", ecolor="g")
        axes10.set_title(compoundlist[9])
        axes10.set_xticks(x)
        axes10.set_ylim(0, 200)
        axes10.text(1, 35, "Ac:" + str(self.ratio(acmaxlists[9])), size=15)
        axes10.text(1, 15, "SSI:" + str(self.ratio(sslmaxlists[9])), size=15)
        axes10.set_xticklabels(xlabel)

        axes11 = fig.add_subplot(4, 3, 11)
        axes11.errorbar(x, acmaxlists[10],yerr=acsemlist[10],  color="b", ecolor="r")
        axes11.errorbar(x, sslmaxlists[10],yerr=sslsemlist[10], color="darkorange", ecolor="g")
        axes11.set_title(compoundlist[10])
        axes11.set_xticks(x)
        axes11.set_ylim(0, 200)
        axes11.text(1, 35, "Ac:" + str(self.ratio(acmaxlists[10])), size=15)
        axes11.text(1, 15, "SSI:" + str(self.ratio(sslmaxlists[10])), size=15)
        axes11.set_xticklabels(xlabel)

        axes12 = fig.add_subplot(4, 3, 12)
        axes12.errorbar(x, acmaxlists[11],yerr=acsemlist[11],  color="b", ecolor="r")
        axes12.errorbar(x, sslmaxlists[11],yerr=sslsemlist[11], color="darkorange", ecolor="g")
        axes12.set_title(compoundlist[11])
        axes12.set_xticks(x)
        axes12.set_ylim(0, 200)
        axes12.text(1, 35, "Ac:" + str(self.ratio(acmaxlists[11])), size=15)
        axes12.text(1, 15, "SSI:" + str(self.ratio(sslmaxlists[11])), size=15)
        axes12.set_xticklabels(xlabel)

        fig.tight_layout()
        st.set_y(0.95)
        fig.subplots_adjust(top=0.9, bottom=0.1)
        axes1.legend(legendline, labels, bbox_to_anchor=(2.2, 1.2, 1.0, 1.2), loc=4, borderaxespad=0)
        fig.savefig(self.outaddress+'curdens_pvt.png', dpi=80)

    def count(self):
        alldeaclist=datamain.main.alldeaclist.copy()
        allgvlist=datamain.main.allgvlist.copy()
        allcurlist=datamain.main.allcurlist.copy()
        for n,item in enumerate(alldeaclist):
            for j,items in enumerate(item):
                try:
                    if j==0:
                        alldeaclist[n][j].insert(0, datamain.main.compoundlist[n])
                        allgvlist[n][j].insert(0, datamain.main.compoundlist[n])
                        allcurlist[n][j].insert(0, datamain.main.compoundlist[n])
                    else:
                        alldeaclist[n][j].insert(0, '')
                        allgvlist[n][j].insert(0, '')
                        allcurlist[n][j].insert(0, '')
                except:
                    pass
            for i in range(4):
                f=4*i
                try:
                    alldeaclist[n][f].insert(1,'Average')
                    allgvlist[n][f].insert(1, 'Average')
                    allcurlist[n][f].insert(1, 'Average')
                except:
                    pass
                try:
                    alldeaclist[n][f + 1].insert(1, 'n')
                    allgvlist[n][f + 1].insert(1, 'n')
                    allcurlist[n][f + 1].insert(1, 'n')
                except:
                    pass
                try:
                    alldeaclist[n][f + 2].insert(1, 'STDEV')
                    allgvlist[n][f + 2].insert(1, 'STDEV')
                    allcurlist[n][f + 2].insert(1, 'STDEV')
                except:
                    pass
                try:
                    alldeaclist[n][f + 3].insert(1, 'SEM')
                    allgvlist[n][f + 3].insert(1, 'SEM')
                    allcurlist[n][f + 3].insert(1, 'SEM')
                except:
                    pass
        file = open(self.outaddress +self.description+ ' count.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(['GV'])
        writer.writerow(['','','activation','','','','','','','','','','','','','','','inactivation'])
        for item in allgvlist:
            writer.writerows(item)
        writer.writerow(['currdens'])
        writer.writerow(['', '', 'AC', '', '', '', 'SSL'])
        for item in allcurlist:
            writer.writerows(item)
        writer.writerow(['deac'])
        for item in alldeaclist:
            writer.writerows(item)
        print(4444)
        file.close()

    def normalize(self):
        title2 = ['Compound', '', 'Ac_Delta DMSO', 'Ac Delta 1uM', 'GV Delta 10uM_Ac', 'Inact_Delta DMSO',
                  'Inact_Delta 1uM', 'Inact_Delta 10uM']
        cutofflist = []
        acdomslist = datamain.main.acdomslist
        aconelist = datamain.main.aconelist
        actenlist = datamain.main.actenlist
        indomslist = datamain.main.indomslist
        inonelist = datamain.main.inonelist
        intenlist = datamain.main.intenlist
        for n in range(12):
            avg = [datamain.main.compoundlist[n], 'Average', acdomslist[n]['avg'], aconelist[n]['avg'],
                   actenlist[n]['avg'], indomslist[n]['avg'], inonelist[n]['avg'], intenlist[n]['avg']]
            indexs = ['', 'n', acdomslist[n]['n'], aconelist[n]['n'], actenlist[n]['n'], indomslist[n]['n'],
                      inonelist[n]['n'], intenlist[n]['n']]
            std = ['', 'STDEV', acdomslist[n]['std'], aconelist[n]['std'], actenlist[n]['std'], indomslist[n]['std'],
                   inonelist[n]['std'], intenlist[n]['std']]
            sem = ['', 'SEM', acdomslist[n]['sem'], aconelist[n]['sem'], actenlist[n]['sem'], indomslist[n]['sem'],
                   inonelist[n]['sem'], intenlist[n]['sem']]
            cutofflist.append(avg)
            cutofflist.append(indexs)
            cutofflist.append(std)
            cutofflist.append(sem)
        file = open(self.outaddress +self.description+ ' normalize.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(title2)
        writer.writerows(cutofflist)
        print(4444)
        file.close()

    def hitting(self):
        acdomslist = datamain.main.acdomslist
        aconelist = datamain.main.aconelist
        actenlist = datamain.main.actenlist
        indomslist = datamain.main.indomslist
        inonelist = datamain.main.inonelist
        intenlist = datamain.main.intenlist
        actendiflist = datamain.main.actendiflist
        aconediflist = datamain.main.aconediflist
        intendiflist = datamain.main.intendiflist
        inonediflist = datamain.main.inonediflist
        actenhit = self.achitcalling(actendiflist, actenlist)
        aconehit = self.achitcalling(aconediflist, aconelist)
        intenhit = self.inhitcalling(intendiflist, intenlist)
        inonehit = self.inhitcalling(inonediflist, inonelist)
        acdmsoavg = []
        aconeavg = []
        actenavg = []
        indmsoavg = []
        inoneavg = []
        intenavg = []
        for n in range(12):
            acdmsoavg.append(acdomslist[n]['avg'])
            aconeavg.append(aconelist[n]['avg'])
            actenavg.append(actenlist[n]['avg'])
            indmsoavg.append(indomslist[n]['avg'])
            inoneavg.append(inonelist[n]['avg'])
            intenavg.append(intenlist[n]['avg'])
        hitlist = []
        hitlist.append(aconeavg)
        hitlist.append(actenavg)
        hitlist.append(aconediflist)
        hitlist.append(aconehit)
        hitlist.append(actendiflist)
        hitlist.append(actenhit)
        hitlist.append(inoneavg)
        hitlist.append(intenavg)
        hitlist.append(inonediflist)
        hitlist.append(inonehit)
        hitlist.append(intendiflist)
        hitlist.append(intenhit)
        newhitlist = self.trans(hitlist)
        for n in range(12):
            newhitlist[n].insert(0, datamain.main.compoundlist[n])
        title3 = ['Compound', '2 Tier Norm Delta 1uM_Ac', '2nd (mV) Delta 10uM_Ac', 'DMSO Normalized_Delta_1uM_Ac',
                  '1uM_Ac_ Hit Calling', 'DMSO Normalized_Delta_10uM_Ac', '10uM_Ac_ Hit Calling',
                  '(mV) Normalized Delta 1uM_Inact ', '(mV) Normalized Delta 10uM_Inact',
                  'DMSO_Triple Normalized_1uM_Inact', '1uM_Inact_Hit Calling',
                  'DMSO_Triple Normalized_Delta_10uM_Inact', '10uM_Inact_Hit Calling']
        file = open(self.outaddress + self.description + ' hitting.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(title3)
        writer.writerows(newhitlist)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
