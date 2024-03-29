# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Python_IEX_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Python_IEX_GUI(object):
    def setupUi(self, Python_IEX_GUI):
        Python_IEX_GUI.setObjectName("Python_IEX_GUI")
        Python_IEX_GUI.resize(987, 739)
        Python_IEX_GUI.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Python_IEX_GUI.setStyleSheet("background-color: rgb(197, 248, 255);")
        self.centralwidget = QtWidgets.QWidget(Python_IEX_GUI)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 20, 921, 651))
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_user = QtWidgets.QWidget()
        self.tab_user.setObjectName("tab_user")
        self.connection_status = QtWidgets.QLabel(self.tab_user)
        self.connection_status.setGeometry(QtCore.QRect(430, 70, 451, 41))
        self.connection_status.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"color: black;")
        self.connection_status.setObjectName("connection_status")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_user)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 200, 281, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.p_token = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.p_token.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.p_token.setObjectName("p_token")
        self.verticalLayout.addWidget(self.p_token)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.s_token = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.s_token.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.s_token.setObjectName("s_token")
        self.verticalLayout.addWidget(self.s_token)
        self.connect_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.connect_button.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(184, 184, 184);")
        self.connect_button.setObjectName("connect_button")
        self.verticalLayout.addWidget(self.connect_button)
        self.line = QtWidgets.QFrame(self.tab_user)
        self.line.setGeometry(QtCore.QRect(360, 30, 21, 551))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.connection_browser = QtWidgets.QTextBrowser(self.tab_user)
        self.connection_browser.setGeometry(QtCore.QRect(460, 140, 311, 281))
        self.connection_browser.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.connection_browser.setObjectName("connection_browser")
        self.tabWidget.addTab(self.tab_user, "")
        self.tab_daily = QtWidgets.QWidget()
        self.tab_daily.setObjectName("tab_daily")
        self.date_lbl = QtWidgets.QLabel(self.tab_daily)
        self.date_lbl.setGeometry(QtCore.QRect(160, 20, 91, 16))
        self.date_lbl.setObjectName("date_lbl")
        self.get_btn = QtWidgets.QPushButton(self.tab_daily)
        self.get_btn.setGeometry(QtCore.QRect(280, 50, 93, 21))
        self.get_btn.setStyleSheet("border-width: 5px;\n"
"border-color: rgb(12, 255, 20);\n"
"background-color: rgb(246, 254, 255);\n"
"")
        self.get_btn.setObjectName("get_btn")
        self.sym_lbl = QtWidgets.QLabel(self.tab_daily)
        self.sym_lbl.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.sym_lbl.setObjectName("sym_lbl")
        self.sym_in = QtWidgets.QLineEdit(self.tab_daily)
        self.sym_in.setGeometry(QtCore.QRect(20, 50, 113, 22))
        self.sym_in.setStyleSheet("border-width: 5px;\n"
"border-color: rgb(12, 255, 20);\n"
"background-color: rgb(246, 254, 255);\n"
"")
        self.sym_in.setObjectName("sym_in")
        self.date_in = QtWidgets.QDateEdit(self.tab_daily)
        self.date_in.setGeometry(QtCore.QRect(150, 50, 110, 22))
        self.date_in.setStyleSheet("border-width: 5px;\n"
"border-color: rgb(12, 255, 20);\n"
"background-color: rgb(246, 254, 255);\n"
"")
        self.date_in.setObjectName("date_in")
        self.MplGraph = MplGraph(self.tab_daily)
        self.MplGraph.setGeometry(QtCore.QRect(20, 100, 861, 431))
        self.MplGraph.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.MplGraph.setObjectName("MplGraph")
        self.tabWidget.addTab(self.tab_daily, "")
        self.tab_news = QtWidgets.QWidget()
        self.tab_news.setObjectName("tab_news")
        self.news_browser = QtWidgets.QTextBrowser(self.tab_news)
        self.news_browser.setGeometry(QtCore.QRect(340, 40, 531, 551))
        self.news_browser.setStyleSheet("background-color: rgb(201, 222, 223);")
        self.news_browser.setObjectName("news_browser")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_news)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 70, 267, 137))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(100)
        self.gridLayout.setVerticalSpacing(18)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.news_sym = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.news_sym.setFont(font)
        self.news_sym.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.news_sym.setText("")
        self.news_sym.setObjectName("news_sym")
        self.gridLayout.addWidget(self.news_sym, 1, 0, 1, 1)
        self.num_stories = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.num_stories.setFont(font)
        self.num_stories.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.num_stories.setMinimum(1)
        self.num_stories.setMaximum(50)
        self.num_stories.setObjectName("num_stories")
        self.gridLayout.addWidget(self.num_stories, 1, 1, 1, 1)
        self.news_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.news_button.setFont(font)
        self.news_button.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.news_button.setObjectName("news_button")
        self.gridLayout.addWidget(self.news_button, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tab_news, "")
        Python_IEX_GUI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Python_IEX_GUI)
        self.statusbar.setObjectName("statusbar")
        Python_IEX_GUI.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(Python_IEX_GUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 987, 26))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        Python_IEX_GUI.setMenuBar(self.menubar)
        self.actionTrade = QtWidgets.QAction(Python_IEX_GUI)
        self.actionTrade.setObjectName("actionTrade")
        self.actionDie = QtWidgets.QAction(Python_IEX_GUI)
        self.actionDie.setObjectName("actionDie")
        self.menuOptions.addAction(self.actionTrade)
        self.menuOptions.addAction(self.actionDie)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(Python_IEX_GUI)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Python_IEX_GUI)

    def retranslateUi(self, Python_IEX_GUI):
        _translate = QtCore.QCoreApplication.translate
        Python_IEX_GUI.setWindowTitle(_translate("Python_IEX_GUI", "Python IEX GUI"))
        self.connection_status.setText(_translate("Python_IEX_GUI", "STATUS: NOT CONNECTED"))
        self.label_5.setText(_translate("Python_IEX_GUI", "Enter Publishable Token"))
        self.p_token.setText(_translate("Python_IEX_GUI", "pk_23b0ae9746c642de9500a533c740e06a"))
        self.label_6.setText(_translate("Python_IEX_GUI", "Enter Secret Token"))
        self.s_token.setText(_translate("Python_IEX_GUI", "sk_d10d4c0690a04714b60381eb680bfb5d"))
        self.connect_button.setText(_translate("Python_IEX_GUI", "Connect"))
        self.connection_browser.setHtml(_translate("Python_IEX_GUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; background-color:transparent;\"><span style=\" font-size:12pt; font-weight:600; background-color:transparent;\">Initialize a connection in order to display user information</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; background-color:transparent;\"><span style=\" font-size:10pt;\">All other actions that can be taken using this GUI must be done after successfully establishing a connection with the IEX REST API. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" font-size:8pt;\"><br /></span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_user), _translate("Python_IEX_GUI", "User Info"))
        self.date_lbl.setText(_translate("Python_IEX_GUI", "Enter Date"))
        self.get_btn.setText(_translate("Python_IEX_GUI", "Get Data"))
        self.sym_lbl.setText(_translate("Python_IEX_GUI", "Enter Symbol"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_daily), _translate("Python_IEX_GUI", "Daily Price"))
        self.label.setText(_translate("Python_IEX_GUI", "Symbol"))
        self.label_2.setText(_translate("Python_IEX_GUI", "Stories"))
        self.news_button.setText(_translate("Python_IEX_GUI", "Get News"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_news), _translate("Python_IEX_GUI", "News"))
        self.menuOptions.setTitle(_translate("Python_IEX_GUI", "Options"))
        self.actionTrade.setText(_translate("Python_IEX_GUI", "Trade"))
        self.actionDie.setText(_translate("Python_IEX_GUI", "Die"))

from mplgraph import MplGraph
