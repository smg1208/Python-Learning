list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 998]


def func(x):
    return x**x

# ------------- Old way
# newList = []
# for x in list_:
#     newList.append(func(x))


# ------------- Map way
newList = list(map(func, list_))
# List comprehention
newList = [func(x) for x in list_ if x % 2 == 0]
print(len(str(newList[-1])))
new2 = [str(newList[-1]).count(str(x)) for x in range(0, 10)]
print(new2)
