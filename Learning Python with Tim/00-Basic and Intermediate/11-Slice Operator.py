fruits = ['apple', 'pear','strawberrys']
text = 'Hello, my world'
print('text: ',text)
print('--------------------------')
print('text[1]: ',text[1])
print('text[:5]: ',text[:5]) # == text[:5:]
print('text[1:5]: ',text[1:5])
print('text[5:]: ',text[5:]) # == text[5::]
print('text[::2]: ',text[::2])
print('text[:-2]: ',text[:-2])

print('--------------------------')
print('fruits: ',fruits)
print('--------------------------')
fruits.append('blueberrys')
fruits[1:1] = ['1 state',123]
fruits[3:3] = '3 state'
print(fruits)