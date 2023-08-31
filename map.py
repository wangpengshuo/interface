import sys

from PyQt5.QtCore import QUrl, QFileInfo
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker





map = (Map()
       .add("", [list(z) for z in zip(Faker.provinces, Faker.values())],"china")
       .set_global_opts(
       title_opts=opts.TitleOpts(title="map"),
       visualmap_opts=opts.VisualMapOpts(max_=200),))
map.render('map.html')



