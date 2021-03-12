def printlog(a, *b):
    print('\n\n')
    a = (' ' + a + ' ')
    print(a.center(60, '-'))
    for x in b:
        print('- ', x)
    print(''.center(60, '-'))


# Method
printlog('Methods', 'Function that belongs to a class is called an Method.',
         "All methods require ‘self’ parameter. If you have coded in other OOP language you can think of ‘self’ as the ‘this’ keyword which is used for the current object. It unhides the current instance variable.’self’ mostly work like ‘this’.",
         "‘def’ keyword is used to create a new method.")

# A Python program to demonstrate working of class methods


class Vector2D:
    x = 0.0
    y = 0.0

    # Creating a method named Set
    def Set(self, x, y):
        self.x = x
        self.y = y


def Main():
    # vec is an object of class Vector2D
    vec = Vector2D()
    print('vec.x: ', vec.x)
    print('vec.y: ', vec.y)

    # Passing values to the function Set
    # by using dot(.) operator.
    vec.Set(5, 6)
    print('vec.x: ', vec.x)
    print('vec.y: ', vec.y)
    


if __name__ == '__main__':
    Main()
