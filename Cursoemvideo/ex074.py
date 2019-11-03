from random import randint
numbers = randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)
print(f'I drew these numbers {numbers}')
print(f'\nThe biggest number is {max(numbers)} and the smallest number is {min(numbers)}')