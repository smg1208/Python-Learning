# Guessing Game One
# Exercise 9 (and Solution)
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
# -----------------------------------------------------------------------------------------------------
import random
import functions as gf
print('Hello, welcome to random and guess number!')
leader_dic = {
    'H': [],
    'M': [],
    'E': []}
mode_dic = {
    'H': ['Hard', 10000],
    'M': ['Medium', 1000],
    'E': ['Easy', 100]}


def sortSecond(val):
    return val[1]


while True:
    name = input('Please input your name(using for the leader board): ')
    mode = gf.input_str_with_a_base(
        'Please select mode to play: hard(H)/medium(M)/easy(E): ', ['H', 'M', 'E'])
    rand = random.randint(1, mode_dic[mode][1])
    print("You select the %s mode. Let's go!" % mode_dic[mode][0])
    print('Number range is from 1 to %s' % mode_dic[mode][1])

    guessNum = int(input('Please input your guess number:'))
    guessCount = 1
    while guessNum != rand:
        if guessNum > rand:
            guessNum = int(input('Your number is to high: '))
        else:
            guessNum = int(input('Your number is to low: '))
        guessCount += 1
    print('Congratulation! It is %s. You find out the number after %s time(s) guess!' % (
        rand, guessCount))
    leader_dic[mode].append([name, guessCount])
    leader_dic[mode].sort(key=sortSecond)

    if len(leader_dic[mode]) > 5:
        leader_dic[mode].pop(5)

    print('\n>>> Hard mode leaderboard:')
    no = 1
    print('No  User%sGuess times' % (' '*(55-19)))
    for x in leader_dic['H']:
        space = (50 - len(x[0]) - len(str(x[1])))*' '
        print('%s    %s%s%s' % (no, x[0], space, x[1]))
        no += 1
    print('%s' % ('-'*55))

    print('\n>>> Medium mode leaderboard:')
    no = 1
    print('No  User%sGuess times' % (' '*(55-19)))
    for x in leader_dic['M']:
        space = (50 - len(x[0]) - len(str(x[1])))*' '
        print('%s    %s%s%s' % (no, x[0], space, x[1]))
        no += 1
    print('%s' % ('-'*55))

    print('\n>>> Easy mode leaderboard:')
    no = 1
    print('No  User%sGuess times' % (' '*(55-19)))
    for x in leader_dic['E']:
        space = (50 - len(x[0]) - len(str(x[1])))*' '
        print('%s    %s%s%s' % (no, x[0], space, x[1]))
        no += 1
    print('%s\n' % ('-'*55))

    isContinue = gf.input_str_with_a_base(
        'Do you want to play another game? [y/n]: ', ['Y', 'N'])
    if isContinue == 'Y':
        continue
    else:
        break
