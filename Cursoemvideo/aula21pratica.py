def factorial(num=1):
    f = 1
    for n in range(num, 0, -1):
        f *= n
    return f


def even(number=1):
    if number % 2 == 0:
        return True
    else:
        return False


fac = int(input('Enter a number to make his factorial: '))
print(f"The factorial is {factorial(fac)}")

num = int(input('\nEnter a number to verify if it\'s even: '))
print(f'Number {num} is even? {even(num)}')