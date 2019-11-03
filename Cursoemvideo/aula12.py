name = input('What\'s your name? ')

if (name.strip().upper().split())[0] == 'GABRIEL':
    print('Your first name is the same as mine!')
elif (name.strip().upper().split())[0] == 'GISELE':
    print('Your first name is the same as my mom´s name!')
else:
    print('Your name is not the same as mine or my mother\'s.')
print(f'Have a good day, {name.strip().title()}!')