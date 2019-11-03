from datetime import date
born = int(input('\033[4mInsert the year you were born:\033[m '))
currentyear = date.today().year
if currentyear - born <= 9:
    print('\033[1mBaby category')
elif currentyear - born <= 14:
    print('\033[1mChild category')
elif currentyear - born <= 19:
    print('\033[1mJunior category')
elif currentyear - born <= 25:
    print('\033[1mSenior category')
else:
    print('\033[1mMaster category')