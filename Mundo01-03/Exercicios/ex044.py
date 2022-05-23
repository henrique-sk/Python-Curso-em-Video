print('{:=^40}'.format(' LOJAS TOKTIK '))
v = float(input('Informe o valor do produto: R$ '))
c = int(input('''Escolha a forma de pagamento:
1 - dinheiro/pix
2 - à vsita no cartão
3 - 2x no cartão
4 - 3x ou mais no cartão
Informe a condição escolhida: '''))
if c == 1:
    print('Em dinheiro ou pix tem 10% de desconto, de R${:.2f}, o produto sai por R${:.2f}.'.format(v, v * .9))
elif c == 2:
    print('Á vista no cartão tem 5% de desconto, de R${:.2f}, o produto sai por R${:.2f}.'.format(v, v * .95))
elif c == 3:
    print('Em até 2x no cartão o preço é o mesmo, sai por R${:.2f}.'.format(v))
elif c == 4:
    print('Em 3x ou mais no cartão, tem 20% de juros, de R${:.2f}, o produto sai por R${:.2f}.'.format(v, v * 1.2))
else:
    print('Não foi informada uma condição válida.')
print('Obrigado! Volte sempre!')
