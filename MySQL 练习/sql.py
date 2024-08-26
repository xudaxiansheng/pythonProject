from pymysql import Connection, connect

# 获取数据库的连接

connect = Connection(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456'
)

# print(connect.get_server_info())
cursor = connect.cursor()  # 获取游标
# 使用数据库
connect.select_db('python_xu')
# cursor.execute('create table person(id int,person_num varchar(18))')

# 数据库查询

cursor.execute('insert into python_xu values(%s,%s,%s)')
# 获取查询结果  元组
results = cursor.fetchall()
# 每行数据打印
for row in results:
    for i in row:
        print(i)
connect.close()
