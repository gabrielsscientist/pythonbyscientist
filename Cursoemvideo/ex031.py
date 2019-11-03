distance = float(input('How many kilometers away is the trip? '))
#print(f'The ticket will be cost {distance*0.5} reais') if distance<201 else print(f'The ticket will be cost {distance * 0.45} reais')
if distance <= 200:
    print(f'The ticket will be cost {distance*0.5} reais')
else:
    print(f'The ticket will be cost {distance * 0.45} reais')