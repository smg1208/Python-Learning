# Exercise 4 (and Solution)
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
# ----------------------------------------------------------------------
import functions as gf
import datetime
print('Hello, This is exercise to find divisor of a number!')
num = gf.input_Int('')
listdivisor = []
for d in range(1, num+1):
    if num % d != 0:
        continue
    listdivisor.append(d)
if len(listdivisor) == 2:
    print('%s is a prime number and its divisors is %s' % (num, listdivisor))
else:
    print('%s has list divisors: %s' % (num, listdivisor))
print('\n2. Take another, List all prime number less than the number that you input!')
num = gf.input_Int('')
start = datetime.datetime.now()
primes = [n for n in range(1,num) if gf.prime(n) == True]
print('So, all prime number less than %s is: ' % num)
print(primes)
print(len(primes))
end = datetime.datetime.now()
print('%s' % (start.ctime()))
print('%s' % (end.ctime()))
print('\n3. Other, input a number then find the prime has numerical order like number that you input!')
num = gf.input_Int('')
finding = 0
primes = []
while len(primes) < num:
    finding += 1
    if gf.prime(finding):
        primes.append(finding)

print('So the %s prime is integer is: %s' % (num, finding))
print(primes[num-2])
