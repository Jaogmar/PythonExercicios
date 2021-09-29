from time import sleep
import colorama
colorama.init()

valor1 = int(input('-->Primeiro valor dessa P.A: '))
raz = int(input('-->Razão dessa P.A: '))
result = valor1
c = 0
limite = 10

print(f'-->Calculando P.A de razão {raz}...')
sleep(1)

print('-'*20)

while c <= limite:

    print('[', end= '')
    while c <= limite:
        if c < limite:
            print(f'\033[33m{result}\033[m', end='-')
            result = result + raz
            

        else:
            print('...', end='')
        c = c + 1    
    
    print(']')

    c = 0

    limite = int(input('\n-->Você quer mais quantos termos? '))

    if limite == 0:
        c = limite + 2
        

print('FIM')