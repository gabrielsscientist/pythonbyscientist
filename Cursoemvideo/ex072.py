while True:
    num = int(input('Enter a number between 0 and 20: '))
    if 0 <= num <= 20:
        break
    else:
        print('Try again.', end='')
numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
           'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
print(f'You entered number {numbers[num]}')
