word = input('Insert an word: ')
word = word.strip().lower().split()
word = ''.join(word)
inverse = word[::-1]
"""for i in range(len(word)-1, -1, -1):
    inverse += (word[i])"""
print(f'\033[1m{word} in reverse is {inverse}')
if inverse == word:
    print('\033[32mIs palindrome')
else:
    print('\033[31mIsn\'t palindrome')

"""
isntequal = 0
equal = 0
for i in range(0, word.__len__()):
    if word[i] == word[((word.__len__()) - 1) - i]:
        equal += 1
    else:
        isntequal += 1

if isntequal > 0:
    print('Isn\'t palindrome.')
else:
    print('Is palindrome')"""
