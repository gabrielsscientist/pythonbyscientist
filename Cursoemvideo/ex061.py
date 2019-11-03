first = float(input('Insert a first number of A.P: '))
reason = float(input('Insert a reason of A.P: '))
terms = 10
while terms != 0:
    i = 1
    while i <= terms:
        print(f'{first}' if i == 1 else f', {first}', end='')
        first += reason
        i += 1
    print('')
    print('\nDo you want show more terms? (0 for not)')
    terms = int(input('How many? '))
'''while terms != 0:
    i = 1
    first += reason
    print(first, end='')
    while i < terms:
        first += reason
        print(f', {first}', end='')
        i += 1
    print('\n')
    print('Do you want show more terms? (0 for not)')
    terms = int(input('How many? '))'''
print('')
print('Bye!')
