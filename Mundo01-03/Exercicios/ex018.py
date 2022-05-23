from math import sin, cos, tan, radians

ang = float(input('Digite um ângulo: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('Um ângulo de {:.2f}°, possui seno {:.2f}, cosseno {:.2f} e tangente {:.2f}.'.format(ang, seno, coss, tang))