m = float(input('São quantos metros? '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('A medida de {}m corresponde a:\n{:.3f}km\n{:.2f}hm\n{:.1f}dam\n{}dm\n{}cm\n{:.0f}mm'.format(m, km, hm, dam, int(dm), int(cm), mm))