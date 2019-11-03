sum = c = 0
print('Insert 999 if you want exit')
i = int(input('Insert a number: '))
while i != 999:
    sum += i
    c += 1
    i = int(input('Insert a number: '))
print(f'The sum is {sum} and was typed {c} number' if c <= 1 else f'The sum is {sum} and was typed {c} numbers')