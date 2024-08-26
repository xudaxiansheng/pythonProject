from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 创建地图对象
map = Map()
# 准备数据
data = [
    ('北京市', 80),
    ('河北省', 10),
    ('天津市', 50),
    ('河南省', 90),
    ('山东省', 180),
    ('山西省', 120),
    ('福建省', 380),
    ('广东省', 980)
]
# 添加数据
map.add('测试地图', data, 'china')

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min':1,'max':50,'label':'1-50','color':'#ccffff'},
            {'min':51,'max':200,'label':'51-200','color':'#ff6666'},
            {'min':201,'max':999,'label':'201-999','color':'#990033'},
        ]
    )
)


# 绘图
map.render('中国地图.html')