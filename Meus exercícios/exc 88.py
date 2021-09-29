from random import randint
from time import sleep

sorteios = list()
palpites = list()

print('-'*40,'\n', ' '*10, 'JOGO DA MEGA SENA\n','-'*40 )
quant = int(input('Quantos jogos você quer que eu sorteie? '))

print('=-=-=-=-= Sorteando Jogos =-=-=-=-=')
for count in range(0, quant):
    for x in range(0, 6):
        palpites.append(randint(1, 60))

    sorteios.append(palpites[:])
    palpites.clear()

    print(f'Jogo {count+1}: {sorteios[count]}')
    sleep(1)
print('=-=-=-=-=-=<BOA SORTE!!!>=-=-=-=-=-=')


