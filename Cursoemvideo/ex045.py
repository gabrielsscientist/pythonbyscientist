from random import choice
from time import sleep
print('Lets\'s play a paper, scissor, stone')
print('I will choice...')
sleep(3)
print('I chose')
print("Insert \"paper\" \"scissor\" or \"stone\"")
player = input('It\'s your turn: ')
player = str(player.strip().capitalize())
computer = ['Paper', 'Scissor', 'Stone']
computer = choice(computer)
print('')
if player == 'Scissor' or player == 'Paper' or player == 'Stone':
    print(f'I chose {computer} and you chose {player}')
    if player == computer:
        print('Tied')
    else:
        if player == 'Paper':
            if computer == 'Scissor':
                print('I won!')
            else:
                print('You won!')
        elif player == 'Stone':
            if computer == 'Scissor':
                print('You won!')
            else:
                print('I won!')
        else:
            if computer == 'Stone':
                print('I won!')
            else:
                print('You won!')
else:
    print('Play right')
