var = 9
loop = False

def func_a(x):
    loop = 7
    print('loop inside func_a = ', loop)
    if x == 9:
        return var
a = func_a(9)
print(a)
print('loop outside func_a = ', loop)

def func_b():
    global loop
    loop = 7
    var = 4
    print('loop inside func_b = ', loop)
    print('var inside func_b = ', var)
    if var == 4:
        print('var local = ',var)

func_b()
print('loop outside func_b = ', loop)
print('var outside func_b = ', var)