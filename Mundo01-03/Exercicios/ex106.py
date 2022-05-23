c = ('\033[m',      # 0 - sem cores
     '\033[30;42m', # 1 - verde
     '\033[30;41m', # 2 - vermelho
     '\033[30;46m'  # 3 - azul
     )


def manual(funcao):
    titulo(f'Acessando o manual do comando \'{funcao}\'', 2)
    print(c[3], end='')
    help(funcao)
    print(c[0], end='')

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print(f'{tam * "~"}'
          f'\n  {msg}  '
          f'\n{tam * "~"}')
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        manual(comando)
titulo('ATÉ LOGO!', 1)
