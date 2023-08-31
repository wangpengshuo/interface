import pandas as pd
import xlwings as xw
from pyecharts.charts import Map
from pyecharts.charts import Bar
from pyecharts.charts import Sunburst
from pyecharts.faker import Faker
from pyecharts import options as opts
# people=pd.read_excel('/home/lab406/test/interface/tab2.xlsx')
# DataList=list(people.groupby(['年级']))
# for in_data in DataList:
#     in_data[1].to_excel('/home/lab406/test/interface/'+str(in_data[0])+'.xlsx',sheet_name=in_data[0],index=False)
# excel1_path = './硕士.xlsx'
# excel2_path = './学士.xlsx'
# excel1_data = pd.read_excel(excel1_path)
# excel2_data = pd.read_excel(excel2_path)
# x_data = excel1_data['学院名称']
# y_data1 = excel1_data['学生总数']
# y_data2 = excel2_data['学生总数']
#
# x_values = x_data.tolist()
# y_values1 = y_data1.tolist()
# y_values2 = y_data2.tolist()
#
# bar = Bar()
# bar.add_xaxis(x_values)
# bar.add_yaxis("硕士", y_values1)
# bar.add_yaxis("学士", y_values2)
# bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
# bar.set_global_opts(title_opts=opts.TitleOpts(title="Bar"),
#                     datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")])
# bar.render('bar_degree.html')

excel_path='./Tab1.xlsx'
excel_data=pd.read_excel(excel_path)
x_data = excel_data['学院名称']
y_data1 =excel_data['学生总数']
y_data2=excel_data['男生数量']
y_data3 =excel_data['女生数量']

x_values=x_data.tolist()
y_values1 =y_data1.tolist()
y_values2= y_data2.tolist()
y_values3 = y_data3.tolist()

bar = Bar()
bar.add_xaxis(x_values)
bar.add_yaxis("学生总数",  y_values1)
bar.add_yaxis("男生数量",  y_values2)
bar.add_yaxis("女生数量", y_values3)
bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
bar.set_global_opts(title_opts=opts.TitleOpts(title="Bar"),
                    datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")])
bar.render('bar.html')
