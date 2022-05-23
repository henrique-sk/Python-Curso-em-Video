pessoas = {'nome': 'Henrique', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k, end=' ')
print('\n')
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('\n', end='')
del pessoas['sexo']
pessoas['peso'] = 98.5
pessoas['nome'] = 'Lord'
for k, v in pessoas.items():
    print(f'{k} = {v}')
