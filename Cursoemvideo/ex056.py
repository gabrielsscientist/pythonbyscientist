sumage = 0
wund20 = 0
bigger = 0
mmo = 'name'
for i in range(1, 5):
    print(f'--- Person {i} ---')
    name = input(f'What\'s the name? ').strip()
    age = int(input(f'What\'s the age? '))
    mw = input(f'Insert M(Men) or W(Woman): ').strip()
    sumage += age
    if mw.lower() == 'w' and age < 20:
        wund20 += 1
    if mw.lower() == 'm':
        if age > bigger:
            bigger = age
            mmo = name
if mmo == 'name':
    print(f'The sum of ages is {sumage} and have {wund20} women under 20')
    if wund20 == 0:
        print(f'The sum of ages is {sumage}')
elif wund20 == 0:
    print(f'The more old man is {mmo} and the sum of ages is {sumage}')
else:
    print(f'The more old man is {mmo}, the sum of ages is {sumage} and have {wund20} women under 20')