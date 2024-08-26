class Student:
    name = None
    age = None

    def say_hi(self):
        print(f'你好呀，我是：{self.name}')

    def say_hello(self,msg):
        print(f'你好呀，我是：{self.name}，今年{self.age}岁，{msg}')



stu_11 = Student()
stu_11.name = '许宗广'
stu_11.age = 18
stu_11.say_hi()
stu_11.say_hello('希望大家多多关照')
stu_22 = Student()
stu_22.name = '尚宁宁'
stu_22.age = 19
stu_22.say_hello('大家共同进步')