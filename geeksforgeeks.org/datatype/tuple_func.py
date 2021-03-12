string = 'LETUANANH3'

Tuple = tuple(string)


# all()	Returns true if all element are true or if tuple is empty
print('\nall()	Returns true if all element are true or if tuple is empty')
print(Tuple)
print('all(Tuple): ', all(Tuple))

# any()	return true if any element of the tuple is true. if tuple is empty, return false
print('\nany()	return true if any element of the tuple is true. if tuple is empty, return false')
print(Tuple)
print('any(Tuple): ', any(Tuple))
Tuple = tuple()
print(Tuple)
print('any(tuple()): ', any(Tuple))


# len()	Returns length of the tuple or size of the tuple.
print('\nlen()	Returns length of the tuple or size of the tuple.')
string = 'LETUANANH3'
Tuple = tuple(string)
print(Tuple)
print('len(Tuple): ', len(Tuple))

# enumerate()	Returns enumerate object of tuple
print('\nenumerate()	Returns enumerate object of tuple')
string = 'LETUANANH3'
Tuple = tuple(string)
print(Tuple)
print('list(enumerate(Tuple)): ', list(enumerate(Tuple)))

# max()	return maximum element of given tuple
print('\nmax()	return maximum element of given tuple')
print(Tuple)
print('max(Tuple): ', max(Tuple))

# min()	return minimum element of given tuple
print('\nmin()	return minimum element of given tuple')
print(Tuple)
print('min(Tuple): ', min(Tuple))

# sum()	Sums up the numbers in the tuple
print('\nsum()	Sums up the numbers in the tuple')
newTuple = (int(x) for x in Tuple if x.isnumeric())
print('sum(Tuple): ', sum(newTuple))

# sorted()	input elements in the tuple and return a new sorted list
print('\nsorted()	input elements in the tuple and return a new sorted list')
print(Tuple)
print('sorted(Tuple): ', sorted(Tuple))

# tuple()	Convert an iterable to a tuple.
