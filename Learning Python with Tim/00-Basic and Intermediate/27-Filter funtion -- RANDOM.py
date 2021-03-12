import time


def func(x):
    return x**x


def isOdd(x):
    return x % 2 != 0


a = [x for x in range(1, 20)]
b = list(filter(isOdd, a))
c = list(filter(isOdd, list(map(func, a))))
d = list(map(func, a))
print(a)
print(b)
print(d)
print(c)
# Random 6 number


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        total = time.time() - start
        print('Total time: ', total)
        return rv
    return wrapper


class RandomPowerBall():
    CustomRange = 0
    CustomLength = 0

    def __init__(self, type_=99, time=0, NoRandom=0):
        self.type_ = type_
        self.time = time
        self.NoRandom = NoRandom

    def reset(self):
        self.time = 0
        self.NoRandom = 0
        self.CustomLength = 0
        self.CustomRange = 0

    def getTypeofPowerBall(self):
        if self.type_ == 0:
            return [0, 0]
        elif self.type_ == 1:
            return [6, 55]
        elif self.type_ == 2:
            return [6, 45]
        elif self.type_ == 3:
            return [1, self.CustomRange]
        elif self.type_ == 4:
            return [self.CustomLength, self.CustomRange]

    def randomX(self):
        import random
        return random.randrange(1, self.getTypeofPowerBall()[1]+1)

    @timer
    def eachTryingTime(self):
        result = []
        while len(result) < self.getTypeofPowerBall()[0]:
            listRandom = (self.randomX() for x in range(self.NoRandom))
            import collections
            from collections import Counter
            count = Counter(listRandom)
            most = count.most_common(2)
            if len(most) > 1:
                if most[0][1] > most[1][1]:
                    if most[0][0] not in result:
                        print(most[0])
                        result.append(most[0][0])
            else:
                if most[0][0] not in result:
                    print(most[0])
                    result.append(most[0][0])

        return sorted(result)

    def print_(self):
        print('------------------------------------------------------------------------')
        print('---- Please select function that you want to do!')
        print('- Select number [1] to get list 6 number from 1 to 55!')
        print('- Select number [2] to get list 6 number from 1 to 45!')
        print(
            '- Select number [3] to get the most appearance number following your required!')
        print(
            '- Select number [4] to get list length and range number following your required!')
        # print('- Select number [5] to get list a random number following your required!')
        print('- Select number [0] to EXIT program.')
        print('------------------------------------------------------------------------')

    def getInput(self):
        while self.type_ not in [x for x in range(0, 5)]:
            self.print_()
            self.type_ = int(input('Please select number: '))
        if self.type_ != 0 and self.type_ != 99:
            self.reset()
            while self.time <= 0:
                self.time = int(input('Input time you want to trying: '))

            while self.NoRandom <= 0:
                self.NoRandom = int(
                    input('Input time you want to taking random each trying: '))
            if self.type_ in [3, 4]:
                while self.CustomRange <= 0:
                    self.CustomRange = int(
                        input('Input range of number to random: '))
                if self.type_ == 4:
                    while self.CustomLength <= 0:
                        self.CustomLength = int(
                            input('Input length of list number want to received: '))

    def DoTheRandom(self):
        while self.type_ != 0:
            self.type_ = 99
            self.getInput()
            if self.type_ != 0:
                print('Running ...')
                list_result = [self.eachTryingTime() for x in range(self.time)]
                for x in range(self.time):
                    print(
                        f'- Time trying :{x+1}  --- Result: {list_result[x]}')
        else:
            print('Goodluck!')


play = RandomPowerBall()
play.DoTheRandom()
