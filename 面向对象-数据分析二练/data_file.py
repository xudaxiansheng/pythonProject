# 设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
import json
from data_defien import Record

class Read_File:
    def read_file(self):  # 把每笔订单的销售数据存储到Record类对象中,同时生成list[Record]
        pass

# txt 文件的读取和数据生成对象list
class Text_Read_File(Read_File):

    def __init__(self, path):  # 文件路径变量
        self.path = path

    def read_file(self):
        record_list = []
        with open(self.path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                line = line.split(',')
                record = Record(line[0], line[1], int(line[2]), line[3])  # 单个销售订单的record对象
                # 需要拿到record的list列表，也就是所有的销售数据对象
                record_list.append(record)
            return record_list


class Json_Read_File(Read_File):
    def __init__(self, path): self.path = path
    def read_file(self):
        record_list = []
        with open(self.path, 'r', encoding='utf-8') as f:
            for line in f:
                line = json.loads(line)
                record = Record(line['date'],line['order_id'],int(line['money']),line['province'])
                record_list.append(record)
            return record_list


if __name__ == '__main__':
    text_data = Text_Read_File('2011年1月销售数据.txt')
    list1 = text_data.read_file()
    for i in list1:
        print(i)
    json_data = Json_Read_File('2011年2月销售数据JSON.txt')
    list2 = json_data.read_file()
    for i in list2:
        print(i)

