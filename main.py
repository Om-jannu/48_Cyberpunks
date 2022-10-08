import socket
import os
import subprocess, psutil
from numpy import sinc
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
from PyQt5.QtWidgets import QAbstractItemView,QApplication
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import *
import nmap
from netaddr import IPAddress
import ipcalc
from threads import indPortScan, indScheduleScan
import schedule, time
import signal

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SideMenu = QtWidgets.QFrame(self.centralwidget)
        self.SideMenu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SideMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SideMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SideMenu.setObjectName("SideMenu")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.SideMenu)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SideMenuCon = QtWidgets.QFrame(self.SideMenu)
        self.SideMenuCon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SideMenuCon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SideMenuCon.setObjectName("SideMenuCon")
        self.scheduledscan = QtWidgets.QPushButton(self.SideMenuCon)
        self.scheduledscan.setGeometry(QtCore.QRect(10, 70, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.scheduledscan.setFont(font)
        self.scheduledscan.setObjectName("scheduledscan")
        self.services = QtWidgets.QPushButton(self.SideMenuCon)
        self.services.setGeometry(QtCore.QRect(10, 110, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.services.setFont(font)
        self.services.setObjectName("services")
        self.portscanner = QtWidgets.QPushButton(self.SideMenuCon)
        self.portscanner.setGeometry(QtCore.QRect(11, 31, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.portscanner.setFont(font)
        self.portscanner.setCheckable(False)
        self.portscanner.setAutoDefault(False)
        self.portscanner.setDefault(False)
        self.portscanner.setObjectName("portscanner")
        self.horizontalLayout_2.addWidget(self.SideMenuCon)
        self.horizontalLayout.addWidget(self.SideMenu)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 10, 601, 571))
        self.stackedWidget.setObjectName("stackedWidget")
        self.PortScanner = QtWidgets.QWidget()
        self.PortScanner.setObjectName("PortScanner")
        self.frame_4 = QtWidgets.QFrame(self.PortScanner)
        self.frame_4.setGeometry(QtCore.QRect(-1, -11, 601, 611))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.tab1_3 = QtWidgets.QTabWidget(self.frame_4)
        self.tab1_3.setGeometry(QtCore.QRect(0, 50, 601, 561))
        self.tab1_3.setObjectName("tab1_3")
        self.individualScanTab = QtWidgets.QWidget()
        self.individualScanTab.setObjectName("individualScanTab")
        self.frame_5 = QtWidgets.QFrame(self.individualScanTab)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 591, 521))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.Targetlabel = QtWidgets.QLabel(self.frame_5)
        self.Targetlabel.setGeometry(QtCore.QRect(10, 0, 71, 21))
        self.Targetlabel.setObjectName("Targetlabel")
        self.ind_portinput = QtWidgets.QLineEdit(self.frame_5)
        self.ind_portinput.setGeometry(QtCore.QRect(120, 30, 151, 20))
        self.ind_portinput.setObjectName("ind_portinput")
        self.portlabel = QtWidgets.QLabel(self.frame_5)
        self.portlabel.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.portlabel.setObjectName("portlabel")
        self.ind_ScanButton = QtWidgets.QPushButton(self.frame_5)
        self.ind_ScanButton.setGeometry(QtCore.QRect(320, 70, 131, 31))
        self.ind_ScanButton.setObjectName("ind_ScanButton")
        self.tolabel_3 = QtWidgets.QLabel(self.frame_5)
        self.tolabel_3.setGeometry(QtCore.QRect(280, 30, 21, 20))
        self.tolabel_3.setMinimumSize(QtCore.QSize(0, 20))
        self.tolabel_3.setMaximumSize(QtCore.QSize(21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tolabel_3.setFont(font)
        self.tolabel_3.setObjectName("tolabel_3")
        self.Outputlabel = QtWidgets.QLabel(self.frame_5)
        self.Outputlabel.setGeometry(QtCore.QRect(10, 110, 571, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setUnderline(True)
        self.Outputlabel.setFont(font)
        self.Outputlabel.setObjectName("Outputlabel")
        self.frame = QtWidgets.QFrame(self.frame_5)
        self.frame.setGeometry(QtCore.QRect(9, 129, 581, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.indScanOpArea = QtWidgets.QTextEdit(self.frame)
        self.indScanOpArea.setGeometry(QtCore.QRect(0, 10, 581, 361))
        self.indScanOpArea.setMinimumSize(QtCore.QSize(521, 351))
        self.indScanOpArea.setObjectName("indScanOpArea")
        self.ind_portinput_2 = QtWidgets.QLineEdit(self.frame_5)
        self.ind_portinput_2.setGeometry(QtCore.QRect(300, 30, 151, 20))
        self.ind_portinput_2.setObjectName("ind_portinput_2")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 101, 21))
        self.label_2.setObjectName("label_2")
        self.ind_typeOfPortScan = QtWidgets.QComboBox(self.frame_5)
        self.ind_typeOfPortScan.setGeometry(QtCore.QRect(120, 70, 181, 31))
        self.ind_typeOfPortScan.setObjectName("ind_typeOfPortScan")
        self.ind_typeOfPortScan.addItem("")
        self.ind_typeOfPortScan.addItem("")
        self.ind_typeOfPortScan.addItem("")
        self.ind_typeOfPortScan.addItem("")
        self.ind_typeOfPortScan.addItem("")
        self.indScanIpDD = QtWidgets.QComboBox(self.frame_5)
        self.indScanIpDD.setGeometry(QtCore.QRect(120, 0, 151, 22))
        self.indScanIpDD.setObjectName("indScanIpDD")
        self.indScanIpRefreshBtn = QtWidgets.QPushButton(self.frame_5)
        self.indScanIpRefreshBtn.setGeometry(QtCore.QRect(300, 0, 151, 28))
        self.indScanIpRefreshBtn.setObjectName("indScanIpRefreshBtn")
        self.tab1_3.addTab(self.individualScanTab, "")
        self.FullScanTab = QtWidgets.QWidget()
        self.FullScanTab.setObjectName("FullScanTab")
        self.frame_6 = QtWidgets.QFrame(self.FullScanTab)
        self.frame_6.setGeometry(QtCore.QRect(-1, -1, 591, 531))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.full_targetinput_1 = QtWidgets.QLineEdit(self.frame_6)
        self.full_targetinput_1.setGeometry(QtCore.QRect(170, 10, 151, 21))
        self.full_targetinput_1.setObjectName("full_targetinput_1")
        self.Targetlabel_2 = QtWidgets.QLabel(self.frame_6)
        self.Targetlabel_2.setGeometry(QtCore.QRect(10, 10, 151, 21))
        self.Targetlabel_2.setObjectName("Targetlabel_2")
        self.full_ScanButton = QtWidgets.QPushButton(self.frame_6)
        self.full_ScanButton.setGeometry(QtCore.QRect(340, 10, 111, 51))
        self.full_ScanButton.setObjectName("full_ScanButton")
        self.Outputlabel_2 = QtWidgets.QLabel(self.frame_6)
        self.Outputlabel_2.setGeometry(QtCore.QRect(20, 70, 501, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setUnderline(True)
        self.Outputlabel_2.setFont(font)
        self.Outputlabel_2.setObjectName("Outputlabel_2")
        self.frame_11 = QtWidgets.QFrame(self.frame_6)
        self.frame_11.setGeometry(QtCore.QRect(-1, 99, 591, 431))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.fullScanOpTable = QtWidgets.QTableWidget(self.frame_11)
        self.fullScanOpTable.setGeometry(QtCore.QRect(15, 1, 571, 401))
        self.fullScanOpTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.fullScanOpTable.setObjectName("fullScanOpTable")
        self.fullScanOpTable.setColumnCount(2)
        self.fullScanOpTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.fullScanOpTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fullScanOpTable.setHorizontalHeaderItem(1, item)
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 151, 21))
        self.label_9.setObjectName("label_9")
        self.full_subnetLen = QtWidgets.QLineEdit(self.frame_6)
        self.full_subnetLen.setGeometry(QtCore.QRect(170, 40, 151, 21))
        self.full_subnetLen.setObjectName("full_subnetLen")
        self.tab1_3.addTab(self.FullScanTab, "")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(4, 20, 581, 21))
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.PortScanner)
        self.Services = QtWidgets.QWidget()
        self.Services.setObjectName("Services")
        self.frame_3 = QtWidgets.QFrame(self.Services)
        self.frame_3.setGeometry(QtCore.QRect(-1, -11, 601, 611))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.tab1 = QtWidgets.QTabWidget(self.frame_3)
        self.tab1.setGeometry(QtCore.QRect(10, 39, 591, 571))
        self.tab1.setObjectName("tab1")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame_8 = QtWidgets.QFrame(self.tab)
        self.frame_8.setGeometry(QtCore.QRect(0, 0, 581, 511))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.listServicesRefresh = QtWidgets.QPushButton(self.frame_8)
        self.listServicesRefresh.setGeometry(QtCore.QRect(170, 10, 151, 28))
        self.listServicesRefresh.setObjectName("listServicesRefresh")
        self.label = QtWidgets.QLabel(self.frame_8)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.label.setObjectName("label")
        self.listServicesTab = QtWidgets.QTableWidget(self.frame_8)
        self.listServicesTab.setGeometry(QtCore.QRect(5, 50, 571, 451))
        self.listServicesTab.setObjectName("listServicesTab")
        self.listServicesTab.setColumnCount(3)
        self.listServicesTab.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.listServicesTab.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listServicesTab.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listServicesTab.setHorizontalHeaderItem(2, item)
        self.tab1.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_9 = QtWidgets.QFrame(self.tab_2)
        self.frame_9.setGeometry(QtCore.QRect(-1, -1, 581, 541))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.editServicesTab = QtWidgets.QTableWidget(self.frame_9)
        self.editServicesTab.setGeometry(QtCore.QRect(10, 40, 521, 441))
        self.editServicesTab.setObjectName("editServicesTab")
        self.editServicesTab.setColumnCount(4)
        self.editServicesTab.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.editServicesTab.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.editServicesTab.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.editServicesTab.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.editServicesTab.setHorizontalHeaderItem(3, item)
        self.getServicesRefreshBtn = QtWidgets.QPushButton(self.frame_9)
        self.getServicesRefreshBtn.setGeometry(QtCore.QRect(20, 10, 151, 28))
        self.getServicesRefreshBtn.setObjectName("getServicesRefreshBtn")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_9)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(360, 10, 131, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.userServStatIcon = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.userServStatIcon.setObjectName("userServStatIcon")
        self.horizontalLayout_4.addWidget(self.userServStatIcon)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_9)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 10, 131, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sysServStatIcon = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.sysServStatIcon.setObjectName("sysServStatIcon")
        self.horizontalLayout_3.addWidget(self.sysServStatIcon)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.tab1.addTab(self.tab_2, "")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 531, 16))
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.Services)
        self.ScheduledScan = QtWidgets.QWidget()
        self.ScheduledScan.setObjectName("ScheduledScan")
        self.frame_7 = QtWidgets.QFrame(self.ScheduledScan)
        self.frame_7.setGeometry(QtCore.QRect(0, -10, 611, 611))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.frame_7)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 40, 601, 571))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 111, 31))
        self.label_5.setObjectName("label_5")
        self.SingSchScanBtn = QtWidgets.QPushButton(self.tab_3)
        self.SingSchScanBtn.setGeometry(QtCore.QRect(10, 140, 181, 31))
        self.SingSchScanBtn.setObjectName("SingSchScanBtn")
        self.singSchScanTarget = QtWidgets.QTextEdit(self.tab_3)
        self.singSchScanTarget.setGeometry(QtCore.QRect(150, 20, 361, 31))
        self.singSchScanTarget.setObjectName("singSchScanTarget")
        self.singSchScanTimeIntervalDD = QtWidgets.QComboBox(self.tab_3)
        self.singSchScanTimeIntervalDD.setGeometry(QtCore.QRect(150, 61, 361, 31))
        self.singSchScanTimeIntervalDD.setObjectName("singSchScanTimeIntervalDD")
        self.singSchScanTimeIntervalDD.addItem("")
        self.singSchScanTimeIntervalDD.addItem("")
        self.singSchScanTimeIntervalDD.addItem("")
        self.singSchScanTimeIntervalDD.addItem("")
        self.singSchScanTimeIntervalDD.addItem("")
        self.singSchScanTimeIntervalDD.addItem("")
        self.singSchScanTypeScanDD = QtWidgets.QComboBox(self.tab_3)
        self.singSchScanTypeScanDD.setGeometry(QtCore.QRect(150, 100, 361, 31))
        self.singSchScanTypeScanDD.setObjectName("singSchScanTypeScanDD")
        self.singSchScanTypeScanDD.addItem("")
        self.singSchScanTypeScanDD.addItem("")
        self.singSchScanTypeScanDD.addItem("")
        self.singSchScanTypeScanDD.addItem("")
        self.singSchScanTypeScanDD.addItem("")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 121, 31))
        self.label_6.setObjectName("label_6")
        self.SingSchScanOp = QtWidgets.QTextEdit(self.tab_3)
        self.SingSchScanOp.setGeometry(QtCore.QRect(0, 186, 531, 311))
        self.SingSchScanOp.setObjectName("SingSchScanOp")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 521, 21))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.ScheduledScan)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tab1_3.setCurrentIndex(0)
        self.tab1.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

                #--------------------------- my function start ----------------------------
        self.ind_portinput.setText("0")
        self.ind_portinput_2.setText("65535")
        self.indScanOpArea.setReadOnly(True)


        self.ind_portinput.setValidator(QIntValidator())
        self.ind_portinput_2.setValidator(QIntValidator())
        self.portscanner.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PortScanner))
        self.scheduledscan.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ScheduledScan))
        self.services.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Services))
        self.ind_ScanButton.clicked.connect(self.indPortScan)
        self.full_ScanButton.clicked.connect(self.fullPortScan)
        self.SingSchScanBtn.clicked.connect(self.singScheduleScan)
        self.listServicesRefresh.clicked.connect(self.servicesList)
        self.getServicesRefreshBtn.clicked.connect(self.servicesEditList)
        self.ind_typeOfPortScan.currentIndexChanged.connect(self.changePortVisibility)
        self.fullScanOpTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listServicesTab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.editServicesTab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.indScanIpRefreshBtn.clicked.connect(self.get_ip)
        self.indScanIpDD.setEditable(True)

    def changePortVisibility(self):
        if self.ind_typeOfPortScan.currentIndex()==0:
            self.ind_portinput.setText("1")
            self.ind_portinput_2.setText("1024")
            self.ind_portinput.setDisabled(True)
            self.ind_portinput_2.setDisabled(True)
        elif self.ind_typeOfPortScan.currentIndex()==1:
            self.ind_portinput.setDisabled(True)
            self.ind_portinput_2.setDisabled(True)
        elif self.ind_typeOfPortScan.currentIndex()==2:
            self.ind_portinput.setDisabled(True)
            self.ind_portinput_2.setDisabled(True)
        elif self.ind_typeOfPortScan.currentIndex()==3:
            self.ind_portinput.setText("0")
            self.ind_portinput_2.setText("65535")
            self.ind_portinput.setDisabled(False)
            self.ind_portinput_2.setDisabled(False)
        elif self.ind_typeOfPortScan.currentIndex()==4:
            self.ind_portinput.setText("0")
            self.ind_portinput_2.setText("65535")
            self.ind_portinput.setDisabled(False)
            self.ind_portinput_2.setDisabled(False)
        else :
            self.ind_portinput.setDisabled(False)
            self.ind_portinput_2.setDisabled(False)
            
    def fullPortScan(self):
        nm = nmap.PortScanner()
        fullTargetInp = self.full_targetinput_1.text()
        # def getPorts(x):
        #     keys = []
        #     getPorts = nm.scan(x, '1-5024')
        #     dictionary = getPorts['scan'][x]['tcp']
        #     for key in dictionary.items():
        #         keys.append(key)
        #     return keys
        subnetMaskLen = self.full_subnetLen.text()
        nm.scan(hosts=fullTargetInp+"/"+subnetMaskLen, arguments='-sn')
        hosts_list = [{"ip_addr":x,"status":nm[x]['status']['state']} for x in nm.all_hosts()]
        # print(hosts_list)
        self.fullScanOpTable.setRowCount(len(hosts_list))
        row = 0
        for host in hosts_list:
            self.fullScanOpTable.setItem(row,0,QtWidgets.QTableWidgetItem(host["ip_addr"]))
            self.fullScanOpTable.setItem(row,1,QtWidgets.QTableWidgetItem(host["status"]))
            row = row+1
    
    def indPortScan(self):
        indPortInp1 = int(self.ind_portinput.text())
        indPortInp2 = int(self.ind_portinput_2.text())
        indTypeScan = self.ind_typeOfPortScan.currentIndex()
        indScanIpDdCurrentText = self.indScanIpDD.currentText()
        # t = threading.Thread(target=self.intenseScan)
        # QApplication.processEvents()

        def regularScan(target):
            regScan = subprocess.run(['nmap',target],capture_output=True,text=True)
            return regScan.stdout
        def pingScan(target):
            regScan = subprocess.run(['nmap','-sn',target],capture_output=True,text=True)
            return regScan.stdout
        def intenseScan(target):
            regScan = subprocess.run(['nmap','-T4','-A','-v',target],capture_output=True,text=True)
            return regScan.stdout
        def intenseUDPScan(target,port1,port2):
            regScan = subprocess.run(['nmap','-p',port1+'-'+port2,'-sS','-sU','-T4',target],capture_output=True,text=True)
            return regScan.stdout
        def intenseTCPScan(target,port1,port2):
            regScan = subprocess.run(['nmap','-p',port1+'-'+port2,target],capture_output=True,text=True)
            return regScan.stdout
            
        def displayIndPortOp(string):
            self.indScanOpArea.setText(string)

        if indScanIpDdCurrentText=="" or indPortInp1=="" or indPortInp2=="":
            self.indScanOpArea.setText("Enter All Fields")
        else:
            if indTypeScan == 0 or indTypeScan == 1 or indTypeScan == 2:
                self.thread = QThread()
                self.worker = indPortScan.Worker(indScanIpDdCurrentText, indTypeScan)
                self.worker.moveToThread(self.thread)
                self.thread.started.connect(self.worker.run)
                self.worker.finished.connect(self.thread.quit)
                self.worker.finished.connect(self.worker.deleteLater)
                self.thread.finished.connect(self.thread.deleteLater)

                self.thread.start()

                self.thread.finished.connect(
                    lambda: self.indScanOpArea.setText(self.worker.result)
                )
            elif indTypeScan == 3 or indTypeScan == 4:
                self.thread = QThread()
                self.worker = indPortScan.Worker(indScanIpDdCurrentText, indPortInp1, indPortInp2, indTypeScan)
                self.worker.moveToThread(self.thread)
                self.thread.started.connect(self.worker.run)
                self.worker.finished.connect(self.thread.quit)
                self.worker.finished.connect(self.worker.deleteLater)
                self.thread.finished.connect(self.thread.deleteLater)

                self.thread.start()

                self.thread.finished.connect(
                    lambda: self.indScanOpArea.setText(self.worker.result)
                )
        
    def scheduleThread(self):
        print("started scheduling")
        singTargetIp = self.singSchScanTarget.toPlainText()
        singSchTypeScan = self.singSchScanTypeScanDD.currentIndex()

        self.thread2 = QThread()
        self.scheduleWorker = indScheduleScan.ScheduleWorker(singTargetIp, singSchTypeScan)
        self.scheduleWorker.moveToThread(self.thread2)
        self.thread2.started.connect(self.scheduleWorker.run)
        self.scheduleWorker.finished.connect(self.thread2.quit)
        self.scheduleWorker.finished.connect(self.scheduleWorker.deleteLater)
        self.thread2.finished.connect(self.thread2.deleteLater)

        self.thread2.start()

        self.thread2.finished.connect(
            lambda: self.SingSchScanOp.append(self.scheduleWorker.result)
        )

    def singScheduleScan(self):
        singTargetIp = self.singSchScanTarget.toPlainText()
        singSchTimeInterval = self.singSchScanTimeIntervalDD.currentIndex()
        singSchTypeScan = self.singSchScanTypeScanDD.currentIndex()

        if singTargetIp =="":
            self.SingSchScanOp.setText("Please Enter a Target IP")
            # self.SingSchScanOp.setText("empty")
        else:
            if singSchTimeInterval == 0:
                print("0")
                self.thread2 = QThread()
                self.scheduleWorker = indScheduleScan.ScheduleWorker(singTargetIp, singSchTypeScan)
                self.scheduleWorker.moveToThread(self.thread2)
                self.thread2.started.connect(self.scheduleWorker.run)
                self.scheduleWorker.finished.connect(self.thread2.quit)
                self.scheduleWorker.finished.connect(self.scheduleWorker.deleteLater)
                self.thread2.finished.connect(self.thread2.deleteLater)

                self.thread2.start()

                self.thread2.finished.connect(
                    lambda: self.SingSchScanOp.append(self.scheduleWorker.result)
                )
                # schedule.every(15).seconds.do(self.scheduleThread)
            elif singSchTimeInterval == 1:
                schedule.every(60).minutes.do(self.scheduleThread)
            elif singSchTimeInterval == 2:
                schedule.every(3).hours.do(self.scheduleThread)
            elif singSchTimeInterval == 3:
                schedule.every(6).hours.do(self.scheduleThread)
            elif singSchTimeInterval == 4:
                schedule.every(12).hours.do(self.scheduleThread)
            elif singSchTimeInterval == 5:
                schedule.every(24).hours.do(self.scheduleThread)

        while True:
            schedule.run_pending()
            time.sleep(1)

            # self.SingSchScanOp.setText(singTargetIp)
            # print(singTargetIp)

        
    def servicesList(self):
        processIdarr = []
        processNamearr = []
        processStatusarr = []
        for process in psutil.process_iter ():
            ProcessId = str(process.pid)
            processIdarr.append(ProcessId)
            Name = process.name()
            processNamearr.append(Name)
            Status = process.status()
            processStatusarr.append(Status)

        serviceList = []
        for i in range(len(processStatusarr)):
            eachEle = {"pId":processIdarr[i],"pName":processNamearr[i],"pStatus":processStatusarr[i]}
            serviceList.append(eachEle)
            i=i+1
        # print(serviceList)
        # >> [{'pId': '0', 'pName': 'System Idle Process', 'pStatus': 'running'}, {'pId': '36520', 'pName': 'QcShm.exe', 'pStatus': 'running'}]
        row=0
        self.listServicesTab.setRowCount(len(serviceList))
        for service in serviceList: 
            self.listServicesTab.setItem(row , 0, QtWidgets.QTableWidgetItem(service["pId"]))
            self.listServicesTab.setItem(row , 1, QtWidgets.QTableWidgetItem(service["pName"]))
            self.listServicesTab.setItem(row , 2, QtWidgets.QTableWidgetItem(service["pStatus"]))
            row=row+1
    
    def get_ip(self):
        def getIp():
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(0)
            try:
                # doesn't even have to be reachable
                s.connect(('10.254.254.254', 1))
                IP = s.getsockname()[0]
            except Exception:
                IP = '127.0.0.1'
            finally:
                s.close()
            return IP

        localIpAddress = getIp()
        proc = subprocess.Popen('ipconfig',stdout=subprocess.PIPE)

        while True:
            line = proc.stdout.readline()
            if localIpAddress.encode() in line:
                break
        mask = proc.stdout.readline().rstrip().split(b':')[-1].replace(b' ',b'').decode()
        # print(mask)
        masklen = IPAddress(mask).netmask_bits()
        # print(masklen)

        addr = ipcalc.IP(localIpAddress, mask)
        network_with_cidr = str(addr.guess_network())
        bare_network = network_with_cidr.split('/')[0]

        scanner = nmap.PortScanner()
        scanner.scan(hosts=network_with_cidr,arguments='-sn')
        host_list=[x for x in scanner.all_hosts()]
        # print(host_list)
        self.indScanIpDD.addItems(host_list)

    def servicesEditList(self):
        processIdarr = []
        processNamearr = []
        processUsernamearr = []
        table = self.editServicesTab
        
        # killBtn = QtGui.QPushButton("kill")
        for process in psutil.process_iter ():
            ProcessId = str(process.pid)
            processIdarr.append(ProcessId)
            # print(ProcessId)
            Name = process.name()
            processNamearr.append(Name)
            Username = process.username()  
            processUsernamearr.append(Username)


        serviceList = []
        for i in range(len(processUsernamearr)):
            eachEle = {"pId":processIdarr[i],"pName":processNamearr[i],"pUsername":processUsernamearr[i]}
            serviceList.append(eachEle)
            i=i+1
        # print(serviceList)
        # >> [{'pId': '0', 'pName': 'System Idle Process', 'pStatus': 'running'}, {'pId': '36520', 'pName': 'QcShm.exe', 'pStatus': 'running'}]
        row=0
        self.editServicesTab.setRowCount(len(serviceList))

        for service in serviceList: 
            pid = service["pId"]
            pnmae = service["pName"]
            pusername = service["pUsername"]
            # print(pid)
            btn = QtWidgets.QPushButton(table)
            btn.clicked.connect(self.killService)
            btn.setText('Kill')
            self.editServicesTab.setItem(row , 0, QtWidgets.QTableWidgetItem(pid))
            self.editServicesTab.setItem(row , 1, QtWidgets.QTableWidgetItem(pnmae))
            self.editServicesTab.setItem(row , 2, QtWidgets.QTableWidgetItem(pusername))
            self.editServicesTab.setCellWidget(row,3,btn)
            row=row+1

    def killService(self):
        button = QApplication.focusWidget()
        index = (self.editServicesTab.indexAt(button.pos()))
        pid = self.editServicesTab.item(index.row(), 0).text()
        service_name = self.editServicesTab.item(index.row(), 1).text()
        # print(pid)
        # print(signal.valid_signals())
        os.kill(int(pid), signal.SIGTERM)
        print("killed "+service_name)


    def get_ip(self):
            def getIp():
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.settimeout(0)
                try:
                    # doesn't even have to be reachable
                    s.connect(('10.254.254.254', 1))
                    IP = s.getsockname()[0]
                except Exception:
                    IP = '127.0.0.1'
                finally:
                    s.close()
                return IP

            localIpAddress = getIp()
            proc = subprocess.Popen('ipconfig',stdout=subprocess.PIPE)

            while True:
                line = proc.stdout.readline()
                if localIpAddress.encode() in line:
                    break
            mask = proc.stdout.readline().rstrip().split(b':')[-1].replace(b' ',b'').decode()
            # print(mask)
            masklen = IPAddress(mask).netmask_bits()
            # print(masklen)

            addr = ipcalc.IP(localIpAddress, mask)
            network_with_cidr = str(addr.guess_network())
            bare_network = network_with_cidr.split('/')[0]

            scanner = nmap.PortScanner()
            scanner.scan(hosts=network_with_cidr,arguments='-sn')
            host_list=[x for x in scanner.all_hosts()]
            # print(host_list)
            self.indScanIpDD.addItems(host_list)

        #--------------------------- my function ends -----------------------------


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scheduledscan.setText(_translate("MainWindow", "SCHEDULED SCAN"))
        self.services.setText(_translate("MainWindow", "SERVICES"))
        self.portscanner.setText(_translate("MainWindow", "PORT SCANNER"))
        self.individualScanTab.setToolTip(_translate("MainWindow", "<html><head/><body><p>axca</p><p><br/></p></body></html>"))
        self.Targetlabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Target :</span></p></body></html>"))
        self.portlabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Port Range :</span></p></body></html>"))
        self.ind_ScanButton.setText(_translate("MainWindow", "Scan"))
        self.tolabel_3.setText(_translate("MainWindow", "to"))
        self.Outputlabel.setText(_translate("MainWindow", "<html><head/><body><p>OUTPUT</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Type of Scan :</span></p></body></html>"))
        self.ind_typeOfPortScan.setItemText(0, _translate("MainWindow", "Regular Scan"))
        self.ind_typeOfPortScan.setItemText(1, _translate("MainWindow", "Ping Scan"))
        self.ind_typeOfPortScan.setItemText(2, _translate("MainWindow", "Intensive Scan"))
        self.ind_typeOfPortScan.setItemText(3, _translate("MainWindow", "Intensive | UDP Scan"))
        self.ind_typeOfPortScan.setItemText(4, _translate("MainWindow", "Intensive | TCP Scan"))
        self.indScanIpRefreshBtn.setText(_translate("MainWindow", "Refresh list"))
        self.tab1_3.setTabText(self.tab1_3.indexOf(self.individualScanTab), _translate("MainWindow", "Individual Target"))
        self.Targetlabel_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Target ip :</span></p></body></html>"))
        self.full_ScanButton.setText(_translate("MainWindow", "Full Scan"))
        self.Outputlabel_2.setText(_translate("MainWindow", "OUTPUT"))
        item = self.fullScanOpTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ip Address"))
        item = self.fullScanOpTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Status"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Subnet mask Length :</span></p></body></html>"))
        self.tab1_3.setTabText(self.tab1_3.indexOf(self.FullScanTab), _translate("MainWindow", "Full Network "))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Port Scan :</span></p></body></html>"))
        self.listServicesRefresh.setText(_translate("MainWindow", "List Services"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Allowed Services : </span></p></body></html>"))
        item = self.listServicesTab.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PID"))
        item = self.listServicesTab.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Application"))
        item = self.listServicesTab.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        self.tab1.setTabText(self.tab1.indexOf(self.tab), _translate("MainWindow", "List Services"))
        item = self.editServicesTab.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PID"))
        item = self.editServicesTab.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Application"))
        item = self.editServicesTab.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type"))
        item = self.editServicesTab.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Edit"))
        self.getServicesRefreshBtn.setText(_translate("MainWindow", "Refresh"))
        self.userServStatIcon.setText(_translate("MainWindow", "icon"))
        self.label_10.setText(_translate("MainWindow", "User Services"))
        self.sysServStatIcon.setText(_translate("MainWindow", "icon"))
        self.label_12.setText(_translate("MainWindow", "System Services"))
        self.tab1.setTabText(self.tab1.indexOf(self.tab_2), _translate("MainWindow", "Edit Services"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Services :</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Target :</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Time Interval :</span></p></body></html>"))
        self.SingSchScanBtn.setText(_translate("MainWindow", "Schedule"))
        self.singSchScanTimeIntervalDD.setItemText(0, _translate("MainWindow", "30 minutes"))
        self.singSchScanTimeIntervalDD.setItemText(1, _translate("MainWindow", "60 minutes"))
        self.singSchScanTimeIntervalDD.setItemText(2, _translate("MainWindow", "3 hours"))
        self.singSchScanTimeIntervalDD.setItemText(3, _translate("MainWindow", "6 hours"))
        self.singSchScanTimeIntervalDD.setItemText(4, _translate("MainWindow", "12 hours"))
        self.singSchScanTimeIntervalDD.setItemText(5, _translate("MainWindow", "24 hours"))
        self.singSchScanTypeScanDD.setItemText(0, _translate("MainWindow", "Regular Scan"))
        self.singSchScanTypeScanDD.setItemText(1, _translate("MainWindow", "Ping Scan"))
        self.singSchScanTypeScanDD.setItemText(2, _translate("MainWindow", "Intensive Scan"))
        self.singSchScanTypeScanDD.setItemText(3, _translate("MainWindow", "Intensive | UDP Scan"))
        self.singSchScanTypeScanDD.setItemText(4, _translate("MainWindow", "Intensive | TCP Scan"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Type Of Scan :</span></p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Single Machine"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Full Network"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Schedule Scan :</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
