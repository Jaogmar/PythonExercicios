from time import sleep, strftime
import colorama
colorama.init()

print('#'*100)
print('\033[1mColoque suas informações para podermos classificar você nas competição de natação\033[m')

anoatual = int(strftime("%Y"))
idad1 = int(input('-Data de nascimento: --> '))
idad = (anoatual - idad1)
print(f'A idade do participante é ')

print(' ')

if len(str(anoatual)) != len(str(idad1)):
    print('\033[1;31mNúmeros invalidos!\033[m')

else:
    if idad <= 9:
        print('Você irá fazer parte do grupo \033[1;32m"MIRIM"\033[m')
    
    elif idad<= 14:
        print('Você irá fazer parte do grupo \033[1;33m"INFANTIL"\033[m')
    
    elif idad <= 19:
        print('Você irá participar do grupo \033[1;34m"JUNIOR"\033[m')
    
    elif idad == 20:
        print('Você irá participar do grupo \033[1;35m"SÊNIOR"\033[m')
    
    else:
        print('Você participa do grupo \033[1;36m"MASTER"\033[m')

print('#'*100)


