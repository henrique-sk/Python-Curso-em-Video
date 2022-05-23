peso = float(input('Informe seu peso(Kg): '))
altura = float(input('Informe sua altura(m): '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print('Seu IMC é {:.1f}. Você está abaixo do peso.'.format(imc))
elif imc <= 25:
    print('Seu IMC é {:.1f}. Você está no peso ideal.'.format(imc))
elif imc <= 30:
    print('Seu IMC é {:.1f}. Você está com sobrepeso.'.format(imc))
elif imc <= 40:
    print('Seu IMC é {:.1f}. Você está com obesidade.'.format(imc))
elif imc < 40:
    print('Seu IMC é {:.1f}. Você está com obesidade mórbida.'.format(imc))
