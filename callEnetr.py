import os.path
import random
import sys
import sqlite3
import psycopg2
from PyQt5 import QtWidgets, QtGui, QtSql
from PyQt5.QtChart import QBarSet, QBarSeries, QChart, QBarCategoryAxis, QValueAxis, QChartView
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import qtpandas
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlTableModel
from PyQt5.QtCore import Qt
from callSys import callSys as CSTLogic
from Enter import Ui_Enter

class MainForm(QMainWindow, Ui_Enter):
    people = []
    def __init__(self,parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.LoginBn.clicked.connect(self.login_)
        self.CSTLogic = CSTLogic()
        # 按钮绑定事件
         # 登录事件
    def login_(self):
        self.CSTLogic.show()
        self.close()
        pass

    # 重新启动界面
    def reshow(self):

        self.show()

    # 运行界面循环
def main_():
    app = QApplication(sys.argv)
    login_ =MainForm()
    login_.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main_()
