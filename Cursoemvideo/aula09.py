Phrase = 'Hi, I´m Gabriel the future billionaire'
#Phrase [ H, i, ,,  , I, ´, m,  , G, a, b, r, i, e, l,  , t, h, e,  , f, u, t, u, r, e,  , b, i, l, l, i, o, n, a, i, r, e]
#index    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37
#-------------SLICING----------------
print(Phrase[8:15])#consider until 14
print(Phrase[8:15:2])#first word, after two in two
print(Phrase[:15]) #index 0 until 14
print(Phrase[27:38])#consider until 37
print(Phrase[27:38:2])#first word, after two by two
print(Phrase[20:])#index20 until the end
print(Phrase[20::3])#index20 until the end going three by three
Phrase = 'Gabriel de Lucas is blessed by God'
#-------------ANALYZE----------------
print(len(Phrase))#The function returns how many chars have in object(var or array)
print(Phrase.count('a'))#The function returns how many chars a have in object(var or array)
print(Phrase.count(Phrase[0]))#The function returns how many chars a have between index 0 until 4
print(Phrase.find('blessed'))#The function returns where is the string, here returns 20(where starts the word)
print(Phrase.find('city'))#The function returns -1 (false),because don´t have word city in object(var or array)
print('Have a word town in Phrase object? {}'.format('town'in Phrase))#Returns True or false.
#--------------TRANSFORMATION----------------
print(Phrase.replace('Gabriel de Lucas is','All peoples are'))#the function replaces the first word to the second
print(Phrase.upper())#the function transform the letters in capital letters
print(Phrase.lower())#the function transform the letters in small letters
print(Phrase.capitalize())#the function transform the first letter in capital letter
print(Phrase.title())#the function transform the firsts letters in capital letters
Phrase='    Learn Python language    '
print(Phrase.strip())#the function take off the spaces at the beginning and at the end
print('Python' in Phrase)
print(Phrase.rstrip())#the function take off the spaces at the right side(end)
print(Phrase.lstrip())#the function take off the spaces at the left side(beginning)
Phrase = Phrase.split()
print(Phrase[1])
print(Phrase[1][0])#the first bracket is about word, the second is about letter


