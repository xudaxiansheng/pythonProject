"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
1.设计一个类，可以完成数据的封装
2.设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
3.读取文件，生产数据对象
4.进行数据需求的逻辑计算（计算每一天的销售额）
5.通过PyEcharts进行图形绘制
"""
import json

from prettytable.colortable import Themes
from pyecharts.globals import ThemeType
from pyecharts.options import TitleOpts, InitOpts

from data_define import Record
from read_file import ReadFile, Text_ReadFile, Json_ReadFile
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.options import ThemeRiverItem

# 得到两个数据的对象
text = Text_ReadFile('2011年1月销售数据.txt')
json = Json_ReadFile('2011年2月销售数据JSON.txt')
# 拿到对象的list数据
text_list: list[Record] = text.read_file()
json_list: list[Record] = json.read_file()
data = text_list + json_list  # 1月+2月的数据汇总

# 如何把每天的数据进行汇总，需要一个空的字典来去承载所有订单数据，{'2011-01-01':200,'2011-01-02':200,'2011-01-03':200}   for 循环，去查字典有没有这个日期的key，若没有，则新增，有则去累加money
sale_dict: dict[str, int] = {}
for record in data:
    if record.date in sale_dict.keys(): #如果，key已经在字典中，则销售额累加
        sale_dict[record.date] += record.money
    else:
        sale_dict[record.date] = record.money
# print(sale_dict)

# 绘制柱形图
bar = Bar(init_opts=InitOpts(theme=ThemeType.DARK))
bar.add_xaxis(list(sale_dict.keys()))
bar.add_yaxis('销售额',list(sale_dict.values()),label_opts=opts.LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title='1~2月每日销售数据')
)
bar.render('销售数据分析.html')
