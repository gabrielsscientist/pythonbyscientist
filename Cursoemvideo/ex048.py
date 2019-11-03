Sum = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        Sum += i
        cont += 1
print(f'We have {cont} odd values between 1 and 500. The sum is {Sum}')
