frase = 'Curso em Vídeo Python'
frase2 = '     Curso em Vídeo Python      '
print('frase[3] =>', frase[3])
print('frase[3:13] =>', frase[3:13])
print('frase[:13] =>', frase[:13])
print('frase[13:] =>', frase[13:])
print('frase[1:15:2] =>', frase[1:15:2])
print('frase[::2] =>', frase[::2])
print('frase.count("o") =>', frase.count('o')) # como tudo em python é um objeto, pode usar o "." alguma coisa
print('frase.upper().count("O") =>', frase.upper().count('O'))
print('len(frase) =>', len(frase))
print('(len(frase2)) =>', len(frase2))
print('(len(frase2.strip())) =>', len(frase2.strip()))
print('frase.replace("Python", "Android") =>', frase.replace('Python', 'Android'))
frase = frase.replace('Python', 'Android')
print('***atribuição*** frase =>', frase)
frase = frase.replace('Android', 'Python')
print('***reatribuição*** frase =>', frase)
print('"Curso" in frase =>', 'Curso' in frase)
print('frase.find("Curso") =>', frase.find('Curso'))
print('frase.find("vídeo") =>', frase.find('vídeo')) # -1 qdo não existe
print('frase.lower().find("vídeo") =>', frase.lower().find('vídeo'))
print('frase.split() =>', frase.split())
dividido = frase.split()
print('dividido[3] =>', dividido[3])
print('dividido[3][1] =>', dividido[3][1]) # mostrar índice 1 do índice 3

print('''Caso você queira escrever um texto muito longo
e que ocupe várias linhas, você pode.  Basta]
utilizar aspas triplas no início e final da
sentença.''')
