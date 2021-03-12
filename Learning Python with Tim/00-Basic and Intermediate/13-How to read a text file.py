file = open('13-text.txt', 'r')  # read mode
# file = open('13-text.txt', 'w') # write mode
f = file.readlines()
print('file: ', f)
newlist = []
for l in f:
    if l.count('\n') == 1:
        newlist.append(l[:-1])
    else:
        newlist.append(l)

print('newlist: ', newlist)
