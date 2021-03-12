# Exercise 2 (and Solution)
# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
# -------------------------------------------------------------------------------------------------
import functions as gf
print('Hello, Welcome to Number check and solution!'.upper())
print('---------------------------------------------')
num = gf.input_Int('')
if num % 2 == 0:
    print('%s is an even number!' % num)
else:
    print('%s is an odd number!' % num)

if num % 4 == 0:
    print('%s is also a multiple of 4!')
print('\nTry to another one ...')
num = gf.input_Int(1)
check = gf.input_Int(2)
if check % num == 0 or num % check == 0:
    if check < num:
        print('%s devides to %s ...' % (num, check))
    else:
        print('%s devides to %s ...' % (check, num))
else:
    if check < num:
        print('%s does not devide to %s ...' % (num, check))
    else:
        print('%s does not devide to %s ...' % (check, num))
    
