# Exercise 3 (and Solution)
# Take a list, say for example this one:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

# -------------------------------------------------------------------------------------------------
import functions as gf
print('Hello, This is list Exercise')
alist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print('We have a list: %s' % alist)
print('[...]We have a list with number less than 5:')
for l in alist:
    if l >= 5:
        continue
    print(l)
newa = []
for l in alist:
    if l >= 5:
        continue
    newa.append(l)
print('\n1. List with all number less than 5 from list %s is list %s' %
      (alist, newa))

print('\n2. Input a number, we will return a list that contains only number less than your input number!')
num = gf.input_Int('')
newa_ = []
for l in alist:
    if l >= num:
        continue
    newa_.append(l)
print('List number in list: %s' % alist)
print('is less than %d is : %s' % (num, newa_))
