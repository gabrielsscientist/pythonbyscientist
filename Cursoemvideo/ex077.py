words = ('Carro', 'Casa', 'Moto', 'Comida', 'Dinheiro', 'Caderno', 'Felicidade')
w = 0
for w in words:
    print(f'The word {w}')
    print('Possui as vogais:')
    for l in w:
        if l.lower() in 'aeiou':
            print(l)

