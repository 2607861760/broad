from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import datamain
from sencond import Ui_Dig
from scipy.interpolate import spline
import numpy as np


class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=16, height=12, dpi=80):
        fig = Figure(figsize=(width, height), dpi=dpi)



        FigureCanvas.__init__(self, fig)  # 初始化父类
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

# class deac1(MyMplCanvas):
#     def plot(self):
#
#         listname = ["Pre-DMSO_PM1", "DMSO_Ac_PM2", "1uM_Ac_PM3", "10uM_Ac_PM4"]
#         x = np.linspace(0, 8, 9)
#         colors = ['g', 'b', 'darkorange', 'gold']
#         self.axes.plot(x, main.main.avglists[0], label=listname[0], color=colors[0])
#         self.axes.plot(x, main.main.avglists[1], label=listname[1], color=colors[1])
#         self.axes.plot(x, main.main.avglists[2], label=listname[2], color=colors[2])
#         self.axes.plot(x, main.main.avglists[3], label=listname[3], color=colors[3])
#         self.axes.set_xticks(x, ['0', '0.5', '1', '1.5', '2.5', '3.5', '4.5', '9.5', '29.5'])
#         self.axes.legend()





# class deac2(MyMplCanvas):
#     def plot(self):
#         self.axes = self.figure.add_subplot(111)
#         listname = ["Pre-DMSO_PM1", "DMSO_Ac_PM2", "1uM_Ac_PM3", "10uM_Ac_PM4"]
#         x = [0, 0.5, 1, 1.5, 2.5, 3.5, 4.5, 9.5, 29.5]
#         colors = ['g', 'b', 'darkorange', 'gold']
#         self.axes.errorbar(x, datamain.main.deacavglists[0], yerr=datamain.main.deacsemlists[0], label=listname[0], color=colors[0], ecolor="thistle")
#         self.axes.errorbar(x, datamain.main.deacavglists[1], yerr=datamain.main.deacsemlists[1], label=listname[1], color=colors[1], ecolor="thistle")
#         self.axes.errorbar(x, datamain.main.deacavglists[2], yerr=datamain.main.deacsemlists[2], label=listname[2], color=colors[2], ecolor="thistle")
#         self.axes.errorbar(x, datamain.main.deacavglists[3], yerr=datamain.main.deacsemlists[3], label=listname[3], color=colors[3], ecolor="thistle")
#         self.axes.legend()
#         self.axes.set_ylim(0,100)
#         self.axes.set_xlabel('TIME(ms)')
#         self.figure.tight_layout()
#         # st.set_y(0.98)
#         self.figure.subplots_adjust(top=0.92, bottom=0.08)
#         self.draw()

class deac3(MyMplCanvas):
    def plot(self):
        listname = datamain.main.legend[1]
        x = [0, 0.5, 1, 1.5, 2.5, 3.5, 4.5, 9.5, 29.5]
        colors = ['g', 'b', 'darkorange', 'gold']
        st = self.figure.suptitle("Deactivation Kinetics Curve", fontsize="x-large")
        self.ax1 = self.figure.add_subplot(4, 3, 1)
        self.ax1.errorbar(x, datamain.main.deacallavglist[0][0], yerr=datamain.main.deacallsemlist[0][0],
                       label=listname[0],
                       color=colors[0], ecolor="thistle")
        self.ax1.errorbar(x, datamain.main.deacallavglist[1][0], yerr=datamain.main.deacallsemlist[1][0],
                       label=listname[1],
                       color=colors[1], ecolor="thistle")
        self.ax1.errorbar(x, datamain.main.deacallavglist[2][0], yerr=datamain.main.deacallsemlist[2][0],
                       label=listname[2],
                       color=colors[2], ecolor="thistle")
        self.ax1.errorbar(x, datamain.main.deacallavglist[3][0], yerr=datamain.main.deacallsemlist[3][0],
                       label=listname[3],
                       color=colors[3], ecolor="thistle")
        self.ax1.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][0]), size=12)
        self.ax1.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][0]), size=12)
        self.ax1.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][0]), size=12)
        self.ax1.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][0]), size=12)
        self.ax1.legend(bbox_to_anchor=(2.2, 1.02, 1.05, 0.102), loc=4, borderaxespad=0)
        self.ax1.set_ylim(0, 100)
        self.ax1.set_xlabel('TIME(ms)')

        self.ax2 = self.figure.add_subplot(4, 3, 2)
        self.ax2.errorbar(x, datamain.main.deacallavglist[0][1], yerr=datamain.main.deacallsemlist[0][1],
                          label=listname[0],
                          color=colors[0], ecolor="thistle")
        self.ax2.errorbar(x, datamain.main.deacallavglist[1][1], yerr=datamain.main.deacallsemlist[1][1],
                          label=listname[1],
                          color=colors[1], ecolor="thistle")
        self.ax2.errorbar(x, datamain.main.deacallavglist[2][1], yerr=datamain.main.deacallsemlist[2][1],
                          label=listname[2],
                          color=colors[2], ecolor="thistle")
        self.ax2.errorbar(x, datamain.main.deacallavglist[3][1], yerr=datamain.main.deacallsemlist[3][1],
                          label=listname[3],
                          color=colors[3], ecolor="thistle")
        self.ax2.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][1]), size=12)
        self.ax2.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][1]), size=12)
        self.ax2.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][1]), size=12)
        self.ax2.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][1]), size=12)
        self.ax2.set_ylim(0, 100)
        self.ax2.set_xlabel('TIME(ms)')

        self.ax3 = self.figure.add_subplot(4, 3, 3)
        self.ax3.errorbar(x, datamain.main.deacallavglist[0][2], yerr=datamain.main.deacallsemlist[0][2],
                         label=listname[0],
                         color=colors[0], ecolor="thistle")
        self.ax3.errorbar(x, datamain.main.deacallavglist[1][2], yerr=datamain.main.deacallsemlist[1][2],
                         label=listname[1],
                         color=colors[1], ecolor="thistle")
        self.ax3.errorbar(x, datamain.main.deacallavglist[2][2], yerr=datamain.main.deacallsemlist[2][2],
                         label=listname[2],
                         color=colors[2], ecolor="thistle")
        self.ax3.errorbar(x, datamain.main.deacallavglist[3][2], yerr=datamain.main.deacallsemlist[3][2],
                         label=listname[3],
                         color=colors[3], ecolor="thistle")
        self.ax3.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][2]), size=12)
        self.ax3.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][2]), size=12)
        self.ax3.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][2]), size=12)
        self.ax3.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][2]), size=12)
        self.ax3.set_ylim(0, 100)
        self.ax3.set_xlabel('TIME(ms)')

        self.ax4 = self.figure.add_subplot(4, 3, 4)
        self.ax4.errorbar(x, datamain.main.deacallavglist[0][3], yerr=datamain.main.deacallsemlist[0][3],
                          label=listname[0],
                          color=colors[0], ecolor="thistle")
        self.ax4.errorbar(x, datamain.main.deacallavglist[1][3], yerr=datamain.main.deacallsemlist[1][3],
                          label=listname[1],
                          color=colors[1], ecolor="thistle")
        self.ax4.errorbar(x, datamain.main.deacallavglist[2][3], yerr=datamain.main.deacallsemlist[2][3],
                          label=listname[2],
                          color=colors[2], ecolor="thistle")
        self.ax4.errorbar(x, datamain.main.deacallavglist[3][3], yerr=datamain.main.deacallsemlist[3][3],
                          label=listname[3],
                          color=colors[3], ecolor="thistle")
        self.ax4.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][3]), size=12)
        self.ax4.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][3]), size=12)
        self.ax4.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][3]), size=12)
        self.ax4.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][3]), size=12)
        self.ax4.set_ylim(0, 100)
        self.ax4.set_xlabel('TIME(ms)')

        self.ax5 = self.figure.add_subplot(4, 3, 5)
        self.ax5.errorbar(x, datamain.main.deacallavglist[0][4], yerr=datamain.main.deacallsemlist[0][4],
                         label=listname[0],
                         color=colors[0], ecolor="thistle")
        self.ax5.errorbar(x, datamain.main.deacallavglist[1][4], yerr=datamain.main.deacallsemlist[1][4],
                         label=listname[1],
                         color=colors[1], ecolor="thistle")
        self.ax5.errorbar(x, datamain.main.deacallavglist[2][4], yerr=datamain.main.deacallsemlist[2][4],
                         label=listname[2],
                         color=colors[2], ecolor="thistle")
        self.ax5.errorbar(x, datamain.main.deacallavglist[3][4], yerr=datamain.main.deacallsemlist[3][4],
                         label=listname[3],
                         color=colors[3], ecolor="thistle")
        self.ax5.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][4]), size=12)
        self.ax5.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][4]), size=12)
        self.ax5.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][4]), size=12)
        self.ax5.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][4]), size=12)
        self.ax5.set_ylim(0, 100)
        self.ax5.set_xlabel('TIME(ms)')

        self.ax6 = self.figure.add_subplot(4, 3, 6)
        self.ax6.errorbar(x, datamain.main.deacallavglist[0][5], yerr=datamain.main.deacallsemlist[0][5],
                         label=listname[0],
                         color=colors[0], ecolor="thistle")
        self.ax6.errorbar(x, datamain.main.deacallavglist[1][5], yerr=datamain.main.deacallsemlist[1][5],
                         label=listname[1],
                         color=colors[1], ecolor="thistle")
        self.ax6.errorbar(x, datamain.main.deacallavglist[2][5], yerr=datamain.main.deacallsemlist[2][5],
                         label=listname[2],
                         color=colors[2], ecolor="thistle")
        self.ax6.errorbar(x, datamain.main.deacallavglist[3][5], yerr=datamain.main.deacallsemlist[3][5],
                         label=listname[3],
                         color=colors[3], ecolor="thistle")
        self.ax6.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][5]), size=12)
        self.ax6.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][5]), size=12)
        self.ax6.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][5]), size=12)
        self.ax6.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][5]), size=12)
        self.ax6.set_ylim(0, 100)
        self.ax6.set_xlabel('TIME(ms)')

        self.ax7 = self.figure.add_subplot(4, 3, 7)
        self.ax7.errorbar(x, datamain.main.deacallavglist[0][6], yerr=datamain.main.deacallsemlist[0][6],
                         label=listname[0],
                         color=colors[0], ecolor="thistle")
        self.ax7.errorbar(x, datamain.main.deacallavglist[1][6], yerr=datamain.main.deacallsemlist[1][6],
                         label=listname[1],
                         color=colors[1], ecolor="thistle")
        self.ax7.errorbar(x, datamain.main.deacallavglist[2][6], yerr=datamain.main.deacallsemlist[2][6],
                         label=listname[2],
                         color=colors[2], ecolor="thistle")
        self.ax7.errorbar(x, datamain.main.deacallavglist[3][6], yerr=datamain.main.deacallsemlist[3][6],
                         label=listname[3],
                         color=colors[3], ecolor="thistle")
        self.ax7.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][6]), size=12)
        self.ax7.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][6]), size=12)
        self.ax7.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][6]), size=12)
        self.ax7.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][6]), size=12)
        self.ax7.legend()
        self.ax7.set_ylim(0, 100)
        self.ax7.set_xlabel('TIME(ms)')

        self.ax8 = self.figure.add_subplot(4, 3, 8)
        self.ax8.errorbar(x, datamain.main.deacallavglist[0][7], yerr=datamain.main.deacallsemlist[0][7],
                         label=listname[0],
                         color=colors[0], ecolor="thistle")
        self.ax8.errorbar(x, datamain.main.deacallavglist[1][7], yerr=datamain.main.deacallsemlist[1][7],
                         label=listname[1],
                         color=colors[1], ecolor="thistle")
        self.ax8.errorbar(x, datamain.main.deacallavglist[2][7], yerr=datamain.main.deacallsemlist[2][7],
                         label=listname[2],
                         color=colors[2], ecolor="thistle")
        self.ax8.errorbar(x, datamain.main.deacallavglist[3][7], yerr=datamain.main.deacallsemlist[3][7],
                         label=listname[3],
                         color=colors[3], ecolor="thistle")
        self.ax8.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][7]), size=12)
        self.ax8.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][7]), size=12)
        self.ax8.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][7]), size=12)
        self.ax8.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][7]), size=12)
        self.ax8.set_ylim(0, 100)
        self.ax8.set_xlabel('TIME(ms)')

        self.ax9 = self.figure.add_subplot(4, 3, 9)
        self.ax9.errorbar(x, datamain.main.deacallavglist[0][8], yerr=datamain.main.deacallsemlist[0][8],
                         label=listname[0],
                         color=colors[0], ecolor="thistle")
        self.ax9.errorbar(x, datamain.main.deacallavglist[1][8], yerr=datamain.main.deacallsemlist[1][8],
                         label=listname[1],
                         color=colors[1], ecolor="thistle")
        self.ax9.errorbar(x, datamain.main.deacallavglist[2][8], yerr=datamain.main.deacallsemlist[2][8],
                         label=listname[2],
                         color=colors[2], ecolor="thistle")
        self.ax9.errorbar(x, datamain.main.deacallavglist[3][8], yerr=datamain.main.deacallsemlist[3][8],
                         label=listname[3],
                         color=colors[3], ecolor="thistle")
        self.ax9.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][8]), size=12)
        self.ax9.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][8]), size=12)
        self.ax9.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][8]), size=12)
        self.ax9.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][8]), size=12)
        self.ax9.set_ylim(0, 100)
        self.ax9.set_xlabel('TIME(ms)')

        self.ax10 = self.figure.add_subplot(4, 3, 10)
        self.ax10.errorbar(x, datamain.main.deacallavglist[0][9], yerr=datamain.main.deacallsemlist[0][9],
                          label=listname[0],
                          color=colors[0], ecolor="thistle")
        self.ax10.errorbar(x, datamain.main.deacallavglist[1][9], yerr=datamain.main.deacallsemlist[1][9],
                          label=listname[1],
                          color=colors[1], ecolor="thistle")
        self.ax10.errorbar(x, datamain.main.deacallavglist[2][9], yerr=datamain.main.deacallsemlist[2][9],
                          label=listname[2],
                          color=colors[2], ecolor="thistle")
        self.ax10.errorbar(x, datamain.main.deacallavglist[3][9], yerr=datamain.main.deacallsemlist[3][9],
                          label=listname[3],
                          color=colors[3], ecolor="thistle")
        self.ax10.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][9]), size=12)
        self.ax10.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][9]), size=12)
        self.ax10.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][9]), size=12)
        self.ax10.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][9]), size=12)
        self.ax10.set_ylim(0, 100)
        self.ax10.set_xlabel('TIME(ms)')

        self.ax11 = self.figure.add_subplot(4, 3, 11)
        self.ax11.errorbar(x, datamain.main.deacallavglist[0][10], yerr=datamain.main.deacallsemlist[0][11],
                          label=listname[0],
                          color=colors[0], ecolor="thistle")
        self.ax11.errorbar(x, datamain.main.deacallavglist[1][10], yerr=datamain.main.deacallsemlist[1][11],
                          label=listname[1],
                          color=colors[1], ecolor="thistle")
        self.ax11.errorbar(x, datamain.main.deacallavglist[2][10], yerr=datamain.main.deacallsemlist[2][11],
                          label=listname[2],
                          color=colors[2], ecolor="thistle")
        self.ax11.errorbar(x, datamain.main.deacallavglist[3][10], yerr=datamain.main.deacallsemlist[3][11],
                          label=listname[3],
                          color=colors[3], ecolor="thistle")
        self.ax11.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][10]), size=12)
        self.ax11.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][10]), size=12)
        self.ax11.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][10]), size=12)
        self.ax11.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][10]), size=12)
        self.ax11.set_ylim(0, 100)
        self.ax11.set_xlabel('TIME(ms)')

        self.ax12 = self.figure.add_subplot(4, 3, 12)
        self.ax12.errorbar(x, datamain.main.deacallavglist[0][11], yerr=datamain.main.deacallsemlist[0][11],
                          label=listname[0],
                          color=colors[0], ecolor="thistle")
        self.ax12.errorbar(x, datamain.main.deacallavglist[1][11], yerr=datamain.main.deacallsemlist[1][11],
                          label=listname[1],
                          color=colors[1], ecolor="thistle")
        self.ax12.errorbar(x, datamain.main.deacallavglist[2][11], yerr=datamain.main.deacallsemlist[2][11],
                          label=listname[2],
                          color=colors[2], ecolor="thistle")
        self.ax12.errorbar(x, datamain.main.deacallavglist[3][11], yerr=datamain.main.deacallsemlist[3][11],
                          label=listname[3],
                          color=colors[3], ecolor="thistle")
        self.ax12.text(5, 90, "Tau1:" + str("%.2f" % datamain.main.deacdiflist[0][11]), size=12)
        self.ax12.text(5, 80, "Tau2:" + str("%.2f" % datamain.main.deacdiflist[1][11]), size=12)
        self.ax12.text(5, 70, "Tau3:" + str("%.2f" % datamain.main.deacdiflist[2][11]), size=12)
        self.ax12.text(5, 60, "Tau4:" + str("%.2f" % datamain.main.deacdiflist[3][11]), size=12)
        self.ax12.set_ylim(0, 100)
        self.ax12.set_xlabel('TIME(ms)')

        self.figure.tight_layout()
        st.set_y(0.98)
        self.figure.subplots_adjust(top=0.92, bottom=0.08)
        # self.ax1.legend(legendline, labels, bbox_to_anchor=(2.2, 1.02, 1.05, 0.102), loc=4, borderaxespad=0)
        self.draw()


class deactau(QMainWindow,Ui_Dig):
    def __init__(self):
        super(deactau,self).__init__()
        self.resize(1400,900)
        self.center()

    def center(self):  #窗口居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        try:
            # self.setupUi(self)
            # self.first_widget = QWidget(self.main_widget)
            # self.first_widget.setGeometry(QtCore.QRect(10, 10, 400, 280))
            # l = QVBoxLayout(self.first_widget)
            # dc = deac2(self.main_widget, width=5, height=4, dpi=80)
            # l.addWidget(dc)
            # self.second_widget= QWidget(self.main_widget)
            # self.second_widget.setGeometry(QtCore.QRect(10, 300, 1000, 800))
            # ls = QVBoxLayout(self.second_widget)
            # sc = deac3(self.second_widget, width=16, height=12, dpi=80)
            # ls.addWidget(sc)
            self.setupUi(self)
            l = QVBoxLayout(self.main_widget)
            sc = deac3(self.main_widget, width=16, height=12, dpi=80)
            l.addWidget(sc)

        except Exception as e:
            print('Got an error ', e)

