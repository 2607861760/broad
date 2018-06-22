from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import datamain
import numpy as np
from sencond import Ui_Dig
from scipy.interpolate import spline


class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=16, height=12, dpi=80):
        fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, fig)  # 初始化父类
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        fig.clear()
        self.figure.hold(False)
        self.curdes_pvt()


    def curdes_pvt(self):
        def ratio(list):
            value=list[3]/list[1]
            newvalue=float("%.2f" % value)
            return newvalue
        x = [1, 2, 3, 4]
        acmaxlists=np.asarray(datamain.main.acmaxlist)
        sslmaxlists=np.asarray(datamain.main.sslmaxlist)
        compoundlist=np.asarray(datamain.main.compoundlist)
        acsemlist=np.asarray(datamain.main.acsemlist)
        sslsemlist=np.asarray(datamain.main.insemlist)
        self.figure.hold(False)
        xlabel = ["IV1", "IV2", "IV3", "IV4"]
        st = self.figure.suptitle("Peak Current Density", fontsize="x-large")
        legendline = []
        labels = ["Max Current Density (Ac)", "Max Current Density (SSI)"]
        self.axes1 = self.figure.add_subplot(431)
        self.axes1.errorbar(x, acmaxlists[0], yerr=acsemlist[0], color="b", ecolor="r")
        self.axes1.errorbar(x, sslmaxlists[0], yerr=sslsemlist[0], color="darkorange", ecolor="g")
        line1, =self.axes1.plot(x, acmaxlists[0],color="b")
        line2, =self.axes1.plot(x, sslmaxlists[0],color="darkorange")
        self.axes1.set_title(compoundlist[0])
        self.axes1.set_xticks(x)
        self.axes1.set_ylim(0,200)
        self.axes1.text(1, 35, "Ac:"+str(ratio(acmaxlists[0])), size = 15)
        self.axes1.text(1, 15, "SSI:"+str(ratio(sslmaxlists[0])), size = 15)
        legendline.append(line1, )
        legendline.append(line2, )
        self.axes1.legend(labels=labels, handles=legendline)
        self.axes1.set_xticklabels(xlabel)

        self.axes2 = self.figure.add_subplot(432)
        self.axes2.errorbar(x, acmaxlists[1],yerr=acsemlist[1], color="b",ecolor="r")
        self.axes2.errorbar(x, sslmaxlists[1],yerr=sslsemlist[1], color="darkorange",ecolor="g")
        self.axes2.set_title(compoundlist[1])
        self.axes2.set_xticks(x)
        self.axes2.set_ylim(0, 200)
        self.axes2.text(1, 35, "Ac:" + str(ratio(acmaxlists[1])), size=15)
        self.axes2.text(1, 15, "SSI:" + str(ratio(sslmaxlists[1])), size=15)
        self.axes2.set_xticklabels(xlabel)

        self.axes3 = self.figure.add_subplot(433)
        self.axes3.errorbar(x, acmaxlists[2],yerr=acsemlist[2], color="b", ecolor="r")
        self.axes3.errorbar(x, sslmaxlists[2],yerr=sslsemlist[2], color="darkorange", ecolor="g")
        self.axes3.set_title(compoundlist[2])
        self.axes3.set_xticks(x)
        self.axes3.set_ylim(0, 200)
        self.axes3.text(1, 35, "Ac:" + str(ratio(acmaxlists[2])), size=15)
        self.axes3.text(1, 15, "SSI:" + str(ratio(sslmaxlists[2])), size=15)
        self.axes3.set_xticklabels(xlabel)

        self.axes4 = self.figure.add_subplot(434)
        self.axes4.errorbar(x, acmaxlists[3],yerr=acsemlist[3],  color="b", ecolor="r")
        self.axes4.errorbar(x, sslmaxlists[3],yerr=sslsemlist[3], color="darkorange", ecolor="g")
        self.axes4.set_title(compoundlist[3])
        self.axes4.set_xticks(x)
        self.axes4.set_ylim(0, 200)
        self.axes4.text(1, 35, "Ac:" + str(ratio(acmaxlists[3])), size=15)
        self.axes4.text(1, 15, "SSI:" + str(ratio(sslmaxlists[3])), size=15)
        self.axes4.set_xticklabels(xlabel)

        self.axes5 = self.figure.add_subplot(435)
        self.axes5.errorbar(x, acmaxlists[4],yerr=acsemlist[4],  color="b", ecolor="r")
        self.axes5.errorbar(x, sslmaxlists[4],yerr=sslsemlist[4], color="darkorange", ecolor="g")
        self.axes5.set_title(compoundlist[4])
        self.axes5.set_xticks(x)
        self.axes5.set_ylim(0, 200)
        self.axes5.text(1, 35, "Ac:" + str(ratio(acmaxlists[4])), size=15)
        self.axes5.text(1, 15, "SSI:" + str(ratio(sslmaxlists[4])), size=15)
        self.axes5.set_xticklabels(xlabel)

        self.axes6 = self.figure.add_subplot(436)
        self.axes6.errorbar(x, acmaxlists[5],yerr=acsemlist[5],  color="b", ecolor="r")
        self.axes6.errorbar(x, sslmaxlists[5],yerr=sslsemlist[5], color="darkorange", ecolor="g")
        self.axes6.set_title(compoundlist[5])
        self.axes6.set_xticks(x)
        self.axes6.set_ylim(0, 200)
        self.axes6.text(1, 35, "Ac:" + str(ratio(acmaxlists[5])), size=15)
        self.axes6.text(1, 15, "SSI:" + str(ratio(sslmaxlists[5])), size=15)
        self.axes6.set_xticklabels(xlabel)

        self.axes7 = self.figure.add_subplot(437)
        self.axes7.errorbar(x, acmaxlists[6],yerr=acsemlist[6],  color="b", ecolor="r")
        self.axes7.errorbar(x, sslmaxlists[6],yerr=sslsemlist[6], color="darkorange", ecolor="g")
        self.axes7.set_title(compoundlist[6])
        self.axes7.set_xticks(x)
        self.axes7.set_ylim(0, 200)
        self.axes7.text(1, 35, "Ac:" + str(ratio(acmaxlists[6])), size=15)
        self.axes7.text(1, 15, "SSI:" + str(ratio(sslmaxlists[6])), size=15)
        self.axes7.set_xticklabels(xlabel)

        self.axes8 = self.figure.add_subplot(438)
        self.axes8.errorbar(x, acmaxlists[7],yerr=acsemlist[7],  color="b", ecolor="r")
        self.axes8.errorbar(x, sslmaxlists[7],yerr=sslsemlist[7], color="darkorange", ecolor="g")
        self.axes8.set_title(compoundlist[7])
        self.axes8.set_xticks(x)
        self.axes8.set_ylim(0, 200)
        self.axes8.text(1, 35, "Ac:" + str(ratio(acmaxlists[7])), size=15)
        self.axes8.text(1, 15, "SSI:" + str(ratio(sslmaxlists[7])), size=15)
        self.axes8.set_xticklabels(xlabel)

        self.axes9 = self.figure.add_subplot(439)
        self.axes9.errorbar(x, acmaxlists[8],yerr=acsemlist[8],  color="b", ecolor="r")
        self.axes9.errorbar(x, sslmaxlists[8],yerr=sslsemlist[8], color="darkorange", ecolor="g")
        self.axes9.set_title(compoundlist[8])
        self.axes9.set_xticks(x)
        self.axes9.set_ylim(0, 200)
        self.axes9.text(1, 35, "Ac:" + str(ratio(acmaxlists[8])), size=15)
        self.axes9.text(1, 15, "SSI:" + str(ratio(sslmaxlists[8])), size=15)
        self.axes9.set_xticklabels(xlabel)

        self.axes10 = self.figure.add_subplot(4, 3, 10)
        self.axes10.errorbar(x, acmaxlists[9],yerr=acsemlist[9],  color="b", ecolor="r")
        self.axes10.errorbar(x, sslmaxlists[9],yerr=sslsemlist[9], color="darkorange", ecolor="g")
        self.axes10.set_title(compoundlist[9])
        self.axes10.set_xticks(x)
        self.axes10.set_ylim(0, 200)
        self.axes10.text(1, 35, "Ac:" + str(ratio(acmaxlists[9])), size=15)
        self.axes10.text(1, 15, "SSI:" + str(ratio(sslmaxlists[9])), size=15)
        self.axes10.set_xticklabels(xlabel)

        self.axes11 = self.figure.add_subplot(4, 3, 11)
        self.axes11.errorbar(x, acmaxlists[10],yerr=acsemlist[10],  color="b", ecolor="r")
        self.axes11.errorbar(x, sslmaxlists[10],yerr=sslsemlist[10], color="darkorange", ecolor="g")
        self.axes11.set_title(compoundlist[10])
        self.axes11.set_xticks(x)
        self.axes11.set_ylim(0, 200)
        self.axes11.text(1, 35, "Ac:" + str(ratio(acmaxlists[10])), size=15)
        self.axes11.text(1, 15, "SSI:" + str(ratio(sslmaxlists[10])), size=15)
        self.axes11.set_xticklabels(xlabel)

        self.axes12 = self.figure.add_subplot(4, 3, 12)
        self.axes12.errorbar(x, acmaxlists[11],yerr=acsemlist[11],  color="b", ecolor="r")
        self.axes12.errorbar(x, sslmaxlists[11],yerr=sslsemlist[11], color="darkorange", ecolor="g")
        self.axes12.set_title(compoundlist[11])
        self.axes12.set_xticks(x)
        self.axes12.set_ylim(0, 200)
        self.axes12.text(1, 35, "Ac:" + str(ratio(acmaxlists[11])), size=15)
        self.axes12.text(1, 15, "SSI:" + str(ratio(sslmaxlists[11])), size=15)
        self.axes12.set_xticklabels(xlabel)

        self.figure.tight_layout()
        st.set_y(0.95)
        self.figure.subplots_adjust(top=0.9, bottom=0.1)
        self.axes1.legend(legendline, labels, bbox_to_anchor=(2.2, 1.2, 1.0, 1.2), loc=4, borderaxespad=0)
        self.draw()





class curdespvt(QMainWindow,Ui_Dig):
    def __init__(self):
        super(curdespvt,self).__init__()
        self.resize(1400,990)
        self.center()

    def center(self):  #窗口居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        try:
            self.setupUi(self)
            l = QVBoxLayout(self.main_widget)
            sc = MyMplCanvas(self.main_widget, width=16, height=12, dpi=80)
            l.addWidget(sc)
        except Exception as e:
            print('Got an error ', e)

