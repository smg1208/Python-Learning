class Dog:
    dogs = []
    xc = 5

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dog(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        for _ in range(n):
            print('bark!!')
print(Dog.num_dog())
A3 = Dog('Mickey')
A4 = Dog('Milu')
print(Dog.num_dog())
print(A4.dogs[1])
print(A3.dogs)
A4.bark(10)
