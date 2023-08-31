# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:44:40 2022

@author: mzhan
"""

import plotly.express as px
import pandas as pd
from pyecharts.charts import Sunburst
from pyecharts import options as opts

excel_path = './Tab1.xlsx'
excel_data = pd.read_excel(excel_path)
x1 = excel_data['学院类别']
x2 = excel_data['学院名称']
x3 = excel_data['年级']
x4 = excel_data['学生总数']
x5 = excel_data['男生数量']
x6 = excel_data['女生数量']

x1 = x1.tolist()
x2 = x2.tolist()
x3 = x3.tolist()
x4 = x4.tolist()
x5 = x5.tolist()
x6 = x6.tolist()

data = [
    opts.SunburstItem(
        name=x1,
        children=[
            opts.SunburstItem(
                name=x2,
                children=[
                    opts.SunburstItem(
                        name=x3,
                        children=[
                            opts.SunburstItem(
                                name=x4,
                                value=x4,
                            ),
                        ],
                    ),
                ],
            ),
        ],
    ),
]

sunburst = (
    Sunburst(init_opts=opts.InitOpts(width="1000px", height="600px"))
    .add(series_name="", data_pair=data, radius=[0, "90%"])
    .set_global_opts(title_opts=opts.TitleOpts(title="Sunburst-基本示例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
    .render("basic_sunburst.html")
)

# fig1 = px.sunburst(data, path=['学院类别','学院名称','年级'],values='学生总数',color='学生总数')
# fig2 = px.sunburst(data, path=['学院类别','学院名称','年级'],values='男生数量',color='男生数量')
# fig2.show()
# fig2 = px.sunburst(data, path=['学院类别','学院名称','年级'],values='女生数量',color='女生数量')
# fig2.show()
