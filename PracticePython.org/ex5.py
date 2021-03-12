# Exercise 5 (and Solution)
# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
# ---------------------------------------------------------------------------------------------
import random
import functions as gf
print('Hello, Welcome to Exercise 5. List overlap')
print('1. Now, we are starting with insert 2 list data:')
print('- Input first list length.')
lena = gf.input_Int('')
print('Then, input data of list a')
lista = gf.input_data_to_list(lena)
print(lista)
print('- Input second list length.')
lenb = gf.input_Int('')
print('Then, input data of list b')
listb = gf.input_data_to_list(lenb)
print(listb)
print('So, list a and b have a intersection item list:')
intersection = []
for a in lista:
    if a in intersection:
        continue
    if a in listb:
        intersection.append(a)
print(intersection)
print('2. Now, take another with two random list: ')
randoma = []
for x in range(100):
    randoma.append(random.randrange(1, 100))
print('list ramdoma: %s' % randoma)
randomb = []
for x in range(100):
    randomb.append(random.randrange(1, 100))
print('list ramdomb: %s' % randomb)
print('So, list random a and b have a intersection item list:')
intersection = []
for a in randoma:
    if a in intersection:
        continue
    if a in randomb:
        intersection.append(a)
print(intersection)