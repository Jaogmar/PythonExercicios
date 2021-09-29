from time import sleep
import colorama
colorama.init()

print('-='*50)

print(' '*40,"Caixa Eletrônico \n")

preço = str(input(('Preço --> '))).strip().replace(',', '.')

sleep(1)

#Formas de pagamento
print('='*20)
print('Formas de pagamento: \n \033[32m 1 - À vista\033[m \n \033[31m 2 - Parcelado\033[m')

x = str(input('Qual o a forma de pagamento? ')).strip()
x = int(x)

if x == 1: #A VISTA
    #Formas de pagamento à vista
    print(' ')
    print('\033[32m 1 - Dinheiro/Cheque\033[m \n \033[31m2 - Cartão\033[m')
    x1 = str(input('Selecione uma dessas formas --> ')).strip()
    x1 = int(x1)

    if x1 == 1:
        resultado = (float(preço)/100)*90 #à vista no DINHEIRO / CHEQUE 
        print(f'Você terá um desconto de 10% avista, ou seja você terá que pagar {resultado}')

    else:
        resultado = (float(preço)/100)*95 #à vista no CARTÃO
        print(f'Você terá um desconto de 5% avista no cartão, ou seja você terá que pagar {resultado}')


else: #PARCELADO
    print(' ')
    vezes = str(input('Em quantas vezes você deseja parcelar? ')).strip()
    vezes = int(vezes)

    if vezes <= 2:
        resultado = float(preço)/2
        
        print(f'Você terá que pagar \033[33mpor mês {resultado}$ durante 2 meses\033[m') #PARCELADO 2 meses

    else:
        preço = float(preço)
        resultado = ((preço/100)*120)/vezes
        
        print(f'Você terá que pagar \033[33mpor mês {resultado}$ durante {vezes} meses\033[m') #PARCELADO mais do que 2 meses

print('-='*50, '\n', ' '*40, 'FIM')