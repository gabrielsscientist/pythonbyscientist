from math import hypot
adjacent = float(input('Insert a adjacent leg: '))
opost = float(input('Insert a opost leg: '))
print(f'Hypotenuse is {hypot(opost,adjacent):.6f}')
#or sqrt((adjacent*adjacent)+(opost*opost)) or sqrt((pow(adjacent,2)) + (pow(opost,2)))
