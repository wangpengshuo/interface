# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cordata.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(373, 518)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 90, 281, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)
        self.cor_title = QtWidgets.QLineEdit(self.layoutWidget)
        self.cor_title.setObjectName("cor_title")
        self.gridLayout.addWidget(self.cor_title, 1, 2, 1, 2)
        self.cor_num = QtWidgets.QLineEdit(self.layoutWidget)
        self.cor_num.setObjectName("cor_num")
        self.gridLayout.addWidget(self.cor_num, 0, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)
        self.cor_user = QtWidgets.QLineEdit(self.layoutWidget)
        self.cor_user.setObjectName("cor_user")
        self.gridLayout.addWidget(self.cor_user, 2, 2, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 2)
        self.cor_address = QtWidgets.QLineEdit(self.layoutWidget)
        self.cor_address.setObjectName("cor_address")
        self.gridLayout.addWidget(self.cor_address, 3, 2, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 2)
        self.cor_process = QtWidgets.QComboBox(self.layoutWidget)
        self.cor_process.setObjectName("cor_process")
        self.gridLayout.addWidget(self.cor_process, 5, 2, 1, 2)
        self.cor_operation = QtWidgets.QComboBox(self.layoutWidget)
        self.cor_operation.setObjectName("cor_operation")
        self.gridLayout.addWidget(self.cor_operation, 6, 2, 1, 2)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 4, 2, 1, 2)
        self.corBn = QtWidgets.QPushButton(Form)
        self.corBn.setGeometry(QtCore.QRect(240, 440, 80, 26))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.corBn.setFont(font)
        self.corBn.setObjectName("corBn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 50, 381, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.corbackBn = QtWidgets.QPushButton(Form)
        self.corbackBn.setGeometry(QtCore.QRect(140, 440, 80, 26))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.corbackBn.setFont(font)
        self.corbackBn.setObjectName("corbackBn")
        self.corclearBn = QtWidgets.QPushButton(Form)
        self.corclearBn.setGeometry(QtCore.QRect(40, 440, 80, 26))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.corclearBn.setFont(font)
        self.corclearBn.setObjectName("corclearBn")

        self.retranslateUi(Form)
        self.corclearBn.clicked.connect(self.cor_address.clear)
        self.corclearBn.clicked.connect(self.cor_user.clear)
        self.corclearBn.clicked.connect(self.cor_title.clear)
        self.corclearBn.clicked.connect(self.cor_num.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\">标题</p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\">编号</p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\">用户</p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\">籍贯</p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\">发布时间</p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"center\">是否审核</p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"center\">操作</p></body></html>"))
        self.corBn.setText(_translate("Form", "确认"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">修改数据</span></p></body></html>"))
        self.corbackBn.setText(_translate("Form", "返回"))
        self.corclearBn.setText(_translate("Form", "清除"))
