# Exercise 8 (and Solution)
# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# ----------------------------------------------------------------------------
import getpass
print('Hello, This is Rock Paper Scissors game!')
print("Now, let's start")
player1 = input('- Please input player 1 name: ')
player2 = input('- Please input player 2 name: ')
print('Hello %s and %s. Lets play!' % (player1, player2))
print('\nRULE OF THE GAME:')
print('Rock beats scissors.')
print('Scissors beats paper.')
print('Paper beats rock.')
print('---------------------------')
print('--- Rock :       input R')
print('--- Scissors :   input S')
print('--- Paper :      input P')
print('---------------------------')
rd = 1
while True:
    print("Hello %s & %s, let's play the game. Round %s" %
          (player1, player2, rd))
    s1 = s2 = ''
    while s1 != 'R' and s1 != 'S'and s1 != 'P':
        s1 = getpass.getpass(
            'Hi %s, Please input your choose (S/R/P):' % player1).upper()
    while s2 != 'R' and s2 != 'S'and s2 != 'P':
        s2 = getpass.getpass(
            'Hi %s, Please input your choose (S/R/P):' % player2).upper()
    if (s1 == 'R' and s2 == 'S') or (s1 == 'S' and s2 == 'P') or (s1 == 'P' and s2 == 'R'):
        print('Round %s: %s (%s) is win %s (%s) is lose' %
              (rd, player1, s1, player2, s2))
    elif (s1 == 'S' and s2 == 'R') or (s1 == 'P' and s2 == 'S') or (s1 == 'R' and s2 == 'P'):
        print('Round %s: %s (%s) is lose %s (%s) is win' %
              (rd, player1, s1, player2, s2))
    else:
        print(
            'Round %s: Both of you choose %s, so result is equals! Please play other round!' % (rd, s1))
    isContinue = ''
    while isContinue != 'Y' and isContinue != 'N':
        isContinue = input(
            'Do you want to play another round? [y/n]: ').upper()
    if isContinue == 'Y':
        rd += 1
    else:
        break
