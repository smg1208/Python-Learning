class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('You get a dog!', self.name, ' and its age is ', self.age)

    def changeName(self, age):
        print('You has change age from', self.age, ' to ', age)
        self.age = age

    def talk(self):
        print('Bark!')


class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def talk(self):
        print('Meow!')


A3 = Dog('Mickey', 55)
print(A3.name)
A3.speak()
A3.changeName(12)
print('--------------------')
A4 = Dog('Milu', 45)
print(A4.name)
A4.speak()
A4.changeName(13)
print('--------------------')
A5 = Cat('Meos', 45, 'brown')
print(A5.name)
A5.talk()
A5.changeName(13)
