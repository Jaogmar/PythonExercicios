import colorama
colorama.init()
from time import sleep
from random import randint, choice

print('-'*20,'PAR ou ÍMPAR', '-'*20)
sleep(1)
print('-->Prepa-se')
sleep(3)

ponto = 0

while True:
    print('-->O computador está a pensar num número de 0 a 10')
    sleep(3)
    pc = randint(0, 10)
    
    while True:
        numj = int(input('-->Coloque um número de [0 a 10] '))
        if numj < 0 or numj > 10:
            print('\033[31mO valor tem que ser entre 0 e 10\033[m')

        else:
            escolha = choice(['par', 'impar'])
            if escolha == 'par':
                pessoa = 'par'
            else:
                pessoa = 'impar'
            print(f'O sistema escolheu que você vai ficar com \033[32m{pessoa.upper()}\033[m')

            break  

    soma = pc + numj

    print('\033[31mCalculando...\033[m')
    sleep(1)

    if pessoa == 'par':
        if int(soma%2) == 0:
            print('Parabéns!!! você ganhou esta rodada :white_check_mark:')
            ponto = ponto + 1

        else:
            break
    
    else:
        if pessoa == 'impar':
            if soma%2 != 0:
                print('\033[32mParabéns!!!\033[m você ganhou esta rodada :white_check_mark:')
            
                ponto = ponto + 1

            else:
                break

    print(f'-->O sistema escolheu o número \033[33m{pc}\033[m')    
    sleep(3)
    print('-='*20)

print('-='*20)
print(f'O sistema escolheu o número \033[33m{pc}\033[m')   
print(f'==>Uau, você teve um vitória de {ponto} partidas consecutivas')