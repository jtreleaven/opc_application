# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OPC_Application.ui'
#
# Created: Sun May  4 01:11:41 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_OPC_Demo(object):
    def setupUi(self, OPC_Demo):
        OPC_Demo.setObjectName(_fromUtf8("OPC_Demo"))
        OPC_Demo.resize(1000, 750)
        self.centralwidget = QtGui.QWidget(OPC_Demo)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(25, 25, 950, 650))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.start_page = QtGui.QWidget()
        self.start_page.setObjectName(_fromUtf8("start_page"))
        self.quick_demo_btn = QtGui.QPushButton(self.start_page)
        self.quick_demo_btn.setGeometry(QtCore.QRect(400, 200, 150, 50))
        self.quick_demo_btn.setObjectName(_fromUtf8("quick_demo_btn"))
        self.custom_demo_btn = QtGui.QPushButton(self.start_page)
        self.custom_demo_btn.setGeometry(QtCore.QRect(400, 300, 150, 50))
        self.custom_demo_btn.setObjectName(_fromUtf8("custom_demo_btn"))
        self.training_demo_btn = QtGui.QPushButton(self.start_page)
        self.training_demo_btn.setGeometry(QtCore.QRect(400, 400, 150, 50))
        self.training_demo_btn.setObjectName(_fromUtf8("training_demo_btn"))
        self.stackedWidget.addWidget(self.start_page)
        self.quick_demo = QtGui.QWidget()
        self.quick_demo.setObjectName(_fromUtf8("quick_demo"))
        self.stackedWidget.addWidget(self.quick_demo)
        self.custom_demo = QtGui.QWidget()
        self.custom_demo.setObjectName(_fromUtf8("custom_demo"))
        self.stackedWidget.addWidget(self.custom_demo)
        self.training_page = QtGui.QWidget()
        self.training_page.setObjectName(_fromUtf8("training_page"))
        self.graphicsView = QtGui.QGraphicsView(self.training_page)
        self.graphicsView.setGeometry(QtCore.QRect(155, 10, 640, 480))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label = QtGui.QLabel(self.training_page)
        self.label.setGeometry(QtCore.QRect(270, 540, 205, 25))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.training_page)
        self.label_2.setGeometry(QtCore.QRect(270, 570, 205, 25))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.training_page)
        self.label_3.setGeometry(QtCore.QRect(270, 600, 205, 25))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.training_page)
        self.label_4.setGeometry(QtCore.QRect(580, 540, 205, 25))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.training_page)
        self.label_5.setGeometry(QtCore.QRect(580, 570, 205, 25))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.training_page)
        self.label_6.setGeometry(QtCore.QRect(580, 600, 205, 25))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.training_page)
        self.label_7.setGeometry(QtCore.QRect(210, 500, 551, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.stackedWidget.addWidget(self.training_page)
        OPC_Demo.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(OPC_Demo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        OPC_Demo.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(OPC_Demo)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        OPC_Demo.setStatusBar(self.statusbar)

        self.retranslateUi(OPC_Demo)
        QtCore.QMetaObject.connectSlotsByName(OPC_Demo)

    def retranslateUi(self, OPC_Demo):
        OPC_Demo.setWindowTitle(_translate("OPC_Demo", "MainWindow", None))
        self.quick_demo_btn.setText(_translate("OPC_Demo", "Quick Demo", None))
        self.custom_demo_btn.setText(_translate("OPC_Demo", "Custom Demo", None))
        self.training_demo_btn.setText(_translate("OPC_Demo", "Training Demo", None))
        self.label.setText(_translate("OPC_Demo", "0 = Background/False Positive", None))
        self.label_2.setText(_translate("OPC_Demo", "1 = Human", None))
        self.label_3.setText(_translate("OPC_Demo", "2 = Cattle/Livestock", None))
        self.label_4.setText(_translate("OPC_Demo", "3 = Rhino", None))
        self.label_5.setText(_translate("OPC_Demo", "4 = Elephant", None))
        self.label_6.setText(_translate("OPC_Demo", "5 = Giraff", None))
        self.label_7.setText(_translate("OPC_Demo", "Hit the number associated with your guess for the currently highlighted object...", None))

