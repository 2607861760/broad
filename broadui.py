# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'broadui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1067, 883)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1030, 800))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(1018, 800))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 1001, 261))
        self.groupBox.setObjectName("groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 951, 191))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(474)
        self.tableWidget.verticalHeader().setVisible(False)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 290, 1001, 371))
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_2.setGeometry(QtCore.QRect(40, 30, 531, 321))
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(250, 70, 180, 40))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(250, 120, 180, 40))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(250, 170, 180, 40))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(260, 220, 180, 40))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(260, 270, 180, 40))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.IVJ = QtWidgets.QSpinBox(self.widget_2)
        self.IVJ.setGeometry(QtCore.QRect(450, 70, 64, 40))
        self.IVJ.setMaximum(1000)
        self.IVJ.setObjectName("IVJ")
        self.Seal = QtWidgets.QSpinBox(self.widget_2)
        self.Seal.setGeometry(QtCore.QRect(450, 120, 64, 40))
        self.Seal.setMaximum(1000)
        self.Seal.setObjectName("Seal")
        self.Peak = QtWidgets.QSpinBox(self.widget_2)
        self.Peak.setGeometry(QtCore.QRect(450, 170, 64, 40))
        self.Peak.setMaximum(1000)
        self.Peak.setObjectName("Peak")
        self.Pre = QtWidgets.QSpinBox(self.widget_2)
        self.Pre.setGeometry(QtCore.QRect(450, 220, 64, 40))
        self.Pre.setMaximum(1000)
        self.Pre.setObjectName("Pre")
        self.Steady = QtWidgets.QSpinBox(self.widget_2)
        self.Steady.setGeometry(QtCore.QRect(450, 270, 64, 40))
        self.Steady.setMaximum(1000)
        self.Steady.setObjectName("Steady")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 141, 40))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.wed1 = QtWidgets.QDoubleSpinBox(self.widget_2)
        self.wed1.setGeometry(QtCore.QRect(160, 20, 64, 40))
        self.wed1.setObjectName("wed1")
        self.wed2 = QtWidgets.QDoubleSpinBox(self.widget_2)
        self.wed2.setGeometry(QtCore.QRect(160, 70, 64, 40))
        self.wed2.setObjectName("wed2")
        self.wed3 = QtWidgets.QDoubleSpinBox(self.widget_2)
        self.wed3.setGeometry(QtCore.QRect(160, 120, 64, 40))
        self.wed3.setObjectName("wed3")
        self.wed4 = QtWidgets.QDoubleSpinBox(self.widget_2)
        self.wed4.setGeometry(QtCore.QRect(160, 170, 64, 40))
        self.wed4.setObjectName("wed4")
        self.wed5 = QtWidgets.QDoubleSpinBox(self.widget_2)
        self.wed5.setGeometry(QtCore.QRect(160, 220, 64, 40))
        self.wed5.setObjectName("wed5")
        self.wed6 = QtWidgets.QDoubleSpinBox(self.widget_2)
        self.wed6.setGeometry(QtCore.QRect(160, 270, 64, 40))
        self.wed6.setObjectName("wed6")
        self.widget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_3.setGeometry(QtCore.QRect(590, 30, 381, 321))
        self.widget_3.setObjectName("widget_3")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(85, 220, 81, 40))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.compoundqc = QtWidgets.QLineEdit(self.widget_3)
        self.compoundqc.setGeometry(QtCore.QRect(190, 220, 171, 40))
        self.compoundqc.setObjectName("compoundqc")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(0, 170, 171, 40))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.curdenqc = QtWidgets.QLineEdit(self.widget_3)
        self.curdenqc.setGeometry(QtCore.QRect(190, 170, 171, 40))
        self.curdenqc.setObjectName("curdenqc")
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setGeometry(QtCore.QRect(0, 270, 171, 40))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.address = QtWidgets.QLineEdit(self.widget_3)
        self.address.setGeometry(QtCore.QRect(190, 270, 171, 40))
        self.address.setObjectName("address")
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(0, 120, 171, 40))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.deacqc = QtWidgets.QLineEdit(self.widget_3)
        self.deacqc.setGeometry(QtCore.QRect(190, 120, 171, 40))
        self.deacqc.setObjectName("deacqc")
        self.label_11 = QtWidgets.QLabel(self.widget_3)
        self.label_11.setGeometry(QtCore.QRect(0, 70, 171, 40))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.widget_3)
        self.label_12.setGeometry(QtCore.QRect(0, 20, 171, 40))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.cutoff = QtWidgets.QLineEdit(self.widget_3)
        self.cutoff.setGeometry(QtCore.QRect(190, 20, 171, 40))
        self.cutoff.setObjectName("cutoff")
        self.trim = QtWidgets.QLineEdit(self.widget_3)
        self.trim.setGeometry(QtCore.QRect(190, 70, 171, 40))
        self.trim.setObjectName("trim")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 680, 1001, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.run = QtWidgets.QPushButton(self.groupBox_3)
        self.run.setGeometry(QtCore.QRect(80, 50, 75, 30))
        self.run.setObjectName("run")
        self.cur = QtWidgets.QPushButton(self.groupBox_3)
        self.cur.setGeometry(QtCore.QRect(200, 50, 91, 30))
        self.cur.setObjectName("cur")
        self.avg_plot = QtWidgets.QPushButton(self.groupBox_3)
        self.avg_plot.setGeometry(QtCore.QRect(340, 50, 91, 30))
        self.avg_plot.setObjectName("avg_plot")
        self.curdes_pvt = QtWidgets.QPushButton(self.groupBox_3)
        self.curdes_pvt.setGeometry(QtCore.QRect(480, 50, 91, 30))
        self.curdes_pvt.setObjectName("curdes_pvt")
        self.deac = QtWidgets.QPushButton(self.groupBox_3)
        self.deac.setGeometry(QtCore.QRect(620, 50, 91, 30))
        self.deac.setObjectName("deac")
        self.report = QtWidgets.QPushButton(self.groupBox_3)
        self.report.setGeometry(QtCore.QRect(760, 50, 91, 30))
        self.report.setObjectName("report")
        self.horizontalLayout.addWidget(self.widget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1067, 23))
        self.menubar.setObjectName("menubar")
        self.menuTool = QtWidgets.QMenu(self.menubar)
        self.menuTool.setObjectName("menuTool")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInput_File = QtWidgets.QAction(MainWindow)
        self.actionInput_File.setObjectName("actionInput_File")
        self.menuTool.addAction(self.actionInput_File)
        self.menubar.addAction(self.menuTool.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.wed1.setValue(5)
        self.wed2.setValue(2)
        self.wed3.setValue(1)
        self.wed4.setValue(1)
        self.wed5.setValue(0.5)
        self.wed6.setValue(0.5)
        self.IVJ.setValue(60)
        self.Seal.setValue(500)
        self.Peak.setValue(200)
        self.Pre.setValue(100)
        self.Steady.setValue(15)
        self.cutoff.setText('2')
        self.trim.setText('0.1')
        self.deacqc.setText('7')
        self.curdenqc.setText('7')
        self.compoundqc.setText('8')

        self.cur.setEnabled(False)
        self.avg_plot.setEnabled(False)
        self.curdes_pvt.setEnabled(False)
        self.deac.setEnabled(False)
        self.report.setEnabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "File"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "FileName(Data_IV)"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "FileName(Data_PM)"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Setting"))
        self.label.setText(_translate("MainWindow", "IV jump （%）"))
        self.label_2.setText(_translate("MainWindow", "Seal Resistance（mOhm）"))
        self.label_3.setText(_translate("MainWindow", "Peak current（pA）"))
        self.label_4.setText(_translate("MainWindow", "Pre-pulse Leak current（pA）"))
        self.label_5.setText(_translate("MainWindow", "Steady State Leak current（%）"))
        self.label_6.setText(_translate("MainWindow", "Weight Distribution"))
        self.label_7.setText(_translate("MainWindow", "compound qc"))
        self.label_8.setText(_translate("MainWindow", "curdens qc"))
        self.label_9.setText(_translate("MainWindow", "Output Address"))
        self.label_10.setText(_translate("MainWindow", "deac qc"))
        self.label_11.setText(_translate("MainWindow", "Trim Mean Percentage"))
        self.label_12.setText(_translate("MainWindow", "Capacitance cutoff"))
        self.groupBox_3.setTitle(_translate("MainWindow", "operation"))
        self.run.setText(_translate("MainWindow", "Run"))
        self.cur.setText(_translate("MainWindow", "General"))
        self.avg_plot.setText(_translate("MainWindow", "avg_plot"))
        self.curdes_pvt.setText(_translate("MainWindow", "curdes_pvt"))
        self.deac.setText(_translate("MainWindow", "deac_tau"))
        self.report.setText(_translate("MainWindow", "report"))
        self.menuTool.setTitle(_translate("MainWindow", "Tool"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionInput_File.setText(_translate("MainWindow", "Input File"))
