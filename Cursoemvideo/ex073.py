top20 = ('','Santos', 'Palmeiras', 'Flamengo', 'Atlético-MG', 'Corinthians', 'São Paulo', 'Internacional', 'Athletico-PR',
         'Botafogo', 'Bahia', 'Ceará', 'Goiás', 'Grêmio', 'Fortaleza', 'Vasco', 'Fluminense', 'Chapecoense', 'Cruzeiro',
         'CSA', 'Avaí')
print(f'Top 20 > {top20[1:]}')
print('')
print('Top 5')
for i in range(1, 6):
    print(f'{i} = {top20[i]}')
print('')
print('Last 4 teams')
for i in range(17, len(top20)):
    print(f'{i} = {top20[i]}')
print('')
print('Teams in alphabetical order -> ', sorted(top20[1:]))
print('')
print(f'Chapecoense is in position', top20.index('Chapecoense'))