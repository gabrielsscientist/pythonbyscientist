'''pessoa = {'Nome': 'Gabriel', 'Dinheiro': 1000000, 'Carro': 'Ferrari'}
print(f'{pessoa["Nome"]} tinha ${pessoa["Dinheiro"]} e comprou uma {pessoa["Carro"]}')
pessoa['Empresa'] = 'Google'
#del pessoa['nome']
print(pessoa)
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
for k, v in pessoa.items():
    print(f'{k}: {v}')

pessoa2 = {'Nome': 'Gisele', 'Carro': 'BMW'}
pessoas = [pessoa, pessoa2]
print(pessoas)'''
estado = dict()
Brasil = list()
for i in range(0, 2):
    estado['Nome'] = input('Qual o nome do estado?')
    estado['Sigla'] = input('Qual a sigla do estado?')
    Brasil.append(estado.copy())
    estado.clear()
print(Brasil)
