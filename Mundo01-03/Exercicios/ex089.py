lista = []
aluno = []
notas = []
media = []
while True:
    aluno.append(input('Nome: '))
    for s in range(0, 2):
        notas.append(float(input(f'Nota {s+1}: ')))
    aluno.append(notas[:])
    aluno.append((aluno[1][0]+aluno[1][1])/2)
    notas.clear()
    lista.append(aluno[:])
    aluno.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N] ').upper().strip().replace(' ', '')
    if resposta in 'N':
        break
print(30*'-=',
      f'\n{"No.":<3}{"NOME":<15}{"MÉDIA":<9}',
      f'\n{30 *"-"}')
for chave, valor in enumerate(lista):
    print(f'{chave+1:<3}{valor[0]:<17}{valor[2]:.1f}')
print(40*'-')
mostrar = 0
while mostrar != 999:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar <= len(lista):
        print(f'Notas de {lista[mostrar-1][0]} são {lista[mostrar-1][1]}')
        print(40 * '-')
print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')
