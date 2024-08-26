"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
1.设计一个类，可以完成数据的封装
2.设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
3.读取文件，生产数据对象
4.进行数据需求的逻辑计算（计算每一天的销售额）
5.通过PyEcharts进行图形绘制
"""
from pymysql import Connection
from data_file import Read_File, Text_Read_File, Json_Read_File
from pyecharts import options as opts
text_data = Text_Read_File('2011年1月销售数据.txt')  # 创建文本的对象
json_data = Json_Read_File('2011年2月销售数据JSON.txt')  # 创建json的对象
# 需要接受两个对象方法下的record list列表
list_text = text_data.read_file()
list_json = json_data.read_file()
sale_data:dict[str,str,int,str] = list_text + list_json
# for item in sale_data:
    # print(item.date)

# 连接数据库
con = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True
)
# 使用数据库
con.select_db('python_xu')
# 建立游标
cur = con.cursor()
# 创建SQL 并执行
for i in sale_data:

    valus = f"'{i.date}','{i.order_id}',{i.money},'{i.province}'"
    # print(valus)
    sql = f"insert into python_xu.order values ({valus})"
    cur.execute(sql)
# 关闭连接
con.close()