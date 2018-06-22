from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtWidgets
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
        self.avg_plot()

    def avg_plot(self):
        acylists=datamain.main.acylists
        inylists=datamain.main.inylists
        compoundlist=datamain.main.compoundlist
        x = np.linspace(-120, 20, 15)
        self.figure.hold(False)
        st = self.figure.suptitle("Mean curve of 12 compounds", fontsize="x-large")
        legendline = []
        labels = datamain.main.legend[0]
        xnew = np.linspace(x.min(), x.max(), 500)

        self.ax1 = self.figure.add_subplot(4, 3, 1)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[0][n], xnew)
            newiny = spline(x, inylists[0][n], xnew)
            line, = self.ax1.plot(xnew,newacy , color=datamain.main.colors[n])
            self.ax1.plot(xnew, newiny, color=datamain.main.colors[n])
            self.ax1.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[0]), size=12)
            self.ax1.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[0]), size=12)
            self.ax1.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[0]), size=12)
            self.ax1.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[0]), size=12)
            legendline.append(line, )
        self.ax1.set_title(compoundlist[0])
        self.ax1.set_xlabel('Voltage(mV)')

        self.ax2 = self.figure.add_subplot(432)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[1][n], xnew)
            newiny = spline(x, inylists[1][n], xnew)
            self.ax2.plot(xnew, newacy, color=datamain.main.colors[n])
            self.ax2.plot(xnew, newiny, color=datamain.main.colors[n])
            self.ax2.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[1]), size=12)
            self.ax2.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[1]), size=12)
            self.ax2.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[1]), size=12)
            self.ax2.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[1]), size=12)
        self.ax2.set_title(compoundlist[1])
        self.ax2.set_xlabel('Voltage(mV)')

        self.ax3 = self.figure.add_subplot(433)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[2][n], xnew)
            newiny = spline(x, inylists[2][n], xnew)
            self.ax3.plot(xnew, newacy, color=datamain.main.colors[n])
            self.ax3.plot(xnew, newiny, color=datamain.main.colors[n])
            self.ax3.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[2]), size=12)
            self.ax3.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[2]), size=12)
            self.ax3.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[2]), size=12)
            self.ax3.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[2]), size=12)
        self.ax3.set_title(compoundlist[2])
        self.ax3.set_xlabel('Voltage(mV)')

        self.ax4 = self.figure.add_subplot(434)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[3][n], xnew)
            newiny = spline(x, inylists[3][n], xnew)
            self.ax4.plot(xnew, newacy, color=datamain.main.colors[n])
            self.ax4.plot(xnew, newiny, color=datamain.main.colors[n])
            self.ax4.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[3]), size=12)
            self.ax4.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[3]), size=12)
            self.ax4.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[3]), size=12)
            self.ax4.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[3]), size=12)
        self.ax4.set_title(compoundlist[3])
        self.ax4.set_xlabel('Voltage(mV)')

        self.ax5 = self.figure.add_subplot(435)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[4][n], xnew)
            newiny = spline(x, inylists[4][n], xnew)
            self.ax5.plot(xnew, newacy, color=datamain.main.colors[n])
            self.ax5.plot(xnew, newiny, color=datamain.main.colors[n])
            self.ax5.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[4]), size=12)
            self.ax5.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[4]), size=12)
            self.ax5.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[4]), size=12)
            self.ax5.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[4]), size=12)
        self.ax5.set_title(compoundlist[4])
        self.ax5.set_xlabel('Voltage(mV)')

        self.ax6 = self.figure.add_subplot(436)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[5][n], xnew)
            newiny = spline(x, inylists[5][n], xnew)
            self.ax6.plot(xnew, newacy, color=datamain.main.colors[n])
            self.ax6.plot(xnew, newiny, color=datamain.main.colors[n])
            self.ax6.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[5]), size=12)
            self.ax6.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[5]), size=12)
            self.ax6.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[5]), size=12)
            self.ax6.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[5]), size=12)
        self.ax6.set_title(compoundlist[5])
        self.ax6.set_xlabel('Voltage(mV)')

        self.ax7 = self.figure.add_subplot(437)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[6][n], xnew)
            newiny = spline(x, inylists[6][n], xnew)
            self.ax7.plot(xnew, newacy, color=datamain.main.colors[n])
            self.ax7.plot(xnew, newiny, color=datamain.main.colors[n])
            self.ax7.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[6]), size=12)
            self.ax7.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[6]), size=12)
            self.ax7.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[6]), size=12)
            self.ax7.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[6]), size=12)
        self.ax7.set_title(compoundlist[6])
        self.ax7.set_xlabel('Voltage(mV)')

        self.ax8 = self.figure.add_subplot(438)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[7][n], xnew)
            newiny = spline(x, inylists[7][n], xnew)
            self.ax8.plot(xnew, newacy, color=datamain.main.colors[n])
            self.ax8.plot(xnew, newiny, color=datamain.main.colors[n])
            self.ax8.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[7]), size=12)
            self.ax8.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[7]), size=12)
            self.ax8.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[7]), size=12)
            self.ax8.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[7]), size=12)
        self.ax8.set_title(compoundlist[7])
        self.ax8.set_xlabel('Voltage(mV)')

        self.ax9 = self.figure.add_subplot(439)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[8][n], xnew)
            newiny = spline(x, inylists[8][n], xnew)
            self.ax9.plot(xnew, newacy, color=datamain.main.colors[n])
            self.ax9.plot(xnew, newiny, color=datamain.main.colors[n])
            self.ax9.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[8]), size=12)
            self.ax9.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[8]), size=12)
            self.ax9.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[8]), size=12)
            self.ax9.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[8]), size=12)
        self.ax9.set_title(compoundlist[8])
        self.ax9.set_xlabel('Voltage(mV)')

        self.ax10 = self.figure.add_subplot(4, 3, 10)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[9][n], xnew)
            newiny = spline(x, inylists[9][n], xnew)
            self.ax10.plot(xnew, newacy, color=datamain.main.colors[n])
            self.ax10.plot(xnew, newiny, color=datamain.main.colors[n])
            self.ax10.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[9]), size=12)
            self.ax10.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[9]), size=12)
            self.ax10.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[9]), size=12)
            self.ax10.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[9]), size=12)
        self.ax10.set_title(compoundlist[9])
        self.ax10.set_xlabel('Voltage(mV)')

        self.ax11 = self.figure.add_subplot(4, 3, 11)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[10][n], xnew)
            newiny = spline(x, inylists[10][n], xnew)
            self.ax11.plot(xnew, newacy, color=datamain.main.colors[n])
            self.ax11.plot(xnew, newiny, color=datamain.main.colors[n])
            self.ax11.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[10]), size=12)
            self.ax11.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[10]), size=12)
            self.ax11.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[10]), size=12)
            self.ax11.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[10]), size=12)
        self.ax11.set_title(compoundlist[10])
        self.ax11.set_xlabel('Voltage(mV)')

        self.ax12 = self.figure.add_subplot(4, 3, 12)
        for n in range(len(acylists[0])):
            newacy = spline(x, acylists[11][n], xnew)
            newiny = spline(x, inylists[11][n], xnew)
            self.ax12.plot(xnew, newacy, color=datamain.main.colors[n])
            self.ax12.plot(xnew, newiny, color=datamain.main.colors[n])
            self.ax12.text(-20, 50, "10um_ac:" + str("%.2f" % datamain.main.actendiflist[11]), size=12)
            self.ax12.text(-20, 30, "1um_ac:" + str("%.2f" % datamain.main.aconediflist[11]), size=12)
            self.ax12.text(-120, 50, "10um_in:" + str("%.2f" % datamain.main.intendiflist[11]), size=12)
            self.ax12.text(-120, 30, "1um_in:" + str("%.2f" % datamain.main.inonediflist[11]), size=12)
        self.ax12.set_title(compoundlist[11])
        self.ax12.set_xlabel('Voltage(mV)')

        self.figure.tight_layout()
        st.set_y(0.98)
        self.figure.subplots_adjust(top=0.92, bottom=0.08)
        self.ax1.legend(legendline, labels, bbox_to_anchor=(2.2, 1.02, 1.05, 0.102), loc=4, borderaxespad=0)
        self.draw()





class avgplot(QMainWindow,Ui_Dig):
    def __init__(self):
        super(avgplot,self).__init__()
        self.resize(1021,700)
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

