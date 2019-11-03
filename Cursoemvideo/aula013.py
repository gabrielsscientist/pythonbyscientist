"""
for i in range(0, 5):
    print(i)

for i in range(5, 0, -1):
    print(i)
"""

ini = int(input('Initial: '))
end = int(input('Final: '))
pas = int(input('Pass: '))
for i in range(ini, end+1, pas):
    print(i)
