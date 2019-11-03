reais = int(input('Quantos reais você quer sacar? '))
print('')
notas50 = notas20 = notas10 = notas1 = 0
if reais // 50 >= 1:
    notas50 = (reais // 50)
    reais = (reais % 50)
    print(f'{notas50} cédula de R$50,00' if notas50 == 1 else f'{notas50} cédulas de R$50,00')
if reais // 20 >= 1:
    notas20 = reais // 20
    reais = reais % 20
    print(f'{notas20} cédula de R$20,00' if notas20 == 1 else f'{notas20} cédulas de R$20,00')
if reais // 10 >= 1:
    notas10 = reais // 10
    reais = reais % 10
    print(f'{notas10} cédula de R$10,00' if notas10 == 1 else f'{notas10} cédulas de R$10,00')
if reais // 1 >= 1:
    notas1 = reais // 1
    print(f'{notas1} cédula de R$1,00' if notas1 == 1 else f'{notas1} cédulas de R$1,00')
