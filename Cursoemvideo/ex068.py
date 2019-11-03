from random import randint
from time import sleep
playwin = 1
c = 0
while playwin > 0:
    computernum = randint(0, 10)
    playerporo = input('Choice pair or odd: ').strip().upper()
    playernum = int(input('Choice a number between 0 and 10: '))
    print('')
    if playerporo == 'PAIR':
        print(f'Ok, i\'m odd')
    else:
        print(f'Ok, i\'m pair')
    print(f'I chose the number {computernum}')
    sleep(2)
    if (playernum + computernum) % 2 == 0:
        print(f'{playernum} + {computernum} = {playernum + computernum}. {playernum + computernum} is pair.')
        if playerporo == 'ODD':
            playwin -= 1
    else:
        print(f'{playernum} + {computernum} = {playernum + computernum}. {playernum + computernum} is odd.')
        if playerporo == 'PAIR':
            playwin -= 1
    print('')
    if playwin == 1:
        print('\033[32mYOU WONN!')
        c += 1
    else:
        print('\033[32mI WONN!')
    print('\033[m')
    print('')
print(f'\033[36mYou won {c} times')
