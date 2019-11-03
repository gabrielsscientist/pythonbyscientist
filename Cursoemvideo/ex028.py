def line():
    print('-=-'*18)
def choosing():
    #numbers = [1, 2, 3, 4, 5]
    #chosen = choice(numbers)
    chosen = randint(1, 10)
    print('')
    print('Thinking...')
    sleep(2)
    line()
    print('Let\'s go, i chose the number')
    print('which do you think it is?')
    return chosen
line()
a = 1
print('Hello i\'m a gabriel´s computer...')
print('I will pick a random number(integer) between 0 and 5')
print('and you have to guess')
line()
answer = input('Ready?(answer with yes or no): ')
if answer.upper() == 'YES':
    from time import sleep
    from random import randint
    chosen = choosing()
    line()
    number = int(input('Answer: '))
    while chosen != number:
        print('')
        line()
        print(f'Oh no, you lose! Try again')
        line()
        number = int(input('Answer: '))
        a += 1
    print('\033[32m')
    line()
    if a == 1:
        print(f'\033[32mCongratulations you got it right in {a} attempt!')
    else:
        print(f'\033[32mCongratulations you got it right in {a} attempts!')
    line()
else:
    print('Ok, bye!')