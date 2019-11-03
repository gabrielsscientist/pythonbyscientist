numbers = []
while True:
    num = int(input('Enter a integer number: '))
    if num in numbers:
        print('Duplicate value. I don\'t go add.')
    else:
        numbers.append(num)
        print(f'Successfully added value')
    answer = input('Do you want to continue?(yes(y) or no(n)) ')
    while answer.upper() != 'N' and answer.upper() != 'Y':
        answer = input('Do you want to continue?(yes(y) or no(n)) ')
    if answer.upper() == 'N':
        break
    else:
        print(' ')
#I would used
numbers.sort()
print(f'You was typed the values {numbers}')
