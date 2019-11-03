values = []
big = small = 0
for i in range(0, 5):
    values.append(int(input(f'Enter a number to index {i}: ')))
    if i == 0:
        big = small = values[0]
    else:
        if values[i] > big:
            big = values[i]
        if small > values[i]:
            small = values[i]

print(f'The biggest value is {big} in index')
for i, v in enumerate(values):
    if v == big:
        print(f'{i}...', end='')
print(f'\nThe lowest is {small} in index')
for i, v in enumerate(values):
    if v == small:
        print(f'{v}...', end='')
