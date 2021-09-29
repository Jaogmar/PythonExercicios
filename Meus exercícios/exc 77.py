from typing import Collection


import colorama
colorama.init()

palavrastupla = ('caramba', 'socorro', 'nossa', 'parabens', 'programaçao')

for palavra in palavrastupla:
    cortada = list(palavra)

    print(f'Vogais da palavra \033[32m{palavra.capitalize()}\033[m', ' '* (13 - len(cortada)), '-->', '(', end=' ')

    for count in range(0, len(cortada)):


        if cortada[count] == "a" or cortada[count] == "A":
            print('a', end=' ')
        
        elif cortada[count] == 'e' or cortada[count] == "E":
            print('e', end=' ')
        
        elif cortada[count] == 'i' or cortada[count] == "I":
            print('i', end=' ')

        elif cortada[count] == 'o' or cortada[count] == "O":
            print('o', end=' ') 

        elif cortada[count] == 'u' or cortada[count] == "U":
            print('u', end=' ')  

    print(')')

print('OUTRO SISTEMA')

for p in palavrastupla:
    print(f'\nNa palavra {p} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')