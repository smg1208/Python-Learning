class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        a = {}
        for name, value in attrs.items():
            if name.startswith('__'):
                a[name] = value
            else:
                a[name.upper()] = value
        print(a)
        return type(class_name, bases, a)


class Dog(metaclass=Meta):
    x = 5
    y = 7

    def hi(self):
        print(('Hello'))

d = Dog()
print(d.X)
print(d.HI())
