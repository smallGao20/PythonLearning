# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_E = QtWidgets.QMenu(self.menubar)
        self.menu_E.setObjectName("menu_E")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.FileOpenAction = QtWidgets.QAction(MainWindow)
        self.FileOpenAction.setObjectName("FileOpenAction")
        self.actionFileNew = QtWidgets.QAction(MainWindow)
        self.actionFileNew.setObjectName("actionFileNew")
        self.actionFileClose = QtWidgets.QAction(MainWindow)
        self.actionFileClose.setObjectName("actionFileClose")
        self.actionAddWin = QtWidgets.QAction(MainWindow)
        self.actionAddWin.setObjectName("actionAddWin")
        self.menu_F.addAction(self.FileOpenAction)
        self.menu_F.addAction(self.actionFileNew)
        self.menu_F.addAction(self.actionFileClose)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())
        self.toolBar.addAction(self.actionAddWin)

        self.retranslateUi(MainWindow)
        self.toolBar.actionTriggered['QAction*'].connect(MainWindow.openMsg)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_F.setTitle(_translate("MainWindow", "文件（&F）"))
        self.menu_E.setTitle(_translate("MainWindow", "编辑（&E）"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.FileOpenAction.setText(_translate("MainWindow", "FileOpen"))
        self.FileOpenAction.setShortcut(_translate("MainWindow", "Alt+O"))
        self.actionFileNew.setText(_translate("MainWindow", "FileNew"))
        self.actionFileNew.setShortcut(_translate("MainWindow", "Alt+N"))
        self.actionFileClose.setText(_translate("MainWindow", "FileClose"))
        self.actionFileClose.setShortcut(_translate("MainWindow", "Alt+C"))
        self.actionAddWin.setText(_translate("MainWindow", "AddWin"))
        self.actionAddWin.setToolTip(_translate("MainWindow", "add new mainwindow"))
