from time import sleep

sleep(2)

sal = float(input('Olha que legal!\nSua empresa ganhou um lucro muito grande, então mostre seu salário real para podermos adicionar uma certa quantia no seu salário\n-Salário = '))

sleep(1)
print('=' * 40)
print('Calculando')
sleep(2)
print('Pronto:')
sleep(2)

if sal <= 1250:
    print('=' * 100)
    print(f'Então segundo meus cálculos você ganhou um aumento de 15% no seu salário, então você receberá {(sal * (15/100)) + sal}')
    print('=' * 100)

else:
    print('=' * 100)
    print(f'Então segundo meu cálculos você ganhou um aumento de 10% no seu salário, então você receberá {(sal * (10/100)) + sal}')
    print('=' * 100)
