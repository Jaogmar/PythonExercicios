from time import sleep
import colorama
colorama.init()

v = 1
maior = 1
menor = 0
novo_num = 0

print('-'*20, 'Sequência de Fibônacci', '-'*20)
count = int(input('--> Quantos valores dessa sequência você quer? '))
sleep(1)
print('\033[31mCalculando...\033[m ')
sleep(1)

while v < count:

    if v < 2:
        print(f'[\033[32m0\033[m]->[\033[32m1\033[m]', end='->')

    else:
        novo_num = menor + maior
        menor = maior 
        maior = novo_num
        print(f'[\033[32m{novo_num}\033[m]', end='->')

    v = v + 1 

print('...')
print('=-'*20)