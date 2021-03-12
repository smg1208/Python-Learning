def func(x):
    func2 = lambda x: x**x//2
    return func2(x) ** x


flam = lambda a, c, b=5: a+b**c


a = flam(1, 2, 3)
b = flam(1, 2)
print(a)
print(b)

c = [x for x in range(100)]
newc = list(map(lambda x: (x*5)**2,list(filter(lambda x: x%2 == 1,c))))
print(newc)