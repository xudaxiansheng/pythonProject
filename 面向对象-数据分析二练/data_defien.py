# 1.设计一个类，可以完成数据的封装
class Record:
    # 用以存储销售数据
    def __init__(self,date,order_id,money,province):
        self.date = date            #销售日期
        self.order_id = order_id    #销售订单号
        self.money = money          #销售金额
        self.province = province    #销售省份

    def __str__(self):
        return f'{self.date} {self.order_id} {self.money} {self.province}'