algo = input('Digite algo: ') # input é por padrão 'str'
print('O tipo primitivo é', type(algo))
print('É numérico?', algo.isnumeric())
print('É dígito?', algo.isdigit())
print('É alfanumérico?', algo.isalnum())
print('Tem somente letras?', algo.isalpha())
print('Tem somente minúsculas?', algo.islower())
print('Tem somente espaços?', algo.isspace())
print('Tem somente maiúsculas?', algo.isupper())
print('Está capitalizada?', algo.istitle())
