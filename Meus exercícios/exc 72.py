import colorama
colorama.init()

numeros = ('zero', 'um','dois', 'três', 'quatro', 'cinco', 'seis',
 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 
 'quinze', 'dezeseis', 'dezesete', 'dezenove', 'vinte')

num = int(input('Coloque um número entre [0 à 20]\n--> '))

while num < 0 or num > 20:
    num = int(input('Coloque um número entre [0 à 20]\n--> '))

print(f'O número que você escolheu foi \033[32m{num}\033[m ou \033[32m{numeros[num-1].capitalize()}\033[m')