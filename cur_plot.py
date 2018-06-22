from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import datamain
import numpy as np
import GV_Ac_Inc_Pvt
from sencond import Ui_Dig
from scipy.interpolate import spline


class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=16, height=12, dpi=80):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # self.axes.hold(False)


        FigureCanvas.__init__(self, fig)  # 初始化父类
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.cur()

class IVcurplot(MyMplCanvas):
    def cur(self):
        # self.xx = PdfPages('fff.pdf')
        aclines=[]
        x = np.linspace(-120, 20, 15)
        xnew = np.linspace(x.min(), x.max(), 500)
        for pvtindex in range(len(datamain.main.aclabels)):
            newacy = spline(x, GV_Ac_Inc_Pvt.averg_ac_inc(datamain.main.allAcIV[pvtindex]), xnew)
            newiny = spline(x, GV_Ac_Inc_Pvt.averg_ac_inc(datamain.main.allInIV[pvtindex]), xnew)
            line,=self.axes.plot(xnew, newacy, color=datamain.main.colors[pvtindex])
            self.axes.plot(xnew, newiny, color=datamain.main.colors[pvtindex])
            aclines.append(line)
        self.axes.set_title('Activation/Inactivation IV Cur')
        self.axes.set_ylabel("I/Imax %")
        self.axes.set_xlabel('Voltage(mV) ')
        self.axes.legend(labels=datamain.main.legend[0], handles = aclines)
        self.draw()




class GVcurplot(MyMplCanvas):
    def cur(self):
        inaclines = []
        x = np.linspace(-120, 20, 15)
        xnew = np.linspace(x.min(), x.max(), 500)
        for pvtindex in range(len(datamain.main.aclabels)):
            newacy = spline(x, GV_Ac_Inc_Pvt.averg_ac_inc(datamain.main.allAcGV[pvtindex]), xnew)
            newiny = spline(x, GV_Ac_Inc_Pvt.averg_ac_inc(datamain.main.allInGV[pvtindex]), xnew)
            line,=self.axes.plot(xnew, newacy, color=datamain.main.colors[pvtindex])
            self.axes.plot(xnew, newiny, color=datamain.main.colors[pvtindex])
            inaclines.append(line)
        self.axes.set_title('Activation/Inactivation GV Cur')
        self.axes.set_ylabel("G/Gmax %")
        self.axes.set_xlabel('Voltage(mV)')
        self.axes.legend(labels=datamain.main.legend[0], handles = inaclines)
        self.draw()

class deac2(MyMplCanvas):
    def cur(self):
        st = self.figure.suptitle("Deactivation Kinetics Curve", fontsize="x-large")
        listname = ["Pre-DMSO_PM1", "DMSO_Ac_PM2", "1uM_Ac_PM3", "10uM_Ac_PM4"]
        x = [0, 0.5, 1, 1.5, 2.5, 3.5, 4.5, 9.5, 29.5]
        colors = ['g', 'b', 'darkorange', 'gold']
        self.axes.errorbar(x, datamain.main.deacavglists[0], yerr=datamain.main.deacsemlists[0], label=listname[0], color=colors[0], ecolor="thistle")
        self.axes.errorbar(x, datamain.main.deacavglists[1], yerr=datamain.main.deacsemlists[1], label=listname[1], color=colors[1], ecolor="thistle")
        self.axes.errorbar(x, datamain.main.deacavglists[2], yerr=datamain.main.deacsemlists[2], label=listname[2], color=colors[2], ecolor="thistle")
        self.axes.errorbar(x, datamain.main.deacavglists[3], yerr=datamain.main.deacsemlists[3], label=listname[3], color=colors[3], ecolor="thistle")
        self.axes.legend()
        self.axes.set_ylim(0,100)
        self.axes.set_xlabel('TIME(ms)')
        # self.figure.tight_layout()
        # st.set_y(0.98)
        # self.figure.subplots_adjust(top=0.92, bottom=0.08)
        self.draw()



class curplot(QMainWindow,Ui_Dig):
    def __init__(self):
        super(curplot,self).__init__()
        self.resize(1000,800)
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
            sc = IVcurplot(self.main_widget, width=5, height=4, dpi=80)
            dc = GVcurplot(self.main_widget, width=5, height=4, dpi=80)
            dac = deac2(self.main_widget, width=5, height=4, dpi=80)
            l.addWidget(sc)
            l.addWidget(dc)
            l.addWidget(dac)
        except Exception as e:
            print('Got an error ', e)

