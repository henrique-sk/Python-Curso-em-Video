lista = []
jogador = {}
gols = []
while True:
    jogador.clear()
    jogador['nome'] = str(input(f'{"-"*42}\nNome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear()
    for c in range(0, partidas):
        gols.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    lista.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar: [S/N] ')).upper()[0].strip().replace(' ', '')
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('-='*30)
print(f'{"cod ":>4}', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print(f'\n{"-" * 42}')
for k, v in enumerate(lista):
    print(f'{k+1:>3} ', end='')
    for data in v.values():
        print(f'{str(data):<16}', end='')
    print()
while True:
    dados = int(input(f'{42*"-"}\nMostrar dados de qual jogador? [999 para parar] '))
    if dados == 999:
        break
    if dados > len(lista):
        print(f'ERRO! Não existe jogador com o código {dados}! Tente novamente')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[dados - 1]["nome"]}:')
        for k, v in enumerate(lista[dados-1]["gols"]):
            print(f'   No jogo {k+1} fez {v} gols.')
print('<< VOLTE SEMPRE >>')
