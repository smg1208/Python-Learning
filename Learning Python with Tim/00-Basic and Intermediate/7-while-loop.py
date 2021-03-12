loop = True
while loop:
    sth = input('Input some thing:')
    print('- You input: ', sth)
    if sth == 'stop':
        loop = False
        # break
else:
    print('End while loop with False')