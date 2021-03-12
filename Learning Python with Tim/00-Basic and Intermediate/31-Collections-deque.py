import collections
from collections import deque

d = deque('hello')
d.append('4')
d.appendleft(5)
print(d)

d = deque('hello')
d.pop()
d.popleft()
print(d)

d.clear()
print(d)

d.extend('456')
d.extend([1, 2, 3])
d.extendleft([1, 2, 3])
print(d)


d.rotate(-1)
print(d)
d.rotate(3)
print(d)

print('maxlen'.ljust(30, '_'))
d = deque('superstar', maxlen=5)
print('d'.ljust(30, ' '), d)
d.extend([1, 2, 3])
print('d.extend([1,2,3])'.ljust(30, ' '), d)

