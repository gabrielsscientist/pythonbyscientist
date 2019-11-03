yn = 'yes'
sum = c = bigger = smaller = 0
while yn.lower() != 'no':
    c += 1
    num = int(input('Insert the number: '))
    yn = input('Do you want continue?(type yes or no) ')
    print('')
    if c == 1:
        bigger = smaller = num
    else:
        if num > bigger:
            bigger = num
        elif smaller > num:
            smaller = num
    sum += num
print(f'The average is {sum / c}\nThe higher number is {bigger} and the lowest number is {smaller}')
