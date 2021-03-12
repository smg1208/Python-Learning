# and or not
x = 2
y = 3
if x == y and x + y == 5:
    print('ran')
else:
    print('x == y and x + y == 5 is False')
    
if x == y or x + y == 5:
    print('x == y or x + y == 5 is True')
else:
    print('x == y or x + y == 5 is False')
    
if not(x == y or x + y == 5):
    print('not(x == y or x + y == 5) is True')
else:
    print('not(x == y or x + y == 5) is False')