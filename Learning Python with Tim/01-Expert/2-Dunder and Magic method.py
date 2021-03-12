import inspect


x = [1, 2, 3]
y = [4, 5]
print(x+y)
print(x*3)
print(type(x))

print(('Ex 2'.ljust(30, '-')).rjust(35, '-'))


class Person:
    def __init__(self, agr1):
        self.agr1 = agr1

    def __repr__(self):
        return f'Person({self.agr1})'

    def __mul__(self, xp):
        if type(xp) is not int:
            raise Exception('Invalid agruments, must be int!')
        self.agr1 = self.agr1*xp

    def __call__(self, y):
        print('call this function ', y)
    
    def __len__(self):
        return len(self.agr1)


p = Person('A3')
p*4
p('hello')
print(p)
print(len(p))

print(('Ex 3'.ljust(30, '-')).rjust(35, '-'))

from queue import Queue as q
import inspect
# q = Queue()
# print(q)
# print(inspect.getsource(Queue))

class Queue(q):
    def __repr__(self):
        return f'Queue({self._qsize()})'
    
    def __add__(self, item):
        self.put(item)
    
    def __sub__(self, item):
        self.get(item)

qu = Queue()
qu + 5
qu + 5
qu + 5
qu + 5
print(qu.qsize())

qu - None
qu - 0
print(qu.qsize())