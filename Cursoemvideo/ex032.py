from datetime import date
year = int(input('Insert an year or 0 for current year: '))
if year == 0:
    year = date.today().year
if (year%4) == 0 and (year%100) !=0 or (year%400)==0:
    print(f'The year {year} is leap')
else:
    print(f'The year {year} don\'t is leap')