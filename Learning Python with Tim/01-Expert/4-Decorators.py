import time
print(('Example 1'.ljust(45, '-')).rjust(50, '-'))


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        total = time.time() - start
        print('Total time: ', total)
        return rv
    return wrapper


@timer
def test():
    for _ in range(1_000_000_000):
        pass


test()

print(('Example 2'.ljust(45, '-')).rjust(50, '-'))


def func(f):
    def wrappera(*args, **kwargs):
        print('Started')
        rv = f(*args, **kwargs)
        print('Ended')
        return rv

    return wrappera


@func
def func2(x, y, z, a):
    print('This is func 2 with ', x, y, z, a)
    return a


@func
def func3():
    print('This is func 3')


# func3 = func(func3)
# func3()
# func2 = func(func2)
a = func2(1, 2, 3, 4)
print(a)


# A decorator function to attach
# data to func
def attach_data(func):
    func.data = 3
    return func


@attach_data
def add(x, y):
    return x + y


# This call is equivalent to attach_data()
# with add() as parameter
print(add(2, 3))
print(add.data)
