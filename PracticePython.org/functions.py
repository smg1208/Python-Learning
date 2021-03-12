def input_Int(text):
    while True:
        if text == '':
            num = input('Please input an integer number: ')
        else:
            num = input('Please input an integer number - number %s: ' % text)

        try:
            num = int(num)
            break
        except ValueError:
            print('NOTE: input an integer number!')
    return num


def input_data_to_list(lenOfList):
    listdata = []
    for i in range(1, lenOfList+1):
        data = input('%s. input data (number/string) - no.%s: ' % (i, i))
        try:
            data = int(data)
        except ValueError:
            try:
                data = float(data)
            except ValueError:
                try:
                    data = str(data)
                except ValueError:
                    print('Input data error!')
                    data = False
        listdata.append(data)
    return listdata


def prime(number):
    divisor = [d for d in range(1,number+1) if number % d ==0]     
    # print('%s - %s' % (number, divisor))
    if len(divisor) == 2 or len(divisor) == 1:
        return True
    else:
        return False


def exist_on_list(listvalue, value):
    try:
        listvalue.index(value)
        return True
    except ValueError:
        return False


def Palindrome(number):
    numstr = str(number)
    for i in range(0, len(numstr)//2):
        if numstr[i] != numstr[len(numstr)-1-i]:
            return False
    return True


def input_str_with_a_base(text, lista):
    txt = ''
    print(txt in lista)
    while (txt in lista) == False:
        txt = input('%s: ' % text).upper()
    return txt
