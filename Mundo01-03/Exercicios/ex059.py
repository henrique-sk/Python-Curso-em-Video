v1 = 0
v2 = 0
opção = 4
while opção != 5:
    if opção == 0:
        opção = int(input('\nEscolha o que fazer com {} e {}:'
                          '\n[1]Somar'
                          '\n[2]Multiplicar'
                          '\n[3]Saber qual é o maior'
                          '\n[4]Escolher novos números'
                          '\n[5]Sair do programa'
                          '\nDigite uma das opções: '.format(v1, v2)))
    elif opção == 1:
        print('\n>>> A soma entre {} e {} é {}.'.format(v1, v2, v1 + v2))
        opção = 0
    elif opção == 2:
        print('\n>>> A multiplicação entre {} e {} é {}.'.format(v1, v2, v1 * v2))
        opção = 0
    elif opção == 3:
        if v1 > v2:
            print('\n>>> O maior valor entre {} e {} é {}.'.format(v1, v2, v1))
        else:
            print('\n>>> O maior valor entre {} e {} é {}.'.format(v1, v2, v2))
        opção = 0
    elif opção == 4:
        v1 = int(input('\nDigite um valor: '))
        v2 = int(input('Digite outro valor: '))
        opção = 0
    else:
        print('\n>>> Opção inválida. Tente novamente!')
        opção = 0

print('\n>>> Programa encerrado!')
