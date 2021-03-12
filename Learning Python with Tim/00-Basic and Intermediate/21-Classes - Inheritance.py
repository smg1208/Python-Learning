class Veichle(object):
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas


class Car(Veichle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print('Beep beep !!!')


class Truck(Car):
    def __init__(self, price, gas, color, speed='160', tires='12'):
        super().__init__(price, gas, color, speed)
        self.tires = tires

    def beep(self):
        print('Honk Honk !!!')
    
    def Details(self):
        print('Price: ',self.price)
        print('Gas: ',self.gas)
        print('Color: ',self.color)
        print('Speed: ',self.speed)
        print('Tires: ',self.tires)


truck = Truck('50000', '200', 'green', '16')
truck.beep()
truck.Details()
