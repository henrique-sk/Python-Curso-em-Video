tabela = 'Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',\
         'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',\
         'Atletico-GO', 'Santos', 'Ceará', 'Internacional',\
         'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude',\
         'Grêmio', 'Bahia', 'Sport', 'Chapecoense'
print(20 * '-=')
print(f'Lista de times do Brasileirão: {tabela}')
print(20 * '-=')
print(f'Os 5 primeiros são {tabela[:5]}')
print(20 * '-=')
print(f'Os 4 últimos são {tabela[-4:]}')
print(20 * '-=')
print(f'Times em ordem alfabética{sorted(tabela)}')
print(20 * '-=')
print(f'O Chapecoense está na {tabela.index("Chapecoense")+1}ª'
      f' posição.')
