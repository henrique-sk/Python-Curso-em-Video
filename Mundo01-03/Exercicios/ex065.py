resposta = 'S'
soma = quantidade = maior = menor = 0
while resposta == 'S':
    num = int(input('Digite um número inteiro: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    elif num < menor:
        menor = num
    elif num > maior:
        maior = num
    resposta = input('Quer digitar outro número?'
                     '[S/N]: ').upper().strip().replace(' ', '')
print('Você digitou {} números e a média entre eles é {:.2f}.'
      '\nO maior valor digitado foi {} e o menor foi {}.'
      .format(quantidade, soma/quantidade, maior, menor))
