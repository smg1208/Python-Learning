import collections
from collections import Counter

c = Counter('gallahah')
print(c)
print(list(c.elements()))
print(list(c.most_common(1)))
c = Counter(['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'c'])
print(c)
print(list(c.elements()))
print(list(c.most_common(2)))
c = Counter({'a': 3, 'b': 6})
print(c)
print(list(c.elements()))
print(list(c.most_common(1)))
c = Counter(dogs=7, cats=17)
print(c)
print(list(c.elements()))
print(list(c.most_common(1)))




print('function'.center(30,'-'))
a = Counter(a=4, b=2, c=3, d=5)
b = Counter('aabbddddddddd')
print('a'.ljust(20,' '),list(a.most_common()))
print('b'.ljust(20,' '),list(b.most_common()))
a.subtract(b) 
print('subtract'.ljust(20,' '),a)


a = Counter(a=4, b=2, c=3, d=5)
b = Counter('aabbddddddddd')
a.update(b) 
print('update'.ljust(20,' '),a)

a = Counter(a=4, b=2, c=3, d=5)
b = Counter('aabbddddddddd')
c = a - b
print('a - b = c'.ljust(20,' '),c)

a = Counter(a=4, b=2, c=3, d=5)
b = Counter('aabbddddddddd')
d = a + b
print('a + b = d'.ljust(20,' '),d)

a = Counter(a=4, b=2, c=3, d=5)
b = Counter('aabbddddddddd')
e = a & b
print('a & b = e'.ljust(20,' '),e)

a = Counter(a=4, b=2, c=3, d=5)
b = Counter('aabbddddddddd')
f = a | b
print('a | b = f'.ljust(20,' '),f)
