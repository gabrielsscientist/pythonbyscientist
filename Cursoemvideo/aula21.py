def contador(i, f, p):
    """
    contagem de i até f de p em p.
    exemplo: 1 até 10 de 2 em 2(1, 3, 5, 7, 9)
    :param i: inicio
    :param f: fim
    :param p: passo
    """
    print(f'Contando de {i} até {f} de {p} em {p}')
    while i < f:
        print(f'-> {i} ', end='')
        i += p


def soma(*num):
    soma = 0
    for i in num:
        soma += i
    return soma


def somaopcional(a, b, c=0):
    """
    o programa soma a + b + c
    :param a:
    :param b:
    :param c: opcional
    """
    print(f"Soma é: {a + b + c}")


def teste():
    x = 8
    print('Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


help(contador)
# print(contador.__doc__)
s1 = soma(2, 3, 4)
s2 = soma(1, 8)
s3 = soma(6)
print(f'As somas deram {s1}, {s2} e {s3}')