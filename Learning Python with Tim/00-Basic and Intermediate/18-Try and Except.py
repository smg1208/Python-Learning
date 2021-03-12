text = input('Username: ')
try:
    number = int(text)
    print('%d is a valid user name!', text)

except:
    print('%d Invalid username!', text)
