# 设计类
class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 2000)


clock1 = Clock()
clock1.id = 1233333
clock1.price = 12.99
print(f'闹钟ID是：{clock1.id}，价格是{clock1.price}，闹钟要启动了')
clock1.ring()

clock2 = Clock()
clock2.id = 33
clock2.price = 16.99
print(f'闹钟ID是：{clock2.id}，价格是{clock2.price}，闹钟要启动了')
clock2.ring()