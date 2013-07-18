# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Jul 11 00:56:04 2013
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(400, 300)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.button_save = QtGui.QPushButton(self.centralWidget)
        self.button_save.setGeometry(QtCore.QRect(30, 210, 114, 32))
        self.button_save.setObjectName(_fromUtf8("button_save"))
        self.text = QtGui.QTextEdit(self.centralWidget)
        self.text.setGeometry(QtCore.QRect(30, 20, 341, 181))
        self.text.setObjectName(_fromUtf8("text"))
        self.button_open = QtGui.QPushButton(self.centralWidget)
        self.button_open.setGeometry(QtCore.QRect(150, 210, 114, 32))
        self.button_open.setObjectName(_fromUtf8("button_open"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuText_Writer = QtGui.QMenu(self.menuBar)
        self.menuText_Writer.setObjectName(_fromUtf8("menuText_Writer"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuText_Writer.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.button_save.setText(_translate("MainWindow", "Save", None))
        self.button_open.setText(_translate("MainWindow", "Open", None))
        self.menuText_Writer.setTitle(_translate("MainWindow", "Text Writer", None))

