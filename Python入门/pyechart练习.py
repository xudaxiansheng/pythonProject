from pyecharts.charts import Line
from pyecharts.options import TitleOpts, ToolboxOpts, VisualMapOpts, LegendOpts

# 得到折线图对象
line = Line()
# 添加X轴数据
line.add_xaxis(['中国', '美国', '英国'])
# 添加y轴数据
line.add_yaxis('GDP', [30, 20, 10])
# 插入标题
line.set_global_opts(
    title_opts=TitleOpts(title='GDP展示', pos_left='center', pos_bottom='1%'),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
    legend_opts=LegendOpts(is_show=True)
)
# 生成图表
line.render()
# import pyecharts.charts
#
# # 创建折线图对象
# line = pyecharts.charts.Line()
# # 增加X轴数据
# line.add_xaxis(['中国', '美国', '英国'])
# # 增加Y轴数据
# line.add_yaxis('GDP', [30, 20, 10])
# # 生成图标
# line.render('GDP.html')
