import inspect
from collections import Counter

def make_class(x):
    class Dog:
        def __init__(self, name):
            self.name = name

        def print_value(self):
            print(x)

    return Dog

cls = make_class(100)
A3 = cls('A3')
print(A3.name)
print(A3.print_value())

print(('Ex 2'.ljust(30,'-')).rjust(35,'-'))

for i in range(10):
    def show():
        print(i*2)
    show()
show()

print(('Ex 3'.ljust(30,'-')).rjust(35,'-'))

def func(x):
    if x==1:
        def rv():
            print('X is equal to 1')
    else:
        def rv():
            print('X is not 1')
    return rv
new_func = func(1)
new_func()

print(('Ex 4'.ljust(30,'-')).rjust(35,'-'))
print(id(new_func))
print(inspect.getsource(cls))
# print(inspect.getsource(Counter)) #(Optional) if you want to show Counter Collection source, unlock this code

