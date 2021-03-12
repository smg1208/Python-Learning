def printlog(a, *b):
    print('\n\n')
    a = (' ' + a + ' ')
    print(a.center(60, '-'))
    for x in b:
        print('- ', x)
        


printlog('Iterators',
         "Python uses the __iter__() method to return an iterator object of the class.",
         "The iterator object then uses the __next__() method to get the next item.",
         "for loops stops when StopIteration Exception is raised.")


# This program will reverse the string that is passed to it from the main function
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):        
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        print(self.index)
        # print(self.data[self.index])
        return self.data[self.index]


def Main():
    rev = Reverse('Drapsicle')
    for char in rev:
        print(char)

    print(rev.data)


if __name__ == '__main__':
    Main()
