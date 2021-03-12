def printlog(a, *b):
    print('\n\n')
    a = (' ' + a + ' ')
    print(a.center(60, '-'))
    for x in b:
        print('- ', x)
    print(''.center(60, '-'))


# Class
printlog('Class', 'Classes are created by keyword class.',
         'Attributes are the variables that belong to class.',
         'Attributes are always public and can be accessed using dot (.) operator. Eg.: Myclass.')

# creates a class named MyClass


class MyClass:
    # assign the values to the MyClass attributes
    number = 0
    name = "noname"


def Main():
    # Creating an object of the MyClass.
    # Here, 'me' is the object
    me = MyClass()
    print('me.name: ', me.name)
    print('me.number: ', me.number)

    # Accessing the attributes of MyClass using the dot(.) operator
    me.number = 1337
    me.name = "Harssh"
    print('Assign value for object, then:')
    print('me.name: ', me.name)
    print('me.number: ', me.number)