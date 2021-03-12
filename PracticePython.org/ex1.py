# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

import datetime
print('Hello, Welcome to demo!')
name = input('Please input your name: ')
while True:
    age = input('Hello %s, please input your age: ' % name)
    try:
        age = int(age)
        break
    except:
        print('Please input an integer number!')

now = datetime.datetime.now()
print_text = 'You will turn to 100 years old on %s! ' % (100-age+now.year)
while True:
    time = input(
        "How many time that you want print previous message in screen? : ")
    try:
        time = int(time)
        break
    except:
        print('Please input an integer number!')
print(print_text*time)
for x in range(time):
    print('%s. %s' % (x+1, print_text))