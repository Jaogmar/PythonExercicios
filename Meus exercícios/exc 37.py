from time import sleep
import colorama
colorama.init()

quest = input('Você quer qual dos dois programas? responda com [1/2] ')

if quest == '1':

    print('='*100)
    num = int(input('Coloque um número: ---> '))
    num1 = int(input(f'Este número "{num}" você quer transformar este número em\n1-Binário\n2-Octal\n3-Hexadecimal\nQual dessas opções? '))
    print('='*100)

    if num1 == 1:
        print('Seu número escolhido é em binário é \033[32;40m{0:08b}\033[m'.format(num))
        print('='*100)

    elif num1 == 2:
        print('Seu número escolhido é em binário é \033[32;40m{0:08o}\033[m'.format(num))
        print('='*100)

    else:
        print('Seu número escolhido é em binário é \033[32;40m{0:020e}\033[m'.format(num))
        print('='*100)

else:
    print('='*100)
    num = int(input('Coloque um número: ---> '))
    num1 = int(input(f'Este número "{num}" você quer transformar este número em\n1-Binário\n2-Octal\n3-Hexadecimal\nQual dessas opções? '))
    print('='*100)

    if num == int:

        if num1 == 1:
            num2 = '{0:08b}'.format(num)

        elif num1 == 2:
            num2 = '{0:08o}'.format(num)

        elif num1 == 3:
            num2 = '{0:08e}'.format(num)
        
        else:
            print('\033[33mOpção inválida\033[m')
    
        print(f'O número que você escolheu, convertido é \033[32;40m{num2}\033[m')
        
    else:
        print('Só aceitamos núemros inteiros')
    
print('='*100)