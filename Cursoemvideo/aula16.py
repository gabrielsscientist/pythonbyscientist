'''snack = ('Pizza', 'BigMC', 'Juice', 'Pineapple')
print(snack[1]) == print(snack[-3])
snack = snack[0], 'Pudim', snack[2], snack[3]
print(snack)
print(snack[1])
print(snack[-3])
print(snack[-3:])
for c in snack:
    print(c)
for cont in range(0, len(snack)):
    print(f'snack {snack[cont]} is in position {cont}')
for pos, food in enumerate(snack):
    print(f'{food} in position {pos}')
snack = sorted(snack)
print(snack) #or print(sorted(snack))
'''
a = (5, 4, 3, 2, 1, 0)
b = (-1, -2, -3, -4, -5)
print(a+b)
print(sorted(b)+sorted(a))
a = (5, 2, 3, 2, 1, 0)
print(a.count(2))#prints how many numbers 2 have in tuple
print(a.index(1, 1))#prints what is the position of 1 in tuple starting at position 1


