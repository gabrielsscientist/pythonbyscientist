num1 = int(input('Digite o primeiro número: ')) #casting de int
num2 = int(input('Digite o segundo número: ')) #casting de int
#é necessário o cast pois input retorna uma string
#type(variable)=>to consult type of data in variable
print('A soma entre {} e {} = {}'.format(num1,num2,num1+num2))
#print('A soma é:',num1+num2) ou
#print(f'A soma é {num1+num2}') ou
#print('A soma entre {} e {} = {}'.format(num1,num2,num1+num2))