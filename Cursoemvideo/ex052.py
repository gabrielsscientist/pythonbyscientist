num = int(input('Insert a integer number: '))
cont = 0
for i in range(1, (num + 1)):
    if num % i == 0:
        cont += 1
if cont < 3:
    print(f'{num} is cousin')
else:
    print(f'{num} isn\'t cousin')
