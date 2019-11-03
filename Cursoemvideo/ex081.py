numbers = []
while True:
    answer = ''
    numbers.append(int(input('Enter a integer number: ')))
    while answer.upper() != 'N' and answer.upper() != 'Y':
        answer = input('Do you want to continue?(yes(y) or no(n)) ')
    if answer.upper() == 'N':
        break
    else:
        print(' ')
print(' ')
numbers.sort(reverse=True)
print(f'We have {len(numbers)} values -> {numbers}' if len(numbers) > 1 else f'We have {len(numbers)} value -> {numbers}')
if 5 in numbers:
    print('We have the value 5')
else:
    print('We don\'t have the value 5')
