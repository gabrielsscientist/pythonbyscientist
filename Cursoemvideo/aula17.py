#values = []
values = list()#this command and the above do the same thing
a = [3, 63, 53, 54, 3]
b = a
b[2] = 5
print(f'A = {a}, B = {b}')#everything changed in B will be changed in A. A and B have a connection
a = [3, 63, 53, 54, 3]
b = a[:]
b[2] = 5
print(f'A = {a}, B = {b}')#now i can change the list B alone
'''
values = list(range(4, 11))
print(values)
values = [5, 3, 9, 0, 1, 5]
values.sort()
print(values)
values.sort(reverse=True)
print(values)

#add methods
snack = ['Pizza', 'Sandwich', 'Juice', 'Bread']
print(snack)
snack[0] = 'Mango'
print(snack)
snack.append('Salmon')#append is acrescentar in portuguese
print(snack)
snack.insert(0, 'Water')
print(snack)
#del methods
del snack[0]
print(snack)
snack.pop(3)
print(snack)
snack.remove('Sandwich')
print(snack)'''
