import itertools
import sys
import time
print(('Example 1'.ljust(45, '-')).rjust(50, '-'))
x = [i**2 for i in range(1000)]


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        total = time.time() - start
        print('Total time: ', total)
        return rv
    return wrapper


@timer
def loop():
    for el in x:
        pass
        # print(el)


loop()

# another way


class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration
        rv = self.last**2
        self.last += 1
        return rv


g = Gen(100)

# while True:
#     try:
#         pass
#         # print(next(g))
#     except StopIteration:
#         break

print(('Example 2'.ljust(45, '-')).rjust(50, '-'))


def gen(n):
    for i in range(n):
        yield i**2


x = [i**2 for i in range(10000)]
g = gen(10000)
print(sys.getsizeof(x))
print(sys.getsizeof(g))


print(('Example 3'.ljust(45, '-')).rjust(50, '-'))


def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1


def squares():
    for i in integers():
        yield i * i


def take(n, seq):
    """Returns first n values from the given sequence."""
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(seq.__next__())
    except StopIteration:
        pass
    return result


print(take(15, squares()))

print(('Example 4'.ljust(45, '-')).rjust(50, '-'))


pyt = ((x, y, z) for z in integers() for y in range(1, z)
       for x in range(1, y) if x ** 2 + y ** 2 == z*z)


print(take(100, pyt))
