class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def __str__(self):
        return '('+str(self.x) + ','+str(self.y)+')'

    def __len__(self):
        import math
        return int(math.sqrt(self.x**2+self.y**2))

    def length(self):
        import math
        return math.sqrt(self.x**2+self.y**2)

    def __gt__(self, p):
        return self.length() > p.length()

    def __ge__(self, p):
        return self.length() >= p.length()

    def __lt__(self, p):
        return self.length() <= p.length()

    def __le__(self, p):
        return self.length() <= p.length()

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y


p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)
p5 = Point(0, 1)

p6 = p1 + p2
p7 = p4 - p1
p8 = p2 * p3

print(p1, p2, p3, p4)
print(p8, p6, p7)
print(len(p1))
# print(p1 > p2)
# print(p3 >= p2)

# print(p4 == p5)
