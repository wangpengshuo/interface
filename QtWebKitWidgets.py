from pyecharts.charts import Geo,Map
from pyecharts import options as opts
from pyecharts.faker import Faker
c=(
    Map()
    .add("全国主要城市空气质量热力图",[list(z) for z in zip(Faker.provinces,Faker.values())],"china",is_map_symbol_show=False)
    .set_global_opts(title_opts=opts.TitleOpts(title="Map"),visualmap_opts=opts.VisualMapOpts())
    .render("map_base.html")

)

# geo = (Geo().add_schema(maptype="china").add("", [list(z) for z in zip(keys, values)], "china"))
# geo.set_global_opts(title_opts=opts.TitleOpts(
#     title="全国主要城市空气质量热力图", subtitle="data from pm2.5", item_gap=15,
#     title_textstyle_opts=opts.TextStyleOpts(color="black", font_weight="bolder", font_size=40),
#     subtitle_textstyle_opts=opts.TextStyleOpts(color="gray", font_weight="bolder", font_size=15)))
# geo.render()
