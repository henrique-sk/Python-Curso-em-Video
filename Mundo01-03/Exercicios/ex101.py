def voto(ano):
    from datetime import date as dt
    idade = dt.today().year - ano
    if 18 > idade >= 16 or idade > 65:
        status = 'VOTO OPCIONAL'
    elif idade >= 18:
        status = 'VOTO OBRIGATÓRIO'
    else:
        status = 'NÃO VOTA'
    print(f'Com {idade} anos: {status}.')


print(30*'-')
voto(int(input('Em que ano você nasceu? ')))
