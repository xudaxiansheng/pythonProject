# 折线图开发练习   疫情数据
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LabelOpts

# 处理数据
with open('D:\可视化案例数据\折线图数据\美国.txt', 'r', encoding='utf-8') as f_us:
    f_us = f_us.read()
with open('D:\可视化案例数据\折线图数据\日本.txt', 'r', encoding='utf-8') as f_jp:
    f_jp = f_jp.read()
with open('D:\可视化案例数据\折线图数据\印度.txt', 'r', encoding='utf-8') as f_ind:
    f_ind = f_ind.read()
    # print(f)
# 去掉不符合JSON规范开头
f_us = f_us.replace('jsonp_1629344292311_69436(', '')
f_jp = f_jp.replace('jsonp_1629350871167_29498(', '')
f_ind = f_ind.replace('jsonp_1629350745930_63180(', '')
# print(f)
# 去掉不符合JSON规范结尾
f_us = f_us[:-2]
f_jp = f_jp[:-2]
f_ind = f_ind[:-2]
# print(f)
# JSON转Python字典
json_us = json.loads(f_us)
json_jp = json.loads(f_jp)
json_ind = json.loads(f_ind)


# print(json_amr)
# print(type(json_amr))
# 获取trend key
def handle(json_str):
    json_trend = json_str['data'][0]['trend']
    # print(json_trend)
    # 获取日期，用于X轴，取2020年，下标到314结束
    x_data = json_trend['updateDate'][:314]
    # print(x_data)
    # 获取确诊数据，用于Y轴，取2020线，下标到314结束
    y_data = json_trend['list'][0]['data'][:314]
    # print(y_data)
    return x_data, y_data


us_x_data, us_y_data = handle(json_us)
jp_x_data, jp_y_data = handle(json_jp)
ind_x_data, ind_y_data = handle(json_ind)
# 创建折线图对象
line = Line()

# 添加x轴数据
line.add_xaxis(us_x_data)
# 添加y轴数据
line.add_yaxis('美国疫情数据', us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis('日本疫情数据',jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis('印度疫情数据',ind_y_data,label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(title='美国、日本、印度疫情2020年数据', pos_left='center', pos_bottom='1%')
)
# 生成图表
line.render('美国、日本、印度疫情数据.html')
