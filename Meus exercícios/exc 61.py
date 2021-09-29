from time import sleep
import colorama
colorama.init()

valor1 = int(input('-->Primeiro valor dessa P.A: '))
raz = int(input('-->Razão dessa P.A: '))
result = valor1
c = 0

print(f'-->Calculando P.A de razão {raz}...')
sleep(1)

print('-'*20)

print('[', end= '')
while c < 11:
    
    if c < 10:
        print(f'{result}', end='-')
    
    else:
        print('...', end='')
        
    result = result + raz
    c = c + 1

print(']')
