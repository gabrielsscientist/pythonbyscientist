numbers = []
maior = menor = 0
for i in range(0, 5):
    num = int(input('Enter a number: '))
    if i == 0 or num > numbers[-1]:
        numbers.append(num)
    else:
        pos = 0
        while pos < len(numbers):
            print()
print(numbers)
