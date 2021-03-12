# Lession 1 - Hello, world
def les_1():
    print('\n\nLession 1 - Hello, world')
    print('Hello, My Python world!')
    print('Python using indentation for block instead braces')
    print('Example:')
    print('Block with braces:')
    print('    if (a==b){')
    print('      print(\'a equal b\')')
    print('    }')
    print('\nBlock with indentation:')
    print('    if a==b:')
    print('      print(\'a equal b\')')

# Lession 2 - Variables and Types


def les_2():
    print('\n\nLession 2 - Variables and Types')
    print('\tInteger example:')
    myint = 7
    print(myint)

    print('\tFloat example:')
    myfloat = 7.054
    print(myfloat)
    myfloat = float(7)
    print(myfloat)

    print('\tString example:')
    mystring = 'this is my string using SINGLE quotation'
    print(mystring)
    mystring = "this is my string using DOUBLE quotation"
    print(mystring)

    print('\tApostrophes example:')
    mystring = "Don't worry about apostrophes, You can using many single qoute in a double qoute like this ' ' ' ' ' '  "
    print(mystring)
    mystring = 'Or many double qoute in a single qoute like this " " " " " " " " "'
    print(mystring)

    print('\tSimple operators can be executed on numbers and strings:')
    one = 1
    two = 2
    three = one + two
    print(one + two)
    hello = "hello"
    world = "world"
    helloworld = hello + " " + world
    print(helloworld)

    print('\tAssign variables "simultaneously"')
    inta, intb = 3, 4
    print(inta, intb)

    # change this code
    mystring = input('input mystring value: ')
    myfloat = float(input('input myfloat value: '))
    myint = int(input('input myint value: '))

    print('\tExercise:')
    # testing code
    if mystring == "hello":
        print("String: %s" % mystring)
    else:
        print("You input %s but exactly string is hello" % mystring)
    if isinstance(myfloat, float) and myfloat == 10.0:
        print("Float: %f" % myfloat)
    else:
        print("You input %f but exacly number is 10.0" % myfloat)
    if isinstance(myint, int) and myint == 20:
        print("Integer: %d" % myint)
    else:
        print("You input %f but exacly number is 20" % myint)

# Lession 3 - List


def les_3():
    print('- Lists are very similar to arrays.')
    print('- They can contain any type of variable, and they can contain as many variables as you wish.')
    print('- Lists can also be iterated over in a very simple manner. Here is an example of how to build a list.')
    print('---------------------------------------------')
    print('Example:')
    print('mylist = []')
    print('mylist.append(1)')
    print('mylist.append(2)')
    print('mylist.append(3)')
    print('CODE RUNNING:')
    mylist = []
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    print('print(mylist[0]) # prints 1')
    print('print(mylist[1]) # prints 2')
    print('print(mylist[2]) # prints 3')
    print(mylist[0])
    print(mylist[1])
    print(mylist[2])
    print('# prints out 1,2,3')
    print('for x in mylist:')
    print('\tprint(x)')
    # prints out 1,2,3
    for x in mylist:
        print(x)

    print('\n\n')
    print('Accessing an index which does not exist generates an exception (an error).')
    print('---------------------------------------------')
    print('Example:')
    print('mylist = [1,2,3]')
    print('print(mylist[10])')

    print('\n\nEXERCISE:')
    print('---------------------------------------------')
    numbers = []
    strings = []
    names = ["John", "Eric", "Jessica"]
    # write your code here
    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    strings.append(names[0])
    strings.append(names[1])
    strings.append(names[2])
    second_name = names[1]
    # this code should write out the filled arrays and the second name in the names list (Eric).
    print(numbers)
    print(strings)
    print("The second name on the names list is %s" % second_name)

# Lession 4 - Basic Operators


def les_4():
    print('Lession 3 - Basic Operators')
    print('\nArithmetic Operators')
    print('---------------------------------------------')
    print('- Addition, subtraction, multiplication, and division operator can be used with numbers.')
    print('number = 1 + 2 * 3/4 - 5 = %f' % (1+2+3/4))
    print('- Another operator available is the modulo (%) operator, which returns the integer remainder of the division. dividend % divisor = remainder.')
    print('remainder = 11 :: 3 = %d' % (11 % 3))
    print('Note that: :: == %')
    print('- Using two multiplication symbols makes a power relationship.')
    print('squared : 3 ^ 2 = 3 ** 2 = %d' % (3**2))
    print('cubed : 3 ^ 3 = 3 ** 3 = %d' % (3**3))
    print('Other: 3 ^ 12 = 3 ** 12 = %d' % (3**12))
    print('\nUsing Operators with Strings')
    print('---------------------------------------------')
    print('- Python supports concatenating strings using the addition operator:')
    print('print("hello"+" "+"world") = %s' % ('hello' + ' ' + 'world'))
    print('- Python also supports multiplying strings to form a string with a repeating sequence:')
    print('print("hello "*10) = %s' % ('hello '*10))
    print('\nUsing Operators with Lists')
    print('---------------------------------------------')
    print('- Lists can be joined with the addition operators:')
    print('even_numbers = [2,4,6,8]')
    print('odd_numbers = [1,3,5,7]')
    even_numbers = [2, 4, 6, 8]
    odd_numbers = [1, 3, 5, 7]
    print('print(even_numbers + odd_numbers) = %s' %
          (even_numbers + odd_numbers))
    print('- Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator:')
    print('mylist = [1,2,3]')
    mylist = [1, 2, 3]
    print('print(mylist*3) = %s' % (mylist*3))
    print('\Exercise:')
    print('---------------------------------------------')
    x = object()
    y = object()

    # TODO: change this code
    x_list = [x]*10
    y_list = [y]*10
    big_list = x_list+y_list
    print("x_list contains %d objects" % len(x_list))
    print("y_list contains %d objects" % len(y_list))
    print("big_list contains %d objects" % len(big_list))

    # testing code
    if x_list.count(x) == 10 and y_list.count(y) == 10:
        print("Almost there...")
    if big_list.count(x) == 10 and big_list.count(y) == 10:
        print("Great!")

# Lession 5 - String Formatting


def les_5():
    print('Lession 5 - String Formatting')
    print('\n- Python uses C-style string formatting to create new, formatted strings.')
    print('- The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".')
    print('---------------------------------------------')
    # This prints out "Hello, John!"
    name = "John"
    print('print("Hello, %s!" % name) printout "Hello, John!"')
    print("Hello, %s!" % name)
    print('\n- To use two or more argument specifiers, use a tuple (parentheses):')
    print('---------------------------------------------')
    # This prints out "John is 23 years old."
    name = "John"
    age = 23
    print('print("%s is %d years old." % (name, age)) printout "John is 23 years old."')
    print("%s is %d years old." % (name, age))
    print('\nExercise:')
    print('---------------------------------------------')
    data = ("John", "Doe", 53.44)
    format_string = "Solution 1: Hello %s %s. Your current balance is $%s."
    print(format_string)
    print(format_string % data)
    format_string = "Solution 2: Hello %s %s. Your current balance is $%.2f."
    print(format_string)
    print(format_string % data)
    print('----------------------------------------------------------------------------------------------------')
    print('%s - String (or any object with a string representation, like numbers)')
    print('%d - Integers')
    print('%f - Floating point numbers')
    print('%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.')
    print('%x/%X - Integers in hex representation (lowercase/uppercase)')
    print('----------------------------------------------------------------------------------------------------')

# Lession 6 - Basic String Operations


def les_6():
    print('Lession 6 - Basic String Operations')
    print('\n- Len of string:')
    print('----------------------------------------------------')
    print('string = "abcxyz12" so len(string) = %d' % len('abcxyz12'))

    print('\n- Index of text/string in other string')
    print('----------------------------------------------------')
    print('string = "abcdefghijklmn", text="c" so index of text in string:')
    print('string.index(text) = %d' % "abcdefghijklmn".index('c'))

    print('\n- Count number of text/string in other string')
    print('----------------------------------------------------')
    print('string = "aaabbbbbbccc", text="b" so index of text in string:')
    print('string.index(text) = %d' % "aaabbbbbbccc".index('b'))

    print('\n- Slice a string.')
    print('----------------------------------------------------')
    print(
        'string = "My name is Le Tuan Anh" so string[3:15] = %s' % "My name is Le Tuan Anh"[3:15])
    print('The general form is: newstring=string[start:end]')

    print('\n- Slice a string with skip step')
    print('----------------------------------------------------')
    print('string = "My name is Le Tuan Anh" so string[3:15:1] = %s' % "My name is Le Tuan Anh"[
          3:15:1])
    print('string = "My name is Le Tuan Anh" so string[3:15:2] = %s' % "My name is Le Tuan Anh"[
          3:15:2])
    print('The general form is: newstring=string[start:end:skip]')

    print('\n- Reverse a string')
    print('----------------------------------------------------')
    print('string = "Reverse a string" and if you want to reverse:')
    print('string[::-1] = %s' % "Reverse a string"[::-1])

    print('\n- Upper and Lower a string')
    print('----------------------------------------------------')
    print('string = "Hello, world!"')
    print('so upper of string: string.upper() = %s' % "Hello, world!".upper())
    print('so lower of string: string.lower() = %s' % "Hello, world!".lower())

    print('\n- Upper and Lower a string')
    print('----------------------------------------------------')
    print('string = "Hello, world!"')
    print('so upper of string: string.upper() = %s' % "Hello, world!".upper())
    print('so lower of string: string.lower() = %s' % "Hello, world!".lower())

    print('\n- startswith and endswith a string')
    print('----------------------------------------------------')
    print('string = "Hello, world!"')
    print('string.startswith("Hello") = %s' %
          "Hello, world!".startswith('Hello'))
    print('string.startswith("hello") = %s' %
          "Hello, world!".startswith('hello'))

    print('string.endswith("ld!") = %s' % "Hello, world!".endswith("ld!"))
    print('string.endswith("abd") = %s' % "Hello, world!".endswith("abd"))

    print('\n- split a string')
    print('----------------------------------------------------')
    print('string = "Hello, world!"')
    print('string.split(", ") = %s' % "Hello, world!".split(', '))

    print('\n- Exercise')
    print('----------------------------------------------------')
    s = "Strings are awesome!"
    # Length should be 20
    print("Length of s = %d" % len(s))

    # First occurrence of "a" should be at index 8
    print("The first occurrence of the letter a = %d" % s.index("a"))

    # Number of a's should be 2
    print("a occurs %d times" % s.count("a"))

    # Slicing the string into bits
    print("The first five characters are '%s'" % s[:5])  # Start to 5
    print("The next five characters are '%s'" % s[5:10])  # 5 to 10
    print("The thirteenth character is '%s'" % s[12])  # Just number 12
    print("The characters with odd index are '%s'" %
          s[1::2])  # (0-based indexing)
    print("The last five characters are '%s'" % s[-5:])  # 5th-from-last to end

    # Convert everything to uppercase
    print("String in uppercase: %s" % s.upper())

    # Convert everything to lowercase
    print("String in lowercase: %s" % s.lower())

    # Check how a string starts
    if s.startswith("Str"):
        print("String starts with 'Str'. Good!")

    # Check how a string ends
    if s.endswith("ome!"):
        print("String ends with 'ome!'. Good!")

    # Split the string into three separate strings,
    # each containing only a word
    print("Split the words of the string: %s" % s.split(" "))

# Lession 7 - Conditions


def les_7():
    print('Lession 7 - Conditions')
    print('\n- Python uses boolean variables to evaluate conditions. The boolean values True and False are returned when an expression is compared or evaluated.')
    print('------------------------------------------------')
    x = 2
    print('x = 2')
    print('print(x == 2) will print out %s' % (x == 2))

    print('\n- Boolean operators')
    print('The "and" and "or" boolean operators allow building complex boolean expressions')
    print('------------------------------------------------')
    name = "John"
    age = 23
    print('name = "John"')
    print('age = 23')
    print('if name == "John" and age == 23:')
    if name == "John" and age == 23:
        print("Your name is John, and you are also 23 years old.")
    print('if name == "John" or name == "Rick":')
    if name == "John" or name == "Rick":
        print("Your name is either John or Rick.")

    print('\n- The "in" operators')
    print('The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list:')
    print('------------------------------------------------')
    name = "John"
    print('name = "John"')
    print('if name in ["John","Rick"]:')
    if name in ["John", "Rick"]:
        print("Your name is either John or Rick.")
    print('if name in ["John 1","Rick 1"]:')
    if name in ["John 1", "Rick 1"]:
        print("Your name is either John 1 or Rick 1.")
    else:
        print("Your name is neither John 1 nor Rick 1.")

    print('\n - The "is" operator')
    print('For single variables')
    print('------------------------------------------------')
    x = 2
    y = 2
    print('x = 2')
    print('y = 2')
    print('so:')
    print('x is 2: return %s' % (x is 2))
    print('x == 2: return %s' % (x == 2))
    print('x is y: return %s' % (x is y))
    print('x == y: return %s' % (x == y))

    print('For values of variables')
    print('------------------------------------------------')
    x = [1, 2, 3]
    y = [1, 2, 3]
    print('x = [1,2,3]')
    print('y = [1,2,3]')
    print('so:')
    print('x is y: return %s' % (x is y))
    print('x == y: return %s' % (x == y))

    print('\n - The "not" operator')
    print('For single variables')
    print('------------------------------------------------')
    x = True
    y = False
    print('x = True')
    print('y = False')
    print('so:')
    print('not x: return %s' % (not x))
    print('(not x) is y: return %s' % ((not x)is y))
    print('(not x) != y: return %s' % ((not x) != y))
    print('(not x) == y: return %s' % ((not x) == y))

    print('\n Exercise:')    
    print('number = 10')
    print('second_number = 10')
    print('first_array = []')
    print('second_array = [1,2,3]')
    print('\nChange the variables in the first section, so that each if statement resolves as True.'.upper())
    print('We have 6 statements.\n'.upper())
    print('------------------------------------------------')
    number = int(input('number: '))
    second_number = input('second_number: ')
    try:
        second_number = bool(second_number)
    except ValueError:
        try:
            second_number = int(second_number)
        except ValueError:
            try:
                second_number = float(second_number)
            except:
                second_number = str(second_number)
    first_array = list()
    second_array = list()
    num = int(input('[Input first_array]range of array: '))
    for x in range(num):
        data = input('data: ')
        try:
            data = int(data)
        except ValueError:
            try:
                data = int(data)
            except ValueError:
                data = str(data)
        first_array.append(data)
    num = int(input('[Input second_array]range of array: '))
    for x in range(num):
        data = input('data: ')
        try:
            data = int(data)
        except ValueError:
            try:
                data = float(data)
            except ValueError:
                data = str(data)
        second_array.append(data)
    # Code to check:
    if number > 15:
        print("1. number is %s and greater than 15" % number)

    if first_array:
        print("2. first_array is %s" % first_array)

    if len(second_array) == 2:
        print("3. len(second_array) = %s" % len(second_array))

    if len(first_array) + len(second_array) == 5:
        print("4. len(first_array) = %s and len(second_array) = %s" %
              (len(first_array), len(second_array)))

    if first_array and first_array[0] == 1:
        print("5. first_array = %s and first_array[0]= %d" % (
            first_array, first_array[0]))
    
    if not second_number:
        print("6. second_number = %s" % second_number)


# les_1()
# les_2()
# les_3()
# les_4()
# les_5()
# les_6()
les_7()
