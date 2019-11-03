Sum = 0
for i in range(0, 6):
    number = int(input('Insert a number: '))
    if number % 2 == 0:
        Sum += number
print(f'The sum of pair\'s values is {Sum}')
