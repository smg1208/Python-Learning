# Learning python
# LESSION 1: STRING FORMATTING


def Lession1():
    print('Lession 1:')
    print('Hello world, Hello Python!')
    x = 1
    if x == 1:
       # indented four spaces
       print("x is 1.")
       print('- There are two major Python versions, Python 2 and Python 3.')

def Lession5():
    print('Lession 5:')
    name = 'Tuấn Anh'
    age = 23.5
    mylist = [1, 2, 3, 4]
    data = ('John', 'Doe', 53.44)

    print('1. This is %s' % name)
    print('- This is ' + name)

    print('2. This is %s, and he is %d year old!' % (name, age))
    print('- This is %s, and he is %.2f year old!' % (name, age))
    print('- This is '+name + ', and he is '+str(age)+' year old!')

    print('3. A list %s' % mylist)

    format_string = "4. Hello %s %s. Your current balance is $%.3f."
    print(format_string % data)

    print('Here are some basic argument specifiers you should know:')
    print('- %'+'s - String (or any object with a string representation, like numbers)')
    print('- %'+'d - Integers')
    print('- %'+'f - Floating point numbers')
    print('- %'+'.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.')
    print('- %'+'x/'+'%'+'X - Integers in hex representation (lowercase/uppercase)')


# CALLING FUNCTION DEFIINE
Lession1()
Lession5()
