# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Enter.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Enter(object):
    def setupUi(self, Enter):
        Enter.setObjectName("Enter")
        Enter.resize(800, 600)
        Enter.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(Enter)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 411, 561))
        self.label.setStyleSheet("border-image: url(:/background/1);")
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(480, 170, 261, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.user = QtWidgets.QLineEdit(self.layoutWidget)
        self.user.setObjectName("user")
        self.gridLayout.addWidget(self.user, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.layoutWidget)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.LoginBn = QtWidgets.QPushButton(self.layoutWidget)
        self.LoginBn.setObjectName("LoginBn")
        self.gridLayout_2.addWidget(self.LoginBn, 1, 0, 1, 1)
        Enter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Enter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        Enter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Enter)
        self.statusbar.setObjectName("statusbar")
        Enter.setStatusBar(self.statusbar)

        self.retranslateUi(Enter)
        QtCore.QMetaObject.connectSlotsByName(Enter)

    def retranslateUi(self, Enter):
        _translate = QtCore.QCoreApplication.translate
        Enter.setWindowTitle(_translate("Enter", "MainWindow"))
        self.label.setText(_translate("Enter", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Welcome! </span></p><p align=\"center\"><span style=\" font-size:24pt;\">某某后台管理系统</span></p></body></html>"))
        self.label_2.setText(_translate("Enter", "<html><head/><body><p><span style=\" font-size:11pt;\">用户名</span></p></body></html>"))
        self.label_3.setText(_translate("Enter", "<html><head/><body><p><span style=\" font-size:11pt;\">密码</span></p></body></html>"))
        self.LoginBn.setText(_translate("Enter", "登录"))

import picture_rc
