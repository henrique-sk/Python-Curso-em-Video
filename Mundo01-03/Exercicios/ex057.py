c = 0
while c == 0:
    sexo = input('Digite seu sexo: [M/F]: ').strip().upper()[0]
    # [0] - para ler somente a primeira letra digitada
    if sexo == 'M':
        print('Você é do sexo masculino!')
        c += 1
    elif sexo == 'F':
        print('Você é do sexo feminino!')
        c += 1
    else:
        print('Opção inválida!')

#ALTERNATIVA
# sexo = input('Informe um sexo [M/F]: ').strip().upper()[0]
# while sexo not in 'FM':
#     sexo = input('Valor inválido!'
#                  '\nInforme um sexo [M/F]: ').strip().upper()[0]
# print('Sexo {} registrado.'.format(sexo))
