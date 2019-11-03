numroot = int(input('Enter a number to calculate square root of this: '))
squareroot = numroot ** (1 / 2)
print(f'Square root of {numroot} is {squareroot}')
numrootcub = int(input('Enter the number to discovery your cubic root: '))
raizcubic = numrootcub ** (1 / 3)
print('Cubic root of', numrootcub, 'is', raizcubic)
numpower = int(input('Enter the number to calculate your power: '))
numexponent = int(input('Enter the number that will be exponent: '))
power = numpower ** numexponent
# pow(numpower,numexponent)
print(f'{numpower} elevated at {numexponent} power is= {power:.2f}')  # example:{:20}-> it´s 20 characters
# example: can be use{power:<20} and text will be in the left
# example: can be use{power:<20} and text will be in the left
# example: can be use{power:.2f} and number will be printabled with 2 houses after the point
num1 = int(input('Enter a number: '))
num2 = int(input('Enter other number: '))
# sum = num1+num2
sum = sum([num1, num2])
multiplication = num1 * num2
print(f'Sum is {sum} and multilplication is {multiplication}')
numdd = int(input('Enter the number that will be divided: '))
numdr = int(input('Enter the number that will be divider: '))
division = numdd / numdr
intediv = numdd // numdr
restdiv = numdd % numdr
print(f'Division= {division},integer division=  {intediv} and rest of division = {restdiv}')
thing = (input('Enter any thing: '))
times = int(input('Enter how many times you can put the thing: '))
print(thing * times)
