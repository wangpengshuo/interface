# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:44:40 2022

@author: mzhan
"""


import pandas as pd
data = pd.read_excel("/home/lab406/test/interface/Tab1.xlsx")
data.head()

import plotly.express as px

fig1 = px.sunburst(data, path=['学院类别','学院名称','年级'],values='学生总数',color='学生总数')
fig1.show()

fig2 = px.sunburst(data, path=['学院类别','学院名称','年级'],values='男生数量',color='男生数量')
fig2.show()
fig2 = px.sunburst(data, path=['学院类别','学院名称','年级'],values='女生数量',color='女生数量')
fig2.show()