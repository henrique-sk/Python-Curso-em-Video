def cor(num=0):
    cod = ('\33[m',     # 0 - sem cores
           '\33[32m',   # 1 - verde
           '\33[31m',   # 2 - vermelho
           '\33[34m',   # 3 - azul
           '\33[33m'    # 4 - amarelo
           )
    return cod[num]


def leiaInt(resp):
    while True:
        try:
            n = int(input(resp))
        except (ValueError, TypeError):
            print('\33[31mERRO: por favor, digite um número inteiro válido.\33[m')
            continue
        except KeyboardInterrupt:
            print('\n\33[31mUsuário preferiu não digitar esse número.\33[m')
            return 0
        else:
            return n


def linha(qtd=42):
    return print('-'*qtd)


def cabecalho(tit='teste', tam=42):
    linha()
    print(tit.center(42))
    linha()


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{cor(4)}{c}{cor(0)} - {cor(3)}{item}{cor(0)}')
        c += 1
    linha()
    opc = leiaInt(f'{cor(1)}Sua Opção: {cor()}')
    return opc
