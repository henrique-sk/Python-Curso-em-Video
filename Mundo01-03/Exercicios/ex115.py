from time import sleep as sl


def cor(num=0):
    cod = ('\33[m',     # 0 - sem cores
           '\33[32m',   # 1 - verde
           '\33[31m',   # 2 - vermelho
           '\33[34m',   # 3 - azul
           '\33[33m'    # 4 - amarelo
           )
    return cod[num]


def linha(qtd=42):
    return print('-'*qtd)


def cabecalho(tit='teste', tam=42):
    linha(tam)
    print(f'{tit:^42}')
    linha(tam)


def cadastrar(nome, idade):
    txt = open('ex115.txt', 'a')
    txt.writelines(f'{nome:<30}\t{idade:<3}anos\n')
    txt.close()
    print(f'Novo registro de {nome} adicionado.', end='')
    sl(2)


def listar():
    txt = open('ex115.txt', 'r')
    print(txt.read())
    txt.close()


while True:
    cabecalho('MENU PRINCIPAL')
    print(f'{cor(4)}1{cor()} - {cor(3)}Ver pessoas cadastradas{cor()}'
          f'{cor(4)}\n2{cor()} - {cor(3)}Cadastrar nova pessoa{cor()}'
          f'{cor(4)}\n3{cor()} - {cor(3)}Sair do Sistema{cor()}')
    linha()
    resp = int(input(f'{cor(1)}Sua Opção: {cor()}'))
    if 1 <= resp <= 3:
        if resp == 1:
            cabecalho('PESSOAS CADASTRADAS')
            listar()
            sl(2)
        if resp == 2:
            cabecalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            while True:
                try:
                    idade = int(input('Idade: '))
                except (ValueError, TypeError):
                    print(f'{cor(2)}ERRO: por favor, digite um número inteiro válido.{cor()}')
                else:
                    break
            cadastrar(nome, idade)
            print()
        if resp == 3:
            cabecalho('Saindo do sistema... Até logo!')
            break
    else:
        print(f'{cor(2)}ERRO! Digite uma opção válida!{cor()}')
    sl(2)
