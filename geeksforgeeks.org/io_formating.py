# Python program showing how to use
# string modulo operator(%) to print
# fancier output

# print integer and float value
print("Geeks : % 2d, Portal : % 5.2f" % (1, 05.333))

# print integer value
print("Total students : % 3d, Boys : % 2d" % (240, 120))

# print octal value
print("%.o" % (25))

# print exponential value
print("% 10.15E" % (356.08977))


print(str(int('25', 30)))
print('%3d' % 5)
print('%.3d' % 5)
print('% .3d' % 5)


# Python program showing
# use of format() method

# using format() method
print('I love {} for "{}!"'.format('Geeks', 'Geeks'))

# using format() method and refering
# a position of the object
print('{0} and {1}'.format('Geeks', 'Portal'))
print('{1} and {0}'.format('Geeks', 'Portal'))

data = {
    'a': 1,
    'b': 2
}

print('Number {0[a]:3d} {0[b]:3d} '.format(data))

data = [
    (1, 2, 3),
    (1, 2, 3),
    (1, 2, 3)
]
for x in data:
    print('Number {0[0]:3d} {0[1]:3d} {0[2]:3d} '.format(x))

# Python program showing 
# a use of format() method 

# combining positional and keyword arguments 
print('Number one portal is {0}, {1}, and {other}.'
	.format('Geeks', 'For', other ='Geeks')) 

# using format() method with number 
print("Geeks :{0:2d}, Portal :{1:8.2f}". 
	format(12, 00.546)) 

# Changing positional argument 
print("Second argument: {1:3d}, first one: {0:7.2f}". 
	format(47.42, 11)) 

print("Geeks: {a:5d}, Portal: {p:8.2f}". 
	format(a = 453, p = 59.058)) 


# Python program to
# show format () is
# used in dictionary

tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678}

# using format() in dictionary
print('Geeks: {0[geeks]:d}; For: {0[for]:d}; '
      'Geeks: {0[geek]:d}'.format(tab))

data = dict(
    fun="GeeksForGeeks",
    adj="Portal",
    new='By this way'
)

# using format() in dictionary
print("I love {fun} computer {adj} - {new}".format(**data))



# Python program to 
# format a output using 
# string() method 

cstr = "I love geeksforgeeks"
	
# Printing the center aligned 
# string with fillchr 
print ("Center aligned string with fillchr: ") 
print (cstr.center(40, ' ')) 

# Printing the left aligned 
# string with "-" padding 
print ("The left aligned string is : ") 
print (cstr.ljust(40, ' ')) 

# Printing the right aligned string 
# with "-" padding 
print ("The right aligned string is : ") 
print (cstr.rjust(40, ' ')) 
