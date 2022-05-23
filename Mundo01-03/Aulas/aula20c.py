def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 5, 1, 0, 5]
print(valores)
dobra(valores)
print(valores)


# EMPACOTAMENTO
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores}, temos {s}.')


soma(5, 2)
soma(5, 2, 4, 9)
