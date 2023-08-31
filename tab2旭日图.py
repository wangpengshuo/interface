# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:44:40 2022

@author: mzhan
"""


import pandas as pd
temp = pd.read_excel("/home/wps/interface/tab2.xlsx")
temp.head()

import plotly.express as px

fig4 = px.sunburst(temp, path=['学院类别','学院名称','年级'],values='学生总数',color='学生总数')
fig4.show()

fig5 = px.sunburst(temp, path=['学院类别','学院名称','年级'],values='男生数量',color='男生数量')
fig5.show()
fig6 = px.sunburst(temp, path=['学院类别','学院名称','年级'],values='女生数量',color='女生数量')
fig6.show()