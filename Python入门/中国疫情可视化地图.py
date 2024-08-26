import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 读取数据文件
with open('D:\可视化案例数据\地图数据\疫情.txt', 'r', encoding='utf-8') as f:
    json_data = f.read()
# 取到各省数据
data = json.loads(json_data)
area_data = data['areaTree'][0]['children']
# print(area_data)
# 组装每个省份和确诊人数为元组，并将各个省的数据封装到列表内
# 空列表
list_area = []
# 修正JSON省区名称数据，以便地图显示
for i in area_data:
    if i['name'] in ['北京', '天津', '重庆', '上海']:
        i['name'] = i['name'] + '市'
    elif i['name'] == '新疆':
        i['name'] = '新疆维吾尔自治区'
    elif i['name'] == '宁夏':
        i['name'] = '宁夏回族自治区'
    elif i['name'] == '西藏':
        i['name'] = '西藏自治区'
    elif i['name'] == '内蒙古':
        i['name'] = '内蒙古自治区'
    else:
        i['name'] = i['name'] + '省'
    list_area.append((i['name'], i['total']['confirm']))
# print(list_area)

# 创建地图
map = Map()
# 添加数据
map.add('中国疫情地图数据', list_area, 'china')
# 设置全局配置
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min': 1, 'max': 50, 'label': '1-50', 'color': '#ffffff'},
            {'min': 51, 'max': 200, 'label': '51-200', 'color': '#cccccc'},
            {'min': 201, 'max': 999, 'label': '201-999', 'color': '#ff6347'},
            {'min': 1000, 'max': 1999, 'label': '201-999', 'color': '#ff8000'},
            {'min': 2000, 'max': 9999999, 'label': '201-999', 'color': '#990033'},
        ]
    )
)
# 绘图
map.render('中国疫情地图.html')
