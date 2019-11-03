days = int(input('How many days rented? '))
kilometers = float(input('How many kilometers rolled? '))
print(f'Total pay: R$ {(days*60)+(kilometers*0.15):.2f}')