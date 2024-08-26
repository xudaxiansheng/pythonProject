# 父类  电话

class Phone:
    ID: str = '12344546567'
    prodtcer: str = 'china'

    def call_by_4g(self):
        print('用4g打电话')

# 子类，继承父类

class Phone2024(Phone):
    face_id = '面部识别'
    prodtcer = 'china_tianjin'
    def call_by_5g(self):
        print('____________________')
        self.call_by_4g()
        print('用5g打电话')

# 创建对象，使用父类方法
phone = Phone2024()
phone.call_by_4g()
phone.call_by_5g()