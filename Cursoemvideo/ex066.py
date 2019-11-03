c = sum = 0
while True:
    num = int(input('Insert a number or \"0\" to stop: '))
    if num == 0:
        break
    sum += num
    c += 1
print(f'The sum is {sum} and was typed {c} numbers' if c > 1 else f'The sum is {sum} and was typed 1 number')