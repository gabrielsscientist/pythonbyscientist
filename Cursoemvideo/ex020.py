from random import shuffle
names0 = input('Insert the first name: ')
names1 = input('Insert the second name: ')
names2 = input('Insert the third name: ')
names3 = input('Insert the fourth name: ')
list = [names0,names1,names2,names3]
shuffle(list)
print(f'The order for apresentation is\nfirst: {list[0]}\nsecond: {list[1]}\nthird: {list[2]}\nlast: {list[3]}')
