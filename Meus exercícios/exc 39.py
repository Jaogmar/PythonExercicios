from time import localtime, strftime
import colorama
colorama.init()

anoatual = int(strftime("%Y"))#ano em que o programa foi inicializado

print('='*100)
ano = int(input('Em que ano você nasceu? '))#data de nascimento do usuário
print(' ')

if len(str(ano)) != len(str(anoatual)):
    print(f'Por favor coloque um ano legível com {len(str(anoatual))} números')#erro de ano maior do que a quantidade de anos passados
    print('='*100)

else:
    if (anoatual-ano) > 18:
        print(f'\033[31mEi já se passou { (anoatual-ano)-18} anos para você se alistar no exército\033[m')#Passou do ano do alistament0
        print('='*100)
        
    elif (anoatual-ano) < 18:
        print(f'\033[1;32mFalta {18-(anoatual-ano)} anos para você se alistar no exército\033[m')#Falta de anos par ao alistamento
        print('='*100)

    else:
        print('\033[1;31mEi, é este ano em que você tem que se alistar no exército!\033[m')#Ano de alistamento
        print('='*100)