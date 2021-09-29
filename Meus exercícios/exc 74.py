from random import randint
import colorama
colorama.init()

print('='*20, 'Números aleátorios com TUPLAS', '='*20)
c = randint(0, 100),
for count in range(1 ,5):
    b = randint(0, 100),
    c = c + b
count = 0

alinhados = sorted(c)

print(f'''Os números máximo e mínimo dessa lista são
Mínimo:\033[32m {alinhados[0]}\033[m 
Máximo:\033[31m {alinhados[len(alinhados)-1]}\033[m''')

print('[', end='')
for count in range(0, 5):
    if count == 0:
        print(f'\033[32m{alinhados[0]}\033[m', end=', ')
    
    elif count == 4:
        print(f'\033[31m{alinhados[4]}\033[m]')
    
    else:
        print(f'{alinhados[count]}', end=', ')

