expression = input('Insert the expression: ')
lis = []
for char in expression:
    if char == '(':
        lis.append('(')
    elif char == ')':
        if len(lis) > 0:
            lis.pop()
        else:
            lis.append(')')
            break
if len(lis) == 0:
    print('The expression is correct')
else:
    print('Review your expression')
