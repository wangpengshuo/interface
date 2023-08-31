import sqlite3
import sys
import random
import matplotlib
import numpy as np
import pandas as pd
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget,QTabWidget
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from pylab import mpl

db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("./interface.db")
class MyMplCanvas(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""

    def __init__(self, parent=None, width=841, height=151, dpi=100):

        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 新建一个figure
        self.axes1 = self.fig.add_subplot(2,1,1)  # 建立一个子图，如果要建立复合图，可以在这里修改
        self.axes2 = self.fig.add_subplot(2, 2, 2)
        #self.axes.hold(False)  # 每次绘图的时候不保留上一次绘图的结果

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        '''定义FigureCanvas的尺寸策略，这部分的意思是设置FigureCanvas，使之尽可能的向外填充空间。'''
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
    '''启动绘制动态图'''


    def figure_degree(self):
        people=pd.read_excel('/home/lab406/test/interface/tab2.xlsx')
        DataList=list(people.groupby(['年级']))
        for in_data in DataList:
            in_data[1].to_excel('/home/lab406/test/interface/'+str(in_data[0])+'.xlsx',sheet_name=in_data[0],index=False)
        self.axes1 = pd.read_excel('/home/lab406/test/interface/硕士.xlsx')
        self.axes2 = pd.read_excel('/home/lab406/test/interface/学士.xlsx')
        self.axes1.plot.bar(x='学院名称',y=['年级','学生总数'])
        # self.axes1.show()
        self.axes2.plot.bar(x='学院名称', y=['年级','学生总数'])
        plt.show()
        # plt.xlabel('学院名称')
        # plt.ylabel('学生总数')
        # plt.legend()
        # # people.plot.bar(x='学院名称',y=['年级','学生总数'])
        # self.draw()

    def figure_class(self):
        people= pd.read_excel('/home/lab406/test/interface/Tab1.xlsx')
        DataList = list(people.groupby(['年级']))
        for in_data in DataList:
            in_data[1].to_excel('/home/lab406/test/interface/' + str(in_data[0]) + '.xlsx', sheet_name=in_data[0],
                                index=False)
        self.axes1= pd.read_excel('/home/lab406/test/interface/一年级.xlsx')
        bardata_2 = pd.read_excel('/home/lab406/test/interface/二年级.xlsx')
        bardata_3 = pd.read_excel('/home/lab406/test/interface/三年级.xlsx')
        self.axes1.plot.bar(x='学院名称', y=[ '学生总数', '男生数量', '女生数量'])
        # self.axes1.plot.bar(x='年级', y=['学院名称','学生总数', '男生数量', '女生数量'])
        # self.axes1.show()
        plt.show()
        # df_1 = pd.read_excel('/home/lab406/test/interface/tab2.xlsx',usecols=[1])
        # df_arr_1=np.asarray(df_1.stack())
        # x_list=df_arr_1.tolist()
        # print(x_list)
        # df_2 = pd.read_excel('/home/lab406/test/interface/tab2.xlsx', usecols=[2])
        # df_arr_2 = np.asarray(df_2.stack())
        # x_list_2 = df_arr_2.tolist()
        # print(x_list_2)
        # df_3 = pd.read_excel('/home/lab406/test/interface/tab2.xlsx', usecols=[1,3])
        # df_arr_3 = np.asarray(df_3.stack())
        # x_list_3 = df_arr_3.tolist()
        # print(x_list_3)
        # df_4 = pd.read_excel('/home/lab406/test/interface/tab2.xlsx', usecols=[1,4])
        # df_arr_4 = np.asarray(df_4.stack())
        # x_list_4 = df_arr_4.tolist()
        # print(x_list_4)
        # df_5 = pd.read_excel('/home/lab406/test/interface/tab2.xlsx', usecols=[1,5])
        # df_arr_5 = np.asarray(df_5.stack())
        # x_list_5 = df_arr_5.tolist()
        # print(x_list_5)
        # y_data2 = [x_list_3, x_list_4,x_list_5]
        # self.axes1.bar(x_list, y_data2, color=['k', 'b','c'])
        # self.fig.suptitle('Bar')
        # self.axes1.set_ylabel('people')
        # self.axes1.set_xlabel('gender')
        # self.axes1.grid(True)
        # self.draw()



class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.mpl = MyMplCanvas(self, width=841, height=151, dpi=100)
        # self.mpl.start_pie_plot() # 如果你想要初始化的时候就呈现静态图，请把这行注释去掉
        # self.mpl.start_dynamic_plot() # 如果你想要初始化的时候就呈现动态图，请把这行注释去掉
        self.mpl_ntb = NavigationToolbar(self.mpl, self)  # 添加完整的 toolbar

        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntb)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    ui.mpl.figure_class()# 测试动态图效果
    sys.exit(app.exec_()) 
