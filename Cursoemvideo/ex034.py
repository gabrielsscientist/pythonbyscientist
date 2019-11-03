salary = float(input('Insert the salary: '))
if salary > 1250.00:
    print(f'\033[7;30mYour new salary is \033[1;32m{salary * 1.10:.2f} reais')
else:
    print(f'Your new salary is \033[1;32m{salary * 1.15:.2f} reais')
