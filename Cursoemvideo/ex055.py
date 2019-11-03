bigger = 0
smaller = 1000
for i in range(0, 5):
    Weight = float(input('Insert the Weight: '))
    if Weight > bigger:
        bigger = Weight
    if smaller > Weight:
        smaller = Weight
print(f'The Highest weight is {bigger}Kg and the lowest weight is {smaller}Kg')
