import colorama
colorama.init()
from random import randint
from time import sleep

numr = int(randint(0, 10))
resposta = 0
tent = 0

print('--> O computador esta \033[31mpensando\033[m num número de \033[31m0 à 10\033[m')
sleep(3)
print('--> Tente acertar o número na menor quantidade de tentativas')
sleep(1)
print('-'*30, 'GO','-'*30)

while resposta != numr:
    tent = tent + 1
    resposta = int(input(f'[{tent}º] Tentativa --> '))

sleep(1)
print(f'--> PARABÉNS... Você acertou o número em {tent} tentativas 🎉🎉🎉🎉')