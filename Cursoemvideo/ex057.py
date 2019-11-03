MW = input('Insert M(if you are men)or W(if you are woman): ')
while MW.upper() != 'W' and MW.upper() != 'M':
    MW = input(f'\033[31mInvalid!\033[m Insert M or W: ')
print(f'\033[32m{MW.upper()} registered successfully')
