import colorama
colorama.init()

print('-=-'*30)
num1 = int(input('Coloque um número: '))
num2 = int(input('Coloque o segundo núemro: '))


if num1 > num2:
    print(f'\nO número \033[32m{num1} é o maior\033[m, e o número \033[31m{num2} é o menor\033[m')#número 1 maior


elif num2 > num1:
    print(f'\nOs número \033[32m{num2} é o maior\033[m, e o número \033[31m{num1} é o menor\033[m')#número 2 maior


elif num2 == num1:
    print('\nOs dois números que você colocou eles são \033[33miguais\033[m')#Os número são iguais


print('-=-'*30)