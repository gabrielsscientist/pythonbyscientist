from math import factorial
num = int(input('Insert a integer number to make a factorial: '))
fac = factorial(num)
print(num, end='')
while num > 0:
    num -= 1
    print(f' x {num}' if num != 0 else ' = ',end='')
print(f' {fac}')
'''i = num - 1
print(f'{num} x {i}', end='')
while i >= 1:
    num *= i
    i -= 1
    if i != 0:
        print(f' x {i}', end='')
print(f' = {num}')
 or factorial(num)'''
