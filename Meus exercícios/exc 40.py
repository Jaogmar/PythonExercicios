from typing import Collection


import colorama
colorama.init()

print('=-'*50)
print('\033[1;37mColoque suas notas para podermos fazer a sua média escolar:\033[m\n ')

n1 = float(input('1º nota = '))
n2 = float(input('2º nota = '))

if n1 > 10:
    print('\033[1;31mEi a sua 1º nota ultrapassa o máximo 10\033[m')

elif n2 > 10:
    print('\033[1;31mEi a sua 2º nota ultrapassa o máximo 10\033[m')
    
else:
    media = (n1 + n2)/2
    media = float('{:.1f}'.format(media))

    if media < 5.0:
        print('Sinto lhe informar mas você foi \033[1;31mREPROVADO\033[m, sua média não bate acima de 5.0\n')
        print('Cálculos:\n',
        f'{n1} + {n2} = {n1+n2}\n',
        f'{n1+n2}/{2} = {media}'
        )

    elif  media > 5.0 and media < 6.9:
        print('Você está em \033[1;33mRECUPERAÇÃO\033[m\n')
        print('Cálculos:\n',
        f'{n1} + {n2} = {n1+n2}\n',
        f'{n1+n2}/{2} = {media}'
        )
    
    else:
        print(f'Parabéns, você \033[1;32mAPROVADO\033[m com uma média {media}\n')
        print('Cálculos:\n',
        f'{n1} + {n2} = {n1+n2}\n',
        f'{n1+n2}/{2} = {media}'
        )

print('-='*50)