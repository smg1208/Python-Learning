# Exercise 6 (and Solution)
# Ask the user for a string and print out whether this string is a palindrome number or not.
# (A palindrome number is a string that reads the same forwards and backwards.)
# -----------------------------------------------------------------------------
import functions as gf
import random
print('Hello, this is palindrome number exercise!')
print('1. Now, input a number, then checking that :is it a palindrome number.')
num = gf.input_Int('')


def Palindrome(number):
    numstr = str(number)
    for i in range(0, len(numstr)//2):
        if numstr[i] != numstr[len(numstr)-1-i]:
            return False
    return True


if Palindrome(num):
    print('%s is a palindrome number!' % num)
else:
    print('%s is not a palindrome number!' % num)

print('\n2. Take a random one.')
num = random.randrange(1, 1000000000)
print('Random number is: %s' % num)
if Palindrome(num):
    print('%s is a palindrome number!' % num)
else:
    print('%s is not a palindrome number!' % num)

print('\n3. Random n times and list out all palindrome number.')
num = gf.input_Int('')
nrange = gf.input_Int('range')
listPalindrome = []
for i in range(num):
    rand = random.randrange(1, nrange)
    if Palindrome(rand):
        listPalindrome.append(rand)
print('There are %d palindrome number appear after %d times random 1 to %d' %(len(listPalindrome), num, nrange))
print(listPalindrome)
