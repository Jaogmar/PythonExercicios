nome = str(input('Fale seu nome por favor: '))
nome1 = nome.upper()
nome2 = 'SILVA' in nome1

if nome2 == True:
    print(f'Então seu nome é "{nome}" e aparentemente tem "Silva"')
else:
    print(f'Então seu nome é "{nome}" e aparentemente não tem "Silva"')