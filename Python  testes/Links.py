import random
import colorama
colorama.init()

d1 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
d2 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
d3 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
d4 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
d5 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
d6 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

print('-='*50)
qdd = int(input('Você quer um código de 5 ou 6 dígitos? ')) #Quantidade de dígitos

if qdd == 5:
    print(f'\033[32mLink da print gerada:\033[m prnt.sc/' + d1 + d2 + d3 + d4 + d5)
else:
    print(f'\033[32mLink da print gerada:\033[m prnt.sc/' + d1 + d2 + d3 + d4 + d5 + d6)

print('-='*50)