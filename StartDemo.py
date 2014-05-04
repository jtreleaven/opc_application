#!/usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui
from OPC_Application import Ui_OPC_Demo

class OPC_Controller(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_OPC_Demo()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.training_demo_btn, QtCore.SIGNAL("clicked()"), self.training_demo)


    def training_demo(self):
        pass
