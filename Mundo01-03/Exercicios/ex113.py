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


def leiaFloat(resp):
    while True:
        try:
            n = float(input(resp))
        except (ValueError, TypeError):
            print('\33[31mERRO: por favor, digite um número real válido.\33[m')
            continue
        except KeyboardInterrupt:
            print('\n\33[31mUsuário preferiu não digitar esse número.\33[m')
            return 0
        else:
            return n


ni = leiaInt('Digite um número Inteiro: ')
nf = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {ni} e o real foi {nf}.')
