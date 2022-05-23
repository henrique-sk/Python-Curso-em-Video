valor = float(input('''Vamos verificar a possibilidade de financiamento
Informe o valor da casa: R$'''))
salario = float(input('Informe o salário: R$'))
anos = int(input('Em quantos anos pretende pagar? '))
mensalidade = valor / (anos * 12)
limite = salario * .3
print('O valor mensal da prestação será de R${:.2f}.'.format(mensalidade))
print('Seu salário é de R${:.2f} e a parcela não pode execer 30% desse ' \
      'valor, ou seja, R${:.2f}.'.format(salario, limite))
if mensalidade <= limite:
    print('Parabéns!!! Seu empréstimo foi aprovado!!!')
else:
    print('Empréstimo negado! Tente parcelar em mais vezes.')
