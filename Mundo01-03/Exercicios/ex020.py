from random import sample

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
ordem = sample([a1, a2, a3, a4], k=4)
print('Os alunos irão se apresentar na seguinte ordem:\n1. {}\n2. {}\n3. {}\n4. {}'.format(ordem[0], ordem[1], ordem[2], ordem[3]))