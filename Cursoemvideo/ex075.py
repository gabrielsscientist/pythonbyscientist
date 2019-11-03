pairnum = ''
i = pair = 0
numbers = (int(input('Enter a number: ')), int(input('Enter a number: ')), int(input('Enter a number: ')),
           int(input('Enter a number: ')))
print('The number 9 was typed {} '.format(numbers.count(9)), end='')
print('times' if numbers.count(9) > 1 else 'time')
if 3 in numbers:
    print('The first number 3 is in {} position'.format(numbers.index(3) + 1))
else:
    print('The number 3 was not entered')
for i in range(0, 4):
    if numbers[i] % 2 == 0:
        pair += 1
if pair >= 1:
    print(f'Was typed {pair} even ', end='')
    print('number: ' if pair == 1 else 'numbers: ', end='')
    for i in range(0, 4):
        if numbers[i] % 2 == 0:
            if i == 3:
                print(f' {numbers[i]}.')
            else:
                print(f' {numbers[i]},', end='')