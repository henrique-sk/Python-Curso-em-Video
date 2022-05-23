lista = []
cadastro = {}
soma = media = 0
while True:
    cadastro['nome'] = str(input('Nome: '))
    while True:
        cadastro['sexo'] = str(input('Sexo: [M/F] ')).upper()[0].strip().replace(' ', '')
            # [0] só a primeira letra
        if cadastro['sexo'] in 'FM':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    lista.append(cadastro.copy())
    while True:
        resposta = str(input('Quer continuar: [S/N] ')).upper().strip().replace(' ', '')
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
media = soma / len(lista)
print(f'{"-="*30}\n- O grupo tem {len(lista)} pessoas.'
      f'\n- A média de idade é de {media:5.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for c in lista:
    if c['sexo'] in 'fF':
        print(c['nome'], end=' ')
print('\n- Lista das pessoas que estão acima da média: ', end='')
for p in lista:
    if p['idade'] > media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
print('\n<< ENCERRADO >>')
