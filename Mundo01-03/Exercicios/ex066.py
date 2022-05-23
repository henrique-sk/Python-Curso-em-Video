soma = qtd = 0
while True:
    valor = int(input('Digite um  valor (999 para parar): '))
    if valor == 999:
        break
    soma += valor
    qtd += 1
print(f'A soma dos {qtd} valores foi {soma}!')
