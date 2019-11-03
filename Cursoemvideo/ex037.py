number = int(input('\033[4;30mInsert a integer number:\033[m '))
print('')
print('''\033[1;36mChoice one base to convert
\033[1;34m1 for binary
2 for octal 
3 for hexadecimal
''')
option = int(input('\033[4;30mChosen base:\033[m '))
if option == 1:
    print(f'\033[32mNumber {number} converted to binary is {bin(number)[2:]}')
elif option == 2:
    print(f'\033[32mNumber {number} converted to octal is {oct(number)[2:]}')
elif option == 3:
    print(f'\033[32mNumber {number} converted to hexadecimal is {hex(number)[2:]}')
else:
    print('\033[31mThis base doesn\'t exist')
