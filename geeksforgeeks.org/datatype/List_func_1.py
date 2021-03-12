print('\nList function:'.upper())
List1 = ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
List2 = [d for d in range(1, 14)]
List = List1 + List2
print(List)
# append() : Add an element to the end of the list
print('\nappend() : Add an element to the end of the list')
List.append('append')
print(List)

# extend() : Add an element to the end of the list
print('\nextend() : Add an element to the end of the list')
List.extend(['extend a', 'extend b'])
print(List)

# Insert()	Insert an item at the defined index
print('\nInsert()	Insert an item at the defined index')
List.insert(5, 'Insert value to index 5')
print(List)

# Remove()	Removes an item from the list
print('\nRemove()	Removes an item from the list')
List.remove('K')
print(List)

# Pop()	Removes and returns an element at the given index
print('\nPop()	Removes and returns an element at the given index')
List.pop(7)
print(List)

# Clear()	Removes all items from the list
print('\nClear()	Removes all items from the list')
List.clear()
print(List)

# Index()	Returns the index of the first matched item
print('\nIndex()	Returns the index of the first matched item')
List = List1 + List2
print('List.index(12): ', List.index(12))


# Count()	Returns the count of number of items passed as an argument
print('\nCount()	Returns the count of number of items passed as an argument')
print('List.count("S"): ', List.count('S'))
print('List.count("K"): ', List.count('K'))
print('List.count("E"): ', List.count('E'))
print('List.count(12): ', List.count(12))


# Sort()	Sort items in a list in ascending order
print('\nSort()	Sort items in a list in ascending order')
List = [d for d in range(1, 10)]
List.reverse()
print('List: ', List)
List.sort()
print('List.sort(): ', List)

# Reverse()	Reverse the order of items in the list
print('\nReverse()	Reverse the order of items in the list')
List = [d for d in range(1, 10)]
print('List: ', List)
List.reverse()
print('List.reverse(): ', List)

# copy()	Returns a copy of the list
print('\ncopy()	Returns a copy of the list')
List = [d for d in range(1, 10)]
print('List: ', List)
ListCopy = List.copy()
print('ListCopy = List.copy(): ', ListCopy)
