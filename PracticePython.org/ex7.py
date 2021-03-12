# Exercise 7 (and Solution)
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
# -------------------------------------------------------------------------
import random
import functions as gf
print('Hello, This is List Comprehension exercise!')
print('Now, we starting with random a list number.')
num = gf.input_Int('')
nrange = gf.input_Int('range')
listRand = []
for i in range(num):
    rand = random.randrange(1, nrange)
    listRand.append(rand)
listOdd = []
listEven = []
for x in listRand:
    if x % 2 == 0:
        listEven.append(x)
    else:
        listOdd.append(x)
print(listRand)
print('There are %s Odd number appear after %d times random 1 to %d' %
      (len(listOdd), num, nrange))
# print(listOdd)
print('There are %s Even number appear after %d times random 1 to %d' %
      (len(listEven), num, nrange))
# print(listEven)
