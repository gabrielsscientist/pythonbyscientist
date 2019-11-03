c = smaller = thousands = Sum = 0
namesmaller = yn = 'S'
print(':'*30)
print('          Big store')
print(':'*30)
while True:
    yn = 'S'
    name = input('What\'s the name of product? ')
    price = float(input('What\'s the price of product? $'))
    while yn.upper() != 'N' and yn.upper() != 'Y':
        yn = input('Do you want type more? [Y/N]').upper()
    print('')
    Sum += price
    c += 1
    if price > 1000:
        thousands += 1
    if c == 1 or smaller > price:
        smaller = price
        namesmaller = name
    if yn.upper() == 'N':
        break
print(f'Total price is {Sum}, the cheapest product is {namesmaller} and have ', end='')
print(f'{thousands} product above $1000.00' if thousands == 1 else f'{thousands} products above $1000.00')

if notas50 == 1:
    if notas20 == 1:
        if notas10 == 1:
            if notas1 == 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} nota de R$ 20,00.\n{notas10} nota de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} nota de R$ 20,00.\n{notas10} nota de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} nota de R$ 20,00.\n{notas10} nota de R$ 10,00')
        elif notas10 > 1:
            if notas1 == 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} nota de R$ 20,00.\n{notas10} notas de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} nota de R$ 20,00.\n{notas10} notas de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} nota de R$ 20,00.\n{notas10} notas de R$ 10,00')
        else:
            if notas1 == 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} nota de R$ 20,00.\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} nota de R$ 20,00.\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} nota de R$ 20,00.')
    elif notas20 > 1:
        if notas10 == 1:
            if notas1 == 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} notas de R$ 20,00.\n{notas10} nota de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} notas de R$ 20,00.\n{notas10} nota de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} notas de R$ 20,00.\n{notas10} nota de R$ 10,00')
        elif notas10 > 1:
            if notas1 == 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} notas de R$ 20,00.\n{notas10} notas de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} notas de R$ 20,00.\n{notas10} notas de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} notas de R$ 20,00.\n{notas10} notas de R$ 10,00')
        else:
            if notas1 == 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} notas de R$ 20,00.\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} notas de R$ 20,00.\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} nota de R$ 50,00.\n{notas20} notas de R$ 20,00.')
    else:
        if notas10 == 1:
            if notas1 == 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas10} nota de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas10} nota de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} nota de R$ 50,00.\n{notas10} nota de R$ 10,00')
        elif notas10 > 1:
            if notas1 == 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas10} notas de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas10} notas de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} nota de R$ 50,00.\n{notas10} notas de R$ 10,00')
        else:
            if notas1 == 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} nota de R$ 50,00.\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} nota de R$ 50,00.')
elif notas50 > 1:
    if notas20 == 1:
        if notas10 == 1:
            if notas1 == 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} nota de R$ 20,00.\n{notas10} nota de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} nota de R$ 20,00.\n{notas10} nota de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} nota de R$ 20,00.\n{notas10} nota de R$ 10,00')
        elif notas10 > 1:
            if notas1 == 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} nota de R$ 20,00.\n{notas10} notas de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} nota de R$ 20,00.\n{notas10} notas de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} nota de R$ 20,00.\n{notas10} notas de R$ 10,00')
        else:
            if notas1 == 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} nota de R$ 20,00.\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} nota de R$ 20,00.\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} nota de R$ 20,00.')
    elif notas20 > 1:
        if notas10 == 1:
            if notas1 == 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} notas de R$ 20,00.\n{notas10} nota de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} notas de R$ 20,00.\n{notas10} nota de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} notas de R$ 20,00.\n{notas10} nota de R$ 10,00')
        elif notas10 > 1:
            if notas1 == 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} notas de R$ 20,00.\n{notas10} notas de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} notas de R$ 20,00.\n{notas10} notas de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} notas de R$ 20,00.\n{notas10} notas de R$ 10,00')
        else:
            if notas1 == 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} notas de R$ 20,00.\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} notas de R$ 20,00.\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} notas de R$ 50,00.\n{notas20} notas de R$ 20,00.')
    else:
        if notas10 == 1:
            if notas1 == 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas10} nota de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas10} nota de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} notas de R$ 50,00.\n{notas10} nota de R$ 10,00')
        elif notas10 > 1:
            if notas1 == 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas10} notas de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas10} notas de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} notas de R$ 50,00.\n{notas10} notas de R$ 10,00')
        else:
            if notas1 == 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas50} notas de R$ 50,00.\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas50} notas de R$ 50,00.')
else:
    if notas20 == 1:
        if notas10 == 1:
            if notas1 == 1:
                print(f'{notas20} nota de R$ 20,00.\n{notas10} nota de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas20} nota de R$ 20,00.\n{notas10} nota de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas20} nota de R$ 20,00.\n{notas10} nota de R$ 10,00')
        elif notas10 > 1:
            if notas1 == 1:
                print(f'{notas20} nota de R$ 20,00.\n{notas10} notas de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas20} nota de R$ 20,00.\n{notas10} notas de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas20} nota de R$ 20,00.\n{notas10} notas de R$ 10,00')
        else:
            if notas1 == 1:
                print(f'{notas20} nota de R$ 20,00.\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas20} nota de R$ 20,00.\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas20} nota de R$ 20,00.')
    elif notas20 > 1:
        if notas10 == 1:
            if notas1 == 1:
                print(f'{notas20} notas de R$ 20,00.\n{notas10} nota de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas20} notas de R$ 20,00.\n{notas10} nota de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas20} notas de R$ 20,00.\n{notas10} nota de R$ 10,00')
        elif notas10 > 1:
            if notas1 == 1:
                print(f'{notas20} notas de R$ 20,00.\n{notas10} notas de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas20} notas de R$ 20,00.\n{notas10} notas de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas20} notas de R$ 20,00.\n{notas10} notas de R$ 10,00')
        else:
            if notas1 == 1:
                print(f'{notas20} notas de R$ 20,00.\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas20} notas de R$ 20,00.\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas20} notas de R$ 20,00.')
    else:
        if notas10 == 1:
            if notas1 == 1:
                print(f'{notas10} nota de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas10} nota de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas10} nota de R$ 10,00')
        elif notas10 > 1:
            if notas1 == 1:
                print(f'{notas10} notas de R$ 10,00\n{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas10} notas de R$ 10,00\n{notas1} notas de R$ 1,00')
            else:
                print(f'{notas10} notas de R$ 10,00')
        else:
            if notas1 == 1:
                print(f'{notas1} nota de R$ 1,00')
            elif notas1 > 1:
                print(f'{notas1} notas de R$ 1,00')
            else:
                print(f'')