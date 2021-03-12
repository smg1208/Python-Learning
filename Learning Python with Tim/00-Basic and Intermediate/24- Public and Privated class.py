class Main():
    def public(self):
        print('Puclic mothod!')

    def _protected(self):
        print('Protected mothod!')

    def __private_method(self):
        print('Private mothod!')


class Children_1(Main):
    def method_ex(self):
        self.public()
        self._protected()
        self._Main__private_method()


class _Main():
    def __init__(self, name):
        self.name = name

    def Speak(self):
        print('My name is ', self.name)


class Childern_2():
    def __init__(self, name):
        self.name = name
        self.priv = _Main(name)


x = Children_1()
x.method_ex()

y = Childern_2('Tuan Anh')
y.priv.Speak()
