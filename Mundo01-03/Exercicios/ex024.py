city = input('Qual o nome da sua cidade? ').strip()
print('Sua cidade começa com o nome "SANTO"? ', 'SANTO' in city[:5].upper())
# OU
print('Sua cidade começa com o nome "SANTO"? ', city[:5].upper() == 'SANTO')