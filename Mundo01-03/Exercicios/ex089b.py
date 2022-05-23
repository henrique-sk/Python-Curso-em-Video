lista = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N] ').upper().strip().replace(' ', '')
    if resposta in 'N':
        break
print(30*'-=',
      f'\n{"No.":<3}', f'{"NOME":<15}', f'{"MÉDIA":<9}',
      f'\n{30 *"-"}')
for chave, valor in enumerate(lista):
    print(f'{chave+1:<3}{valor[0]:<17}{valor[2]:.1f}')
mostrar = 0
while mostrar != 999:
    print(40 * '-')
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar <= len(lista):
        print(f'Notas de {lista[mostrar-1][0]} são {lista[mostrar-1][1]}')
print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')
