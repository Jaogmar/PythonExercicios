import random
from time import sleep

Quer = str(input('Então você quer participar? [sim/não] ')).strip().upper()

while Quer == 'SIM':

    
    numero = int(input('Chute um número de 0 à 5, eu duvido que você vai acertar '))#Jogador tenta adivinhar
    sorte = (random.randint(0,5))#Número aleatório

    sleep(2)
    print('PROCESSANDO...')
    sleep(2)
    if numero == sorte:
        print('Caramba você é um cara muito sortudo, parabéns ')

    else:
        print('É meu parça, eu falei que você não ia acertar, mas tente de novo vai que de certo ')

        sleep(2)

print('AAAAA que pena')
        
 
