nome = input('Digite seu nome completo: ').strip()
nome = nome.split()
# print('Seu primeiro e último nome fica {} {}.'.format(nome.split()[0], nome.split()[len(nome.split()) - 1]))
print('Seu primeiro e último nome fica {} {}.'.format(nome[0], nome[len(nome) - 1]))
