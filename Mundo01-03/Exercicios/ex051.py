primeiro = int(input('Digite o primeiro termo de uma PA: '))
razão = int(input('Digite a razão dessa PA: '))
décimo = (primeiro + (10 - 1) * razão) + razão
print('Os 10 primeiros termos dessa PA são:')
for c in range(primeiro, décimo, razão):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
