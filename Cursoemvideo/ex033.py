number1 = int(input('Insert the first number: '))
number2 = int(input('Insert the second number: '))
number3 = int(input('Insert the third number: '))
numbers = number1, number2, number3
if numbers[0] > numbers[1] and numbers[0] > numbers[2]:
    bigger = numbers[0]
    smaller = numbers[1]
    if numbers[1] > numbers[2]:
        smaller = numbers[2]
if numbers[1] > numbers[0] and numbers[1] > numbers[2]:
    smaller = numbers[0]
    bigger = numbers[1]
    if numbers[0] > numbers[2]:
        smaller = numbers[2]
if numbers[2] > numbers[1] and numbers[2] > numbers[0]:
    bigger = numbers[2]
    smaller = numbers[1]
    if numbers[1] > numbers[0]:
        smaller = numbers[0]

print(f'The biggest number is {bigger}\nThe smallest number is {smaller}')
