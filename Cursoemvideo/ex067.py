i = 1
while True:
    num = int(input('Insert a number to make a multiplication table of him: '))
    if num < 0:
        break
    print('')
    i = 1
    while i <= 10:
        print(f'{num} x {i} = {num * i}')
        i += 1
        if i == 11:
            print('')
