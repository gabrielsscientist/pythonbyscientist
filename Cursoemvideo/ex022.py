name = str(input('Whats your name? ')).strip()
print(name.strip().upper())
print(name.strip().lower())
namewithoutspace = name.replace(' ','')
print(f'Your full name have {len(namewithoutspace)} letters')
namesplited = name.split()
print(f'Your first name have {len(namesplited[0])} letters')
