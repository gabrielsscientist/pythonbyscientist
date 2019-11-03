num1 = (input('Digite o primeiro número: ')) #casting de int
num2 = (input('Digite o segundo número: ')) #casting de int
#é necessário o cast pois input retorna uma string
#type(variable)=>to consult type of data in variable
print(num1.isdecimal()) #exists multiples functions to test type of data(.isnumeric(),.isalpha() ->alphabet), returning true or false, but don´t can apply cast
print('A soma entre {} e {} = {}'.format(num1,num2,num1+num2))
#exists multiple casts function, like str() -> string,int() -> integer, float() and bool() -> boolean