
# 设计类：记录学生信息
class Student:
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress



for i in range(1, 11):
    print(f'当前录入第{i}位学生信息，总共需要录入10位学生信息')
    name = input('请输入学生姓名')
    age = input('请输入学生年龄')
    adress = input('请输入学生地址')
    student = Student(name, age, adress)
    print(f'学生{i}信息录入完成，信息为：【学生姓名：{student.name}，年龄：{student.age}，地址：{student.adress}')
