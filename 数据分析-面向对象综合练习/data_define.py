# 1.设计一个类，可以完成数据的封装,用来保存每一天的日期，订单号，销售额，销售省份
class Record:

    def __init__(self, date, order_id, money, province):
        self.date = date            # 订单日期
        self.order_id = order_id    # 订单编号
        self.money = money          # 订单销售额
        self.province = province    # 订单销售省份

    def __str__(self):
        return f'{self.date}, {self.order_id}, {self.money}, {self.province}'
