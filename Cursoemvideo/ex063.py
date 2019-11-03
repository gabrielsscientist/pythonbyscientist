num = int(input('How many terms of Fibonacci\'s sequence you can show?: '))
anterior = 0
atual = 1
i = 3
if num == 2:
    print(f'{anterior}, {atual}', end='')
elif num == 1:
    print(f'{anterior}', end='')
elif num >= 3:
    proximo = atual + anterior
    print(f'{anterior}, {atual}, {proximo}', end='')
while i < num:
    anterior = atual
    atual = proximo
    proximo = atual + anterior
    i += 1
    print(f', {proximo}', end='')