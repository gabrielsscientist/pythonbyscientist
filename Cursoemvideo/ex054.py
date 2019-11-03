from datetime import date

bigger = 0
smaller = 0
for i in range(0, 7):
    age = int(input('When you were born? '))
    age = date.today().year - age
    if age < 18:
        smaller += 1
    else:
        bigger += 1
if bigger == 0:
    print(f'Don\'t have any people over 18 and have {smaller} peoples under 18')
elif bigger == 1:
    print(f'Have one people over 18 and have {smaller} peoples under 18')
elif smaller == 0:
    print(f'Have {bigger} peoples over 18 and don\'t have any people under 18')
elif smaller == 1:
    print(f'Have {bigger} peoples over 18 and have one people under 18')
else:
    print(f'Have {bigger} peoples over 18 and have {smaller} peoples under 18')
