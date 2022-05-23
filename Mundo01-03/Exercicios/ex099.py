def maior(* num):
    from time import sleep as sl
    print(f'{30*"-="}\nAnalisando os valores passados...')
    cont = maior = 0
    for v in num:
        print(v, end=' ')
        sl(.2)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
