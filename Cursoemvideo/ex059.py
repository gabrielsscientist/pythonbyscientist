print('=^=^=^= Menu =^=^=^=\n'
      '\033[7m|[1] Add            \033[m|\n'
      '\033[7m|[2] Multiply       \033[m|\n'
      '\033[7m|[3] Division       \033[m|\n'
      '\033[7m|[4] New numbers    \033[m|\n'
      '\033[7m|[5] Exit program   \033[m|\n'
      '\033[7m          Gabriel\'s \033[m|\n'
      '~v=v=v=v=v=v=v=v=v=v~\n')
num1 = float(input('Insert the first number: '))
num2 = float(input('Insert the second number: '))
option = int(input('Insert the option: '))
print('')
while option != 5:
    if option == 1:
        print(f'\033[1;36mThe sum is {num1 + num2}')
    elif option == 2:
        print(f'\033[1;36mThe multiplication is {num1 * num2}')
    elif option == 3:
        print(f'\033[1;36mThe division is {num1 / num2}')
    else:
        num1 = int(input('\033[mInsert the number: '))
        num2 = int(input('Insert the number: '))
    print('')
    option = int(input('\033[mInsert the option: '))
    print('')
print('\033[1;32mBye!')
