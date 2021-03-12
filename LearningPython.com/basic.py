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

# Lession 8 - Loops


def les_8():
    print('Lession 8 - Loops')
    print('\nThe "for" loop')
    print('- For loops iterate over a given sequence.')
    print('--------------------------------------------------')
    print('exs = [1, 2, 3, 4, 5, 6, 7, 8, 9]')
    print('for ex in exs:')
    print('    print(ex)')
    print('will print out list from 1 to 9:')
    exs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for ex in exs:
        print(ex)

    print('- For loops with range and step')
    print('--------------------------------------------------')
    print('>>> Case 1: from 0 to end+1')
    print('for ex in range(5):')
    print('    print(ex)')
    print('will print out list from 0 to 4:')
    for ex in range(5):
        print(ex)

    print('>>> Case 2: from start to end+1')
    print('for ex in range(4,9):')
    print('    print(ex)')
    print('will print out list from 4 to 8:')
    for ex in range(4, 9):
        print(ex)

    print('>>> Case 3: from start to end + 1 with step n')
    print('for ex in range(4,15,3):')
    print('    print(ex)')
    print('will print out list from in clude:')
    for ex in range(4, 15, 3):
        print(ex)

    print('\n"while" loop')
    print('- While loops repeat as long as a certain boolean condition is met.')
    print('--------------------------------------------------')
    print('x = 1')
    print('while x < 10:')
    print('    print(x)')
    print('    x+=3')
    print('will print out list :')
    x = 1
    while x < 10:
        print(x)
        x += 3  # same with x = x + 3

    print('- "break" and "continue" statements')
    print('--------------------------------------------------')
    print('break example'.upper())
    print('count = 0')
    print('while True:')
    print('    print(count)')
    print('    count+=1')
    print('    if count >= 3:')
    print('        break')
    print('will print out list:')
    count = 0
    while True:
        print(count)
        count += 1
        if count >= 5:
            break
    print('continue example'.upper())
    print('for x in range(20):')
    print('    if x % 5 != 0:')
    print('        continue')
    print('    print(x)')
    print('will print out list:')
    for x in range(20):
        if x % 5 != 0:
            continue
        print(x)

    print('\n\n- use "else" clause for loops?'.upper())
    print('When the loop condition of "for" or "while" statement fails then code part in "else" is executed.')
    print('If break statement is executed inside for loop then the "else" part is skipped.')
    print('"else" part is executed even if there is a continue statement.')
    print('--------------------------------------------------')
    print('else clause without continue:'.upper())
    count = 0
    while count < 10:
        print(count)
        count += 4
    else:
        print('This is else clause because count = %d >= 10' % count)

    print('else clause continue:'.upper())
    count = 0
    while count < 10:
        count += 1
        if count % 4 != 0:
            continue
        print(count)
    else:
        print('This is else clause because count = %d >= 10' % count)

    print('Exercise:')
    print('numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]')
    print("Loop through and print out all even numbers from the numbers list in the same order they are received. Don't print any numbers that come after 237 in the sequence.")
    print('------------------------------------------------')
    numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
               615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
               386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
               399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
               815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
               958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
               743, 527]
    for i in numbers:
        if i == 217:
            break
        if i % 2 == 0:
            print('%s - %s' % (numbers.index(i)+1, i))


# Lession 9 - Functions

def les_9():
    print('Lession 9 - Functions')
    print("- Functions in python are defined using the block keyword 'def', followed with the function's name as the block's name.")
    print('--------------------------------------------')
    print('def my_function():')
    print('    print("Hello From My Function!")')
    print("\n- Functions may also receive arguments (variables passed from the caller to the function).")
    print('--------------------------------------------')
    print('def my_function_with_args(username, greeting):')
    print('    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))')
    print("\n- Functions may return a value to the caller, using the keyword- 'return'.")
    print('--------------------------------------------')
    print('def sum_two_numbers(a, b):')
    print('    return a + b')
    print("\nHow do you call functions in Python?".upper())
    print('--------------------------------------------')
    print('my_function()')
    print('my_function_with_args("John Doe", "a great year!")')
    print('x = sum_two_numbers(13,12)')
    print('print(x)')

    def my_function():
        print('Hello from my function with love!')

    def my_function_with_args(username, greeting):
        print('Hello, %s, from my function with love!, I wish you feeling %s' %
              (username, greeting))

    def sum_two_numbers(a, b):
        return a+b
    print('Code output:')
    my_function()
    my_function_with_args('Tuan Anh', 'happy')
    x = sum_two_numbers(13, 12)
    print(x)

# Lession 10 - Classes and Object


def les_10():
    print('Lession 10 - Classes and Object')
    print('- Objects are an encapsulation of variables and functions into a single entity.')
    print('- Objects get their variables and functions from classes.')
    print('- Classes are essentially a template to create your objects.')
    print('---------------------------------------------')
    print('- So a basic function like:\n')
    print('class MyClass:')
    print('    variable = "blah"')
    print('    def function(self):')
    print('         print("This is a message inside the class.")')
    print('\n- And you can assign above class to an object:')
    print('myObject = MyClass()')
    print('\n- and access the variable inside by:')
    print('myObject.variable')
    print('\n- then print it out:')
    print('print("myObject.variable")')
    print('\n- you also call function from object')
    print('print("myObject.function()")')

    class Vehical:
        name = ''
        kind = 'car'
        color = ''
        value = 100.00

        def description(self):
            desc_str = '%s is a %s %s worth $%.2f' % (
                self.name, self.color, self.kind, self.value)
            return desc_str

    car1 = Vehical()
    car1.name = 'Fer'
    car1.color = 'Red'
    car1.kind = 'convertible'
    car1.value = 60000.00
    car2 = Vehical()
    car2.name = 'Jump'
    car2.color = 'Blue'
    car2.kind = 'Van'
    car2.value = 100000.00

    print(car1.description())
    print(car2.description())

# Lession 11 - Dictionaries


def les_11():
    print('Lession 11 - Dictionaries')
    print('Same with array but work by key and value instead of indexes')
    print('Each value store in DIC can be accessed by using a key, which is any type of object (string, number, list, ...) instead of index')
    print('-------------------------------------------------')
    print('phonebook = {}')
    print('phonebook["John"] = 938477566')
    print('phonebook["Jack"] = 938377264')
    print('phonebook["Jill"] = 947662781')
    print('print(phonebook)')
    phonebook = {}
    phonebook["John"] = 938477566
    phonebook["Jack"] = 938377264
    phonebook["Jill"] = 947662781

    print('\n or define an DIC by this way:')
    print('phonebook = {')
    print('    "John" : 938477566,')
    print('    "Jack" : 938377264,')
    print('    "Jill" : 947662781,')
    print('}')
    phonebook = {
        "John": 938477566,
        "Jack": 938377264,
        "Jill": 947662781
    }
    print('print(phonebook) will be print out:')
    print(phonebook)

    print('\n Iterating over dictionaries')
    print('Dictionaries can be iterated over, just like a list.')
    print('unlike a list, DIC iterate over key value pairs')
    print('------------------------------------------------------')
    print(
        'phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}')
    print('for name, number in phonebook.items():')
    print('    print("Phone number of %s is %d" % (name, number))')
    phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
    for name, number in phonebook.items():
        print("Phone number of %s is %d" % (name, number))
    for i in phonebook.items():
        print(i)
    print(phonebook.items())
    print(phonebook.keys())
    print(phonebook.values())

    print('\n Removing a value')
    print('------------------------------------------------------')
    print(
        'phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}')
    print('del phonebook["John"]')
    print('or using:')
    print('phonebook.pop("John")')
    print('print(phonebook) will print-out:')
    phonebook = {"John": 938477566, "Jack": 938377264, "Jill": [947662781]}
    del phonebook["John"]
    print(phonebook.get('Jill'))

# Lession 12 - Modules & Packages


def les_12():
    print('Lession 12 - Modules & Packages')
    from module import multiple  # import an object from module
    # from module import * >>> import all object from module, only allowed at module level
    multiple(12, 13)
    import module  # import module
    import module as func  # import module
    func.sum(123456789, 987654321)
    print(__name__)
    print(__file__)
    print(__doc__)
    print(__package__)
    print(__import__)
    import os
    help(os)

    import sys
    print(os.getcwd())
    print('Module have extension like python file .py')
    print('Name of module is python file name')
    print('Python module can be a set of functions, classes, variables defined and implemented')
    print('\n-Using "import module_name" key to import a module from other')
    print('-Using "import module_name as new_name" key to to custom import module name')
    print('-Using "from module_name import object" key to import an object from module')
    print('-Using "from module_name import *" key to import all object from module')
    print('\n A module is loaded once (first time) while running python script if your code import it many time')
    print('So local variables inside the module act as a "singleton" - they are initialized only once.')
    print('\n')

    


# les_1()
# les_2()
# les_3()
# les_4()
# les_5()
# les_6()
# les_7()
# les_8()
# les_9()
# les_10()
# les_11()
les_12()
