print('Case x == 2')
x = 2
if x == 2:
    print('x = 2')
elif 'tree'.upper() == 'TREE':
    print(True)
else:
    print(False)
print('---------------------------')
print('Case x != 2, y = treee')
x = 3
y = 'tree'
if x == 2:
    print(True)
elif y.upper() == 'TREE':
    print('x != 2')
    print('y = tree')
else:
    print(False)
print('---------------------------')
print('Case x != 2, y != tree')
x = 3
y = 'treee'
if x == 2:
    print(True)
elif y.upper() == 'TREE':
    print(True)
else:
    print('x != 2')
    print('y != tree')