def func(word, freq=1, x=3):  # meaning if call func() == func(1)
    print((word+'\n')*(freq+x))
    return x**2


call = func('Hellooooooooooooooooooooo', 3)
print(call)


class Car(object):
    def __init__(self, make, model, year, condition='New', kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll):
        if showAll:
            print(f'This car is a/an {self.make} {self.model} from {self.year}, it is {self.condition} and has {self.kms} kms ran')
        else:
            print(f'This car is a/an {self.make} {self.model} from {self.year}')


A3 = Car('Vinfast', 'Lux Sa 2.0', 2020)
A3.display(True)
