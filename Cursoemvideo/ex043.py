height = float(input('Insert your height: '))
weight = float(input('Insert your weight: '))
imc = weight / (pow(height, 2))
print('')
print("*"*16)
print(f'Your imc is {imc:.1f}')
if imc < 18.5:
    print('Under weight')
elif imc <= 25:
    print('Ideal weight')
elif imc <= 30:
    print('Overweight')
elif imc <= 40:
    print('Obesity')
else:
    print('Morbid obesity')
print("*"*16)

