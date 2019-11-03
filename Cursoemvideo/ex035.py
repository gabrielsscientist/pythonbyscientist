print('''Triangle analyser''')
print('-=-'*10)
straight1 = float(input('Insert the first straight: '))
straight2 = float(input('Insert the second straight: '))
straight3 = float(input('Insert the third straight: '))
print('-=-'*10)
print('')
if (straight1+straight2) > straight3 and (straight3+straight2) > straight1 and (straight1+straight3) > straight2:
    print('\033[1mCan be formed a ', end='')
    if straight1 == straight2 == straight3:
        print('equilateral', end='')
    elif straight1 == straight2 or straight2 == straight3 or straight1 == straight3:
        print('isosceles', end='')
    else:
        print('scalene', end='')
    print(' triangle')
else:
    print('Can\'t be formed a triangle')