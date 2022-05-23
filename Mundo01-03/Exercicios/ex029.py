vel = float(input('A quantos km/h está  o veículo? '))
frase = 'O limite de velocidade é 80km/h.'
if vel > 80:
    multa = (vel - 80) * 7
    print(frase, '\nVocê ultrapassou o limite e foi multado em R${:.2f}!'.format(multa))
print('Tenha um bom dia!')


