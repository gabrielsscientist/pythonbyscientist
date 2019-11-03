for i in range(4, 1000):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    else:
        print(f'{i} Is cousin')
