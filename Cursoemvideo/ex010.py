print('We go help you to exchange coins')
real = float(input('Enter how much reais you have: R$ '))
dollar = real/3.74
# or dollars = real*0.27
euro = real/4.20
#euro = real*0.24
yen = real*28.79
if(dollar == 1):
    print(f'You can buy {dollar} dollar')
else:
    print(f'You can buy {dollar:.2f} dollars')
if(euro == 1):
    print(f'You can buy {euro:.2f} euro')
else:
    print(f'You can buy {euro:.2f} euros')
if(yen == 1):
    print(f'You can buy {yen:.2f} yen')
else:
    print(f'You can buy {yen:.2f} yens')
