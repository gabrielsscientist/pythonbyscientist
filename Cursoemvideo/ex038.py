n1 = float(input('\033[7mInsert the first number:\033[m '))
n2 = float(input('\033[7mInsert the second number:\033[m '))
if n1 > n2:
    print('\033[1mThe first value is bigger than the second')
elif n1 == n2:
    print('\033[1mAre equal values')
else:
    print('\033[1mThe second value is bigger than the first')