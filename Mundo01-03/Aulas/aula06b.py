n = input('Digite algo: ')
print(n.isnumeric())
# pergunta se é possível converter para número

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome)) # em 20 espaços
print('Prazer em te conhecer {:>20}!'.format(nome)) # alinhado direita
print('Prazer em te conhecer {:<20}!'.format(nome)) # alinhado esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) # centralizado
print('Prazer em te conhecer {:=^20}!'.format(nome)) # centralizado com =

