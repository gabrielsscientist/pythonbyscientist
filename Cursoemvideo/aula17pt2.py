person = ['Gabriel', 18, 'Floriscraulria', 900]
I = [person[:2], person[2:]]
# I = [['Gabriel', 18], ['Floriscraulria', 900]]
#print(I)
pessoa = []
pessoas = []
for i in range(0, 3):
    pessoa.append(input('What\'s your name? '))
    pessoa.append(int(input('How old are you? ')))
    pessoas.append(pessoa[:])
    # pessoas.append(pessoa) return [[], [], []]
    pessoa.clear()
for p in pessoas:
    if p[1] >= 18:
        print(f'{p[0]} é maior idade')
    else:
        print(f'{p[0]} é menor de idade')

print(pessoas)
