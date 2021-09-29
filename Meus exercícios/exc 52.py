import colorama
colorama.init()
from time import sleep

n = int(input('Coloque um número --> '))
vezes = 0
q = 0
for c in range(1, n+1):
    q = q + 1
    if n%q >= 1:
        print(f'\033[31m{c}\033[m', end=' ')
    
    else: 
        print(f'\033[32m{c}\033[m', end=' ')
        vezes = vezes + 1 
        

if vezes > 2:
    print(f'\nEste número pode ser dividido por {vezes} números da tabela')
    print(f'Ou seja, o número {n} \033[31mnão\033[m é um número primo')
    
else:
    print(f'\nUau... {n} \033[32mé\033[m um número primo 🎉🎉🎉') 