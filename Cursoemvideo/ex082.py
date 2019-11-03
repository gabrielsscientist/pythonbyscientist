numbers = []
evennumbers = []
oddnumbers = []
i = 0
while True:
    numbers.append(int(input('Enter a integer number: ')))
    print(f'Successfully added value')
    answer = input('Do you want to continue?(yes(y) or no(n)) ')
    while answer.upper() != 'N' and answer.upper() != 'Y':
        answer = input('Do you want to continue?(yes(y) or no(n)) ')
    if answer.upper() == 'N':
        break
    else:
        print(' ')
for i in range(0, len(numbers)):
    num = numbers[i]
    if num % 2 == 0:
        if num in evennumbers:
            continue
        else:
            evennumbers.append(numbers[i])
    else:
        if num in oddnumbers:
            continue
        else:
            oddnumbers.append(numbers[i])

print(f'All numbers are -> {numbers}\nThe odds numbers are -> {oddnumbers}.\nThe evens numbers are ->  {evennumbers}.')
