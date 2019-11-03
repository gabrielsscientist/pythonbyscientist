def linha(msg):
    print("-" * 10)
    print(msg)
    print("-" * 10)


def soma(a, b):
    print(f"{a} + {b} = {a + b}")
    return a + b


def contador(*num):
    print(num)


def dobro(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


linha('Abaixo está a soma')
soma(3, 2)  # ou soma(a=3, b=2) ou soma(b=3, a=2))
contador(2, 4, 5, 2, 6, 9)  # adiciona na tupla
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
linha('Valores normal da lista: ')
dobro(valores)
print(valores)
linha('Valores após serem dobrados: ')
print(valores)
