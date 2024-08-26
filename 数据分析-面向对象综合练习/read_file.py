# 2.设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
# 因为有两个不同类型文件，可以先指定一个顶层的抽象类，用以限制子类的方法和具体实现
import json

from data_define import Record


class ReadFile:
    def read_file(self):
        # 读取文件，同时按每天的数据创建Record(date,order_id,money,province)对象并存储，同时返回list[Record] 列表
        pass


# 先读取txt文件，用以拿到数据创建对象
class Text_ReadFile(ReadFile):
    def __init__(self, path):
        self.path = path

    def read_file(self):
        record_list = []
        with open(self.path, 'r',encoding= 'utf_8') as f:
            for line in f:
                line = line.strip()
                line = line.split(',')
                # print(line)
                # 每个订单数据创建对象
                record = Record(line[0], line[1], int(line[2]), line[3])
                # print(record)
                record_list.append(record)
        return record_list

# 读取JSON文件，用以拿到数据创建对象
class Json_ReadFile(ReadFile):
    def __init__(self, path):
        self.path = path

    def read_file(self):
        record_list = []
        with open(self.path, 'r',encoding= 'utf_8') as f:
            for line in f:
                # line = line.strip()
                line = json.loads(line) # json的每行数据字典
                record = Record(line['date'], line['order_id'], int(line['money']), line['province'])
                record_list.append(record)
        return record_list
if __name__ == '__main__':
    txt_file = Text_ReadFile('2011年1月销售数据.txt')
    list1 = txt_file.read_file()
    for i in list1:
        print(i)
    print('-------------------------------------')
    json_file = Json_ReadFile('2011年2月销售数据JSON.txt')
    list2 = json_file.read_file()
    for x in list2:
        print(x)
