from datetime import datetime as dt

cadastro = {}
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
cadastro['idade'] = dt.now().year - nasc
cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = ((cadastro['contratação'] + 35) - dt.today().year) + cadastro['idade']
print(30*'-=')
for k, v in cadastro.items():
    print(f'  - {k} tem o valor {v}.')
