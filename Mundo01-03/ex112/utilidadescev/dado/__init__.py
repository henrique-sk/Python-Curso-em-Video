def leiaDinheiro(resp=''):
    while True:
        teste = str(input(resp)).replace(',', '.').strip()
        if teste.isalpha() or teste == '':
            print(f'\33[0;31mERRO: \"{teste}\" é um preço inválido!\33[m')
        else:
            return float(teste)
