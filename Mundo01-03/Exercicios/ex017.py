from math import hypot

cop = float(input('Quanto mede o cateto oposto? '))
cad = float(input('Quanto mede o cateto adjacente? '))
print('A hipotenusa é {:.2f}.'.format(hypot(cop, cad)))

# from math import sqrt
#
# cop = float(input('Quanto mede o cateto oposto? '))
# cad = float(input('Quanto mede o cateto adjacente? '))
# hip = sqrt(cop ** 2 + cad ** 2)
# print('A hipotenusa é {:.2f}.'.format(hip))


# cop = float(input('Quanto mede o cateto oposto? '))
# cad = float(input('Quanto mede o cateto adjacente? '))
# hip = (cop ** 2 + cad ** 2) ** (1/2)
# print('A hipotenusa é {:.2f}.'.format(hip))