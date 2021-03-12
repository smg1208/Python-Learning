import collections
from collections import namedtuple

Point = namedtuple('Point', 'x y z')
p1 = Point(3, 4, 5)
print('p1'.ljust(30, ' '), p1)
print('p1.x'.ljust(30, ' '), p1.x)
print('p1[0]'.ljust(30, ' '), p1[0])
print('p1._asdict()'.ljust(30, ' '), p1._asdict())
p1 = p1._replace(y=6)
print('p1 = p1._fields()'.ljust(30, ' '), p1)
print('p1._fields'.ljust(30, ' '), p1._fields)
p1_1 = Point._make(['a', 'b', 'c'])
print('p1_1'.ljust(30, ' '), p1_1)



Point = namedtuple('Point', ['x', 'y', 'z'])
p2 = Point(3, 4, 5)
print('p2'.ljust(30, ' '), p2)


Point = namedtuple('Point', {'x': 0, 'y': 0, 'z': 0})
p3 = Point(3, 4, 5)
print('p3'.ljust(30, ' '), p3)