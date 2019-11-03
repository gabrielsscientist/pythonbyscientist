from random import choice
names0 = input('Insert the first name: ')
names1 = input('Insert the second name: ')
names2 = input('Insert the third name: ')
names3 = input('Insert the fourth name: ')
lista = [names0,names1,names2,names3]
print(f'The student chosen for clear the board is {choice(lista)}')