print('\033[32m$----------LOAN----------$')
housevalue = float(input('\033[7mWhat\'s the value of the house?\033[m '))
salary = float(input('\033[7mWhat\'s your salary?\033[m '))
years = int(input('\033[7mHow many years you want to pay?\033[m '))
print('\033[30m__'*21)
print(f'\033[4;30mThe installments will cost ${housevalue/(years*12):.2f} per month')
print('')
if housevalue/(years*12) > (salary*0.3):
    print('\033[1;31mTHE INSTALLMENTS SURPASSED 30% OF YOUR SALARY')
    print('\033[31mYou can\'t do the loan.')
else:
    print('\033[32mYou can do the loan')
