idades = 0
idade = 0
velho = 0
nova = 0
novas = 0
for i in range(1, 5):
    nome = input('Informe o {}° nome: '.format(i))
    idade = int(input('Idade: '))
    sexo = input('Sexo [m/f]: ')
    idades += idade
    if i == 1 and sexo in 'Mm':
        velho = idade
        ele = nome
    if velho < idade and sexo in 'Mm':
        velho = idade
        ele = nome
    if idade < 20 and sexo in 'Ff':
        nova = idade
        novas += 1
print('A média de idades é {:.1f}.'.format(float(idades / 4)))
print('O homem mais velho é o {} e ele tem {} anos.'.format(ele, velho))
print('São {} mulheres com menos de 20 anos.'.format(novas))
