number = int(input('Insert a number between 0 and 9999: '))
tens = 0
if number < 1000:
    thousands = 0
else:
    if number >= 1000 and number <= 1999:
        thousands = 1
        number = number - 1000
    else:
        if number >= 2000 and number <= 2999:
            thousands = 2
            number = number - 2000
        else:
            if number >= 3000 and number <= 3999:
                thousands = 3
                number = number - 3000

            else:
                if number >= 4000 and number <= 4999:
                    thousands = 4
                    number -= 4000
                else:
                    if number >= 5000 and number <= 5999:
                        thousands = 5
                        number -= 5000
                    else:
                        if number >= 6000 and number <= 6999:
                            thousands = 6
                            number -= 6000
                        else:
                            if number >= 7000 and number <= 7999:
                                thousands = 7
                                number -= 7000
                            else:
                                if number >= 8000 and number <= 8999:
                                    thousands = 8
                                    number -= 8000
                                else:
                                    thousands = 9
                                    number -= 9000
if number < 100:
    hundred = 0
else:
    if number >= 100 and number < 200:
        hundred = 1
        number = number - 100
    else:
        if number >= 200 and number < 300:
            hundred = 2
            number = number - 200
        else:
            if number >= 300 and number < 400:
                hundred = 3
                number = number - 300
            else:
                if number >= 400 and number < 500:
                    hundred = 4
                    number = number - 400
                else:
                    if number >= 500 and number < 600:
                        hundred = 5
                        number = number - 500
                    else:
                        if number >= 600 and number < 700:
                            hundred = 6
                            number = number - 600
                        else:
                            if number >= 700 and number < 800:
                                hundred = 7
                                number = number - 700
                            else:
                                if number >= 800 and number < 900:
                                    hundred = 8
                                    number = number - 800

                                else:
                                    hundred = 9
                                    number = number - 900
    if number < 10:
        number = number
        tens = 0
    else:
        if number >= 10 and number < 20:
            number = number - 10
            tens = 1
        else:
            if number >= 20 and number < 30:
                number = number - 20
                tens = 2
            else:
                if number >= 30 and number < 40:
                    number = number - 30
                    tens = 3
                else:
                    if number >= 40 and number < 50:
                        number = number - 40
                        tens = 4
                    else:
                        if number >= 50 and number < 60:
                            number = number - 50
                            tens = 5
                        else:
                            if number >= 60 and number < 70:
                                number = number - 60
                                tens = 6
                            else:
                                if number >= 70 and number < 80:
                                    number = number - 70
                                    tens = 7
                                else:
                                    if number >= 80 and number < 90:
                                        number = number - 80
                                        tens = 8

                                    else:
                                        number = number - 90
                                        tens = 9

print(f'The number have:\n{thousands} thousands\n{hundred} hundreds\n{tens} tens\n{number} units')
