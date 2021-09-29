from time import sleep
import colorama
colorama.init()

valor1 = int(input('[1] Coloque um valor: '))
valor2 = int(input('[2] Coloque um valor: '))
sair = 0

while sair != 5:
    print('-'*20, 'MENU', '-'*20)
    print('''[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair do programa
''')

    option = int(input('Selecione algumas das opções: '))

    if option > 5 or option < 1:
        print('\033[32mOpção inválida\033[m')
    
    elif option == 1:
        soma = valor1 + valor2
        print(f'\n--> A soma de {valor1} + {valor2} é igual a {soma}')
        sleep(3)

    elif option == 2:
        multipli = valor1*valor2
        print(f'\n--> A soma de {valor1} x {valor2} é igual a {multipli}')
        sleep(3)

    elif option == 3:
        if valor1 > valor2:
            print(f'\n--> Dos números [{valor1}, {valor2}] o maior número é {valor1}')
            sleep(3)

        elif valor1 == valor2:
            print(f'\n--> Ambos dos valores tem números iguais')
            sleep(3)
            
        else:
            print(f'\n--> Dos números [{valor1}, {valor2}] o maior número é {valor2}')
            sleep(3)

    elif option == 4:
        quais = int(input('Quais dos valores você quer trocar? [1/2]'))

        if quais == 1:
            valor1 = int(input('Qual novo valor? '))
            print(f'Valor setado {valor1}')
            sleep(3)
        else:
            valor2 = int(input('Qual novo valor? '))
            print(f'Valor setado {valor2}')
            sleep(3)

    else:
        print('Saindo do programa...')
        sair = 5
        sleep(3)
print('Programa finalizado')