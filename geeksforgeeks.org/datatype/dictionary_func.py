def printlog(a, b):
    print('\n\n')
    a = (' ' + a + ' ')
    print(a.center(60, '-'))
    print(b)
    print(''.center(60, '-'))


# copy()	                They copy() method returns a shallow copy of the dictionary.
# clear()	                The clear() method removes all items from the dictionary.'
printlog('clear()', 'The clear() method removes all items from the dictionary.')
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print(Dict)
Dict.clear()
print(Dict)

# pop()	                    Removes and returns an element from a dictionary having the given key.
printlog('pop()', 'Removes and returns an element from a dictionary having the given key.')
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print('Dict: ', Dict)
pop_ele = Dict.pop(1)
print('\nDictionary after deletion: ' + str(Dict))
print('Value associated to poped key is: ' + str(pop_ele))

# popitem()	                Removes the arbitrary key-value pair from the dictionary and returns it as tuple.
printlog('popitem()', 'Removes the arbitrary key-value pair from the dictionary and returns it as tuple.')
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks', 6: 'Tuan Anh', 5: 'Phuong Loan'}
print('Dict: ', Dict)
pop_ele = Dict.popitem()
print("Dict arbitrary: " + str(Dict))
print("The arbitrary pair returned is: " + str(pop_ele))

# del()
printlog('del()', 'In Python Dictionary, deletion of keys can be done by using the del keyword. \
    Using del keyword, specific values from a dictionary as well as whole dictionary can be deleted. \
    Items in a Nested dictionary can also be deleted by using del keyword and providing specific nested key \
    and particular key to be deleted from that nested Dictionary.')
Dict = {5: 'Welcome', 6: 'To', 7: 'Geeks',
        'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'},
        'B': {1: 'Geeks', 2: 'Life'}}
print("Initial Dictionary: ")
print(Dict)
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)


# get()	                    It is a conventional method to access a value for a key.
printlog('get()', 'It is a conventional method to access a value for a key.')
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print('Dict: ', Dict)
print("Accessing a element using get:")
print("Dict.get('name') :", Dict.get('name'))

# dictionary_name.values()	returns a list of all the values available in a given dictionary.
printlog('dictionary_name.values()',
         'Returns a list of all the values available in a given dictionary.')
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print('Dict :', Dict)
print('Dict.values() :', Dict.values())

# str()	                    Produces a printable string representation of a dictionary.
printlog('str()', 'Produces a printable string representation of a dictionary.')
print('str(Dict):', str(Dict))
print('len(str(Dict)):', len(str(Dict)))

# update()	                Adds dictionary dict2’s key-values pairs to dict
printlog('update()', 'Adds dictionary dict2’s key-values pairs to dict')
Dictionary1 = {'A': 'Geeks', 'B': 'Original Value', }
Dictionary2 = {'B': 'Updated Value'}
print("Original Dictionary 1: ", Dictionary1)
print("To Updated Dictionary: ", Dictionary2)
Dictionary1.update(Dictionary2)
print("Dictionary 1 after updation key-value B:")
print('Dictionary1.update(Dictionary2) : ', Dictionary1)
Dictionary1.update(D='New Value 1', K='New Value 2')
print("Dictionary 1 after updation key-value B:")
print("Dictionary1.update(D='New Value 1', K='New Value 2') : ", Dictionary1)


# setdefault()	            Set dict[key]=default if key is not already in dict
printlog('setdefault()',
         "Set dict[key]=default if key is not already in dict.")
# Dictionary with single item
Dictionary1 = {'A': 'Geeks', 'B': 'For', 'C': 'C Geeks'}
print("--- Dictionary received: ", Dictionary1)
# using setdefault() method
Third_value = Dictionary1.setdefault('C', 'Default Values')
print("--- Dictionary after setdefault('C', 'Default Values') exist key:", Dictionary1)
print("Third_value:", Third_value)
print()
Third_value = Dictionary1.setdefault('D', 'Default Values')
print("--- Dictionary after setdefault('D', 'Default Values') not exist key:", Dictionary1)
print("Third_value:", Third_value)


# keys()	                Returns list of dictionary dict’s keys
printlog('keys()', "Returns list of dictionary dict’s keys")
# Dictionary with three keys
Dictionary1 = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}
empty_Dict1 = {}
print("Dictionary1: ", Dictionary1)
print("empty_Dict1: ", empty_Dict1)
# Printing keys of dictionary
print('Dictionary1.keys(): ', Dictionary1.keys())
print('empty_Dict1.keys(): ', empty_Dict1.keys())
print('\nDictionary key access:')
print('[*Dictionary1][1]: ', [*Dictionary1][1])
print('list(Dictionary1.keys())[1]: ', list(Dictionary1.keys())[1])


# items()	                Returns a list of dict’s (key, value) tuple pairs
# has_key()	                Returns true if key in dictionary dict, false otherwise
# fromkeys()	            Create a new dictionary with keys from seq and values set to value.
# type()	                Returns the type of the passed variable.
# cmp()	                    Compares elements of both dict.
