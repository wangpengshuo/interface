import datetime
import sqlite3

from SysSys import Ui_SysSys
import os.path
import random
import sys
import psycopg2
from PyQt5 import QtWidgets, QtGui, QtSql
from PyQt5.QtChart import QBarSet, QBarSeries, QChart, QBarCategoryAxis, QValueAxis, QChartView
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from MatplotlibWidget import MatplotlibWidget
import qtpandas
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget,QCheckBox,QHeaderView
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QDateTimeEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QStyleFactory
import sys
from showdata import Ui_showdata
from adddata import Ui_adddata
from cordata import Ui_Form
from tablewidget import CheckBoxHeader
from PyQt5.QtWebEngineWidgets import *

db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("./interface.db")
header_filed = [' 全选', '编号', '标题', '用户', '籍贯', '发布时间', '是否审核', '操作']
all_header_combobox = []

class addForm(QWidget, Ui_adddata):  # 弹出新建信息对话框
    _signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(addForm, self).__init__()
        self.setupUi(self)
        self.addBn.clicked.connect(self.adddata)
        self.addbackBn.clicked.connect(self.addclose)

    def addclose(self):
        self.close()

    def adddata(self):
        # connect = sqlite3.connect('interface.db')
        # cursor = connect.cursor()
        # cursor.execute(
        #     "create table if not exists interface("
        #     "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        #     "num TEXT,"
        #     "title TEXT,"
        #     "user TEXT,"
        #     "address TEXT,"
        #     "time TEXT,"
        #     "process TEXT,"
        #     "operation TEXT)")
        # self.db = QSqlDatabase.addDatabase("QSQLITE")
        # # 指定要使用的数据库（如
        # # 果数据库不存在则会建立新的）
        # self.db.setDatabaseName("./interface.db")
        # # 打开数据库
        # if not self.db.open():
        #     exit("无法建立数据库")
        # 创建一个用来执行sql语句的对象
        self.query = QSqlQuery(db)
        # 建立数据表
        sql = "create table if not exists interface(" \
              "id integer primary key, " \
              "num varchar(10)," \
              "title varchar(100), " \
              "user varchar(20), " \
              "address varchar(50), " \
              "time varchar(50), " \
              "process varchar(20), " \
              "operation varchar(20))"
        self.query.exec(sql)

        num = self.add_num.text()
        title = self.add_title.text()
        user = self.add_user.text()
        address = self.add_address.text()
        time = self.add_time.text()
        process = self.add_process.currentText()
        operation = self.add_operation.currentText()

        print("num", num)
        print("title", title)
        print("user", user)
        print("address", address)
        print("time", time)
        print("process", process)
        print("operation", operation)

        # 判断有没有填写的信息，如果有则提示，如果没有则存储到文件

        infos = [num, title, user, address, time, process, operation]
        if "" in infos:
            QMessageBox.information(self, '提示', '输入的信息不能为空')
        else:
            sql = "insert into interface(" \
                  "num," \
                  "title," \
                  "user," \
                  "address," \
                  "time," \
                  "process," \
                  "operation)" \
                  "values(" \
                  "'{0}'," \
                  "'{1}'," \
                  "'{2}'," \
                  "'{3}'," \
                  "'{4}'," \
                  "'{5}'," \
                  "'{6}');".format(*infos)
            self.query.exec(sql)
            self._signal.emit(sql)
            QMessageBox.information(self, '提示', '提交成功')


class showForm(QWidget, Ui_showdata):  # 弹出查询信息对话框
    _signal1 = QtCore.pyqtSignal(str)

    def __init__(self):
        super(showForm, self).__init__()


class corForm(QWidget, Ui_Form):  # 弹出修改信息对话框
    _signal2 = QtCore.pyqtSignal(str)

    def __init__(self):
        super(corForm, self).__init__()
        self.setupUi(self)
        self.corBn.clicked.connect(self.cordata)
        self.corbackBn.clicked.connect(self.corclose)

#     self.barGraph.setVisible(True)
    #     self.barGraph.mpl.start_dynamic_plot()


    def corclose(self):
        self.close()

    def cordata(self):
        table_selected_index = self.data.currentIndex().row()
        model = self.data.model()
        num = model.data(model.index(table_selected_index, 0))
        title = model.data(model.index(table_selected_index, 1))
        user = model.data(model.index(table_selected_index, 2))
        address = model.data(model.index(table_selected_index, 3))
        time = model.data(model.index(table_selected_index, 4))
        process = model.data(model.index(table_selected_index, 5))
        operation = model.data(model.index(table_selected_index, 6))


        # 将这些数据设置到对应的文本框
        self.line_num.setText(num)
        # 用一个隐藏的文本框记录要修改的人员编号
        self.line_title.setText(title)
        self.line_edit_user.setText(user)
        self.line_edit_address.setText(address)
        self.line_edit_time.setText(time)
        self.line_edit_process.setText(process)
        self.line_edit_operation.setText(operation)


        num = self.cor_num.text()
        title = self.cor_title.text()
        user = self.cor_user.text()
        adress = self.cor_adress.text()
        process = self.cor_process.text()
        operation=self.cor_operation.text()

        infos = [num, title, user, address, time, process, operation]
        if "" in infos:
            QMessageBox.information(self, '提示', '修改的信息不能为空')

        sql = "update person set " \
              "num='{1}'," \
              "title='{2}'," \
              "user='{3}'," \
              "address='{4}'," \
              "time='{5}'," \
              "process='{6}'," \
              "operation='{7}'," \
              "where " \
              "stu_id='{0}'".format(*infos)
        self.query.exec(sql)

        # 清空文本框的内容
        self.line_num.setText('')
        # 用一个隐藏的文本框记录要修改的人员编号
        self.line_title.setText('')
        self.line_edit_user.setText('')
        self.line_edit_address.setText('')
        self.line_edit_time.setText('')
        self.line_edit_process.setText('')
        self.line_edit_operation.setText('')

        # 重新加载所有信息
        self._signal2.emit(sql)
        QMessageBox.information(self, '提示', '修改成功')


class CheckBoxHeader(QHeaderView):
    select_all_clicked = QtCore.pyqtSignal(bool)
    _x_offset = 3
    _y_offset = 0
    _width = 20
    _height = 20

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(CheckBoxHeader, self).__init__(orientation, parent)
        self.isChecked = False

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super(CheckBoxHeader, self).paintSection(painter, rect, logicalIndex)
        painter.restore()

        self._y_offset = int((rect.height() - self._width) / 2.)

        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(rect.x() + self._x_offset, rect.y() + self._y_offset, self._width, self._height)
            option.state = QStyle.State_Enabled | QStyle.State_Active
            if self.isChecked:
                option.state |= QStyle.State_On
            else:
                option.state |= QStyle.State_Off
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)

    def mousePressEvent(self, event):
        index = self.logicalIndexAt(event.pos())
        if 0 <= index < self.count():
            x = self.sectionPosition(index)
            if x + self._x_offset < event.pos().x() < x + self._x_offset + self._width and self._y_offset < event.pos().y() < self._y_offset + self._height:
                if self.isChecked:
                    self.isChecked=False
                else:
                    self.isChecked= True
                self.select_all_clicked.emit(self.isChecked)
                self.updateSection(0)
                # self.viewport().update()
        super(CheckBoxHeader, self).mousePressEvent(event)

    def change_state(self,state):
        if state == 0:
            for i in all_header_combobox:
                i.clicked.connect(Qt.Checked)
        if state == 2:
            for i in all_header_combobox:
                i.clicked.connect(Qt.Unchecked)


class callSysSys(Ui_SysSys, QMainWindow):
    returnLoginSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(callSysSys, self).__init__()
        self.init_db()
        self.setupUi(self)
        self.addInf = addForm()
        self.showInf = showForm()
        self.corInf = corForm()

        url=r'/home/lab406/test/interface/map_base.html'


        # 退出系统
        self.ExitBn.clicked.connect(self.exitSystem)
        # 返回登录界面
        self.backBn.clicked.connect(self.returnLogin)
        self.homeBn.clicked.connect(self.jiemian1)
        self.InfBn.clicked.connect(self.jiemian2)
        self.scoreBn.clicked.connect(self.jiemian3)

        self.searchBn.clicked.connect(self.searchInf)

        self.corBn.clicked.connect(self.corInfShow)
        self.delBn.clicked.connect(self.delInf)
        self.addBn.clicked.connect(self.addInfShow)
        self.showBn.clicked.connect(self.searchInf)
        ###tabwidget####

        # self.Graph_data.addTab(self.graph, "柱状图")
        # self.Graph_data.addTab(self.pie, "饼状图")
        # self.tab1UI()
        # self.tab2UI()

    @pyqtSlot()
    def tab1UI(self):
        1

    def addInfShow(self):
        self.addInf.show()
        self.addInf._signal.connect(self.get_all_infos)

    def corInfShow(self):
        self.corInf.show()
        self.corInf._signal2.connect(self.get_all_infos)

    def showShow(self):
        self.showInf.show()
        self.showInf._signal1.connect(self.searchInf())

    def get_all_infos(self):
        """查询所有人员信息并显示"""
        self.load_all_infos()
        # 清理查询输入框内容

    def searchInf(self):
        # 查询类型
        # 获取要搜索的内容
        search_content = self.search_keyword.text()

        search_type_map = [
            ('编号', 'num'),
            ('标题', 'title'),
            ('用户', 'user'),
            ('籍贯', 'address'),
            ('发布时间', 'time'),
            ('是否审核', 'process'),
            ('操作', 'operation'),
        ]
        for temp in search_type_map:
            sql = "select count(*) from interface where `{}'".format(search_content)
            self.query.exec(sql)
            self.query.next()
            self.data.setRowCount(self.query.value(0))
            sql = "select * from interface where `{}'".format(search_content)
            self.query.exec(sql)
            i = 0
            while self.query.next():  # 每次查询一行记录
                for j in range(1, 12):
                    new_item = QTableWidgetItem(self.query.value(j))
                    new_item.setTextAlignment(Qt.AlignHCenter)
                    self.data.setItem(i, j - 1, new_item)

                i += 1
            break


        #
        # connect = sqlite3.connect('interface.db')
        # connect.row_factory = sqlite3.Row
        # cursor = connect.cursor()
        # suser = self.search_user.text()
        # cursor.execute('SELECT * FROM interface WHERE name="%s"' % suser)  # 搜出来了 展现在表格上
        # rows = len(cursor.fetchall())
        # student_list = cursor.fetchall()
        # self.data.setRowCount(rows)
        # titles = [' 全选', '编号', '标题', '用户', '籍贯', '发布时间', '是否审核', '操作']
        # self.data.setColumnCount(8)
        # self.data.setHorizontalHeaderLabels(titles)
        #
        # for i, temp_info in enumerate(rows):
        #     print(f'{i + 1}\t\t{temp_info[1]}\t\t{temp_info[2]}\t\t{temp_info[3]}\t\t{temp_info[4]}')
        #     # for j, info_item in enumerate(temp_info):
        #     #     new_item = QTableWidgetItem(info_item)
        #     #     new_item.setTextAlignment(Qt.AlignHCenter)#对齐方式
        #     #     self.data.setItem(i, j, new_item)
        # connect.commit()
        # cursor.close()
        # connect.close()

    def init_db(self):
        """对数据库初始化"""
        # 指定要操作的数据库类型
        # 指定要使用的数据库（如
        # 果数据库不存在则会建立新的）
        # self.db.setDatabaseName("./interface.db")
        # 打开数据库
        if not db.open():
            exit("无法建立数据库")
        # 创建一个用来执行sql语句的对象
        self.query = QSqlQuery()
        # 建立数据表
        sql = "create table if not exists person(" \
              "id integer primary key, " \
              "num varchar(10)," \
              "title varchar(100), " \
              "user varchar(20), " \
              "address varchar(50), " \
              "time varchar(50), " \
              "process varchar(20), " \
              "operation varchar(20))"
        self.query.exec(sql)

    def closeEvent(self, *args):
        """重写此方法，在关闭窗口时要关闭数据库"""
        db.close()
        super().closeEvent(*args)

    def corInf(self):
        self.showInf.show()
        self.showInf._signal1.connect(self.searchInf())

    def delInf(self):
        self.reload_all_infos()
        table_selected_index = self.data.currentIndex().row()
        # 获取表格数据模型对象
        model = self.data.model()
        # 通过模型对象提取第X行第0列（即编号）单元格对象
        table_selected_first_cell = model.index(table_selected_index,1)
        # 提取编号数据
        num = model.data(table_selected_first_cell)
        print("要删除的编号:", num)
        sql = "delete from interface where num='{}'".format(num)
        self.query.exec(sql)

        # 重新加载所有信息
        self.reload_all_infos()

        QMessageBox.information(self, '提示', '删除成功')

    def reload_all_infos(self):
        """重新加载所有信息"""
        self.load_all_infos()

    def load_all_infos(self):
        sql = "select count(*) from interface"
        self.query.exec(sql)
        self.query.next()
        self.data.setColumnCount(8)
        self.data.setHorizontalHeaderLabels([
            ' 全选', '编号', '标题', '用户', '籍贯', '发布时间', '是否审核', '操作'])
        # self.data.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.data.resizeColumnsToContents()
        # self.data.resizeRowsToContents()
        self.data.setRowCount(self.query.value(0))
        # 查询所有信息（如果数据量过大，切记要limit）
        sql = "select * from interface"
        self.query.exec(sql)
        i = 0
        while self.query.next():  # 每次查询一行记录
            for j in range(2, 9):
                new_item = QTableWidgetItem(self.query.value(j - 1))
                new_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.data.setItem(i, j - 1, new_item)
                checkbox = QCheckBox()
                all_header_combobox.append(checkbox)
                self.data.setCellWidget(i, 0, checkbox)
            i += 1
        header = CheckBoxHeader()
        header.select_all_clicked.connect(header.change_state)
        self.data.setHorizontalHeader(header)
        self.data.setColumnWidth(0, 60)
        self.data.setSelectionBehavior(QAbstractItemView.SelectRows)

    @pyqtSlot()
    def jiemian1(self):
        self.Pdata.setCurrentIndex(0)
        #     self.barGraph.setVisible(True)
        #     self.barGraph.mpl.start_dynamic_plot()

    def jiemian2(self):
        self.Pdata.setCurrentIndex(1)
        self.load_all_infos()

    def jiemian3(self):
        self.Pdata.setCurrentIndex(2)

    # 退出系统
    def exitSystem(self):
        sys.exit()

    # 返回登录界面
    def returnLogin(self):
        self.close()
        self.returnLoginSignal.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    CSTLogic = callSysSys()
    addForm = addForm()
    CSTLogic.show()
    sys.exit(app.exec_())
