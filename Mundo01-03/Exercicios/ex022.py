nome = input('Digite seu nome completo: ').strip()
print('Em maiúsculas: {}\nEm minúsculas: {}\nTotal de letras: {}\nSeu primeiro nome é {} e ele tem {} letras.'.format(nome.upper(), nome.lower(), len(nome.replace(' ','')), nome.split()[0], len(nome.split()[0])))

# OU

# nome = str(input('Digite seu nome completo: ')).strip()
# print('Em maiúsculas: {}\nEm minúsculas: {}\nTotal de letras: {}\nSeu primeiro nome é {} e ele tem {} letras.'.format(nome.upper(), nome.lower(), len(nome) - nome.count(' '), nome.split()[0], nome.find(' ')))