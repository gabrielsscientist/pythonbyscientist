def line():
    print('\033[34m--' * 11)


def line2(i, c):
    if c.strip().lower() == 'red':
        print('\033[31m^' * i)
    elif c.strip().lower() == 'green':
        print('\033[32m^' * i)
    else:
        print('\033[36m^' * i)


line()
grade1 = float(input('Insert the first grade: '))
grade2 = float(input('Insert the second grade: '))
line()
print('')
print(f'\033[4;30mThe average is {(grade1 + grade2) / 2:.2f}')
print('')
if (grade1 + grade2) / 2 < 5:
    line2(11, 'red')
    print('\033[1;31mDisapproved')
    line2(11, 'red')
elif 5 <= (grade1 + grade2) / 2 < 7:
    line2(8, 'blue')
    print('\033[1;36mRecovery')
    line2(8, 'blue')
else:
    line2(8, 'green')
    print('\033[1;32mApproved')
    line2(8, 'green')
