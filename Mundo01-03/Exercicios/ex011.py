l = float(input('Qual a largura da parede que você quer pintar? '))
h = float(input('E qual a altura? '))
a = l * h
t = a / 2
print('Sua parede tem {:.2f}m².\nPara pintá-la, vai precisar de {:.2f} litros de tinta.'.format(a, t))