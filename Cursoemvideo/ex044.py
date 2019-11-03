print('^^^^^^^^Gabriel\'s Store^^^^^^^^^^')
price = float(input('Purchase price: $'))
print('')
print('These are the payments methods')
print('*'*22)
print('1 for: cash payment')
print('---Payment card---')
print('2 for: sight')
print('3 for: 2 times')
print('4 for: 3 times or more')
print('*'*22)
print('')
method = int(input('What method do you want?(corresponding number) '))
if method == 4:
    install = int(input('How many installments? '))
    if install < 3:
        print('\033[31mWrong selected method')
    else:
        print('The products will cost $', end='')
        print(f'{price*1.20} = {install}x ${(price*1.20) / install}')
elif method < 1 or method > 4:
    print('\033[31mThis method doesn\'t exists')
else:
    print('The products will cost $', end='')
    if method == 1:
        print(f'{price * 0.90}')
    elif method == 2:
        print(f'{price * 0.95}')
    else:
        print(f'{price} = 2x ${price * 0.5}')
