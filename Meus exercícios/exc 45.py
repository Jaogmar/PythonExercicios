import colorama
from colorama.ansi import set_title
from termcolor import colored
from time import sleep
import random
colorama.init()

print('\033[33mVamos jogar jokenpô?\033[m (\033[32msim\033[m/\033[31mnão\033[m)')
r = str(input('--> ')).strip().lower()

if r == 'sim' or r == 's':
    x = ('tesoura', 'papel', 'pedra') #COMPUTADOR
    x = random.choice(x)
    x = str(x)
    

    print('\033[33mEscolha \033[m(\033[35mpapel\033[m/\033[34mtesoura\033[m/\033[36mpedra\033[m)')
    y = str(input('--> ')).strip().lower()#PESSOA
    
    sleep(1)
    print('Jo\n')
    sleep(1)
    print('  Ken')
    sleep(1)
    print('\n  PO')

    if x == y:
        print(colored('\nVocê empatou com o computador', 'magenta'))
    
    elif y == 'papel' and x == 'pedra':
        print(colored('Parabéns meu caro, VOCÊ VENCEU!!!', 'green'))
    
    elif y == 'pedra' and x == 'tesoura':
        print(colored('Parabéns meu caro, VOCÊ VENCEU!!!', 'green'))    

    elif y == 'tesoura' and x == 'papel':
        print(colored('Parabéns meu caro, VOCÊ VENCEU!!!', 'green'))
    
    else:
        print(colored('Então meu caro, você perdeu ;-;', 'red'))

    print(f'\nO computador fez a seguinte escolha \033[32m{x}\033[m e você escolheu \033[33m{y}\033[m')
        
else:
    print(colored('Ah ok, fica para um proxima ;-;', 'blue'))

print('=-'*50)

