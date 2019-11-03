from datetime import date
born = int(input('What\'s your year\'s birth? '))
year = date.today().year
if year - born == 18:
    print('\033[1mYou must enlist this year')
elif year - born < 18:
    if year - born == 17:
        print(f'\033[1mYou must enlist in 1 year in the year {year+1}')
    else:
        print(f'\033[1mYou must enlist in {18-(year - born)} years in the year {year + (18-(year - born))}')
else:
    if (year - born) == 19:
        print(f'\033[1mYou should have enlisted 1 year ago in {year-1}')
    else:
        print(f'\033[1mYou should have enlisted {(year - born)-18} years ago in the year {year - ((year - born)-18)}')
