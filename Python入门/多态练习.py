class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print('旺旺旺')
class Cat(Animal):
    def speak(self):
        print('喵喵喵')

def make_noise(animal: Animal):
        animal.speak()

dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)