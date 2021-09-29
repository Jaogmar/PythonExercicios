from termcolor import colored
import colorama
from time import sleep
colorama.init()

print(colored('-=-'*10 +'BANCO'+'-=-'*10, 'yellow'))
print('\nAntes de fazer a compra preciso de algumas informações:\n')

salario = str(input('-Salário: ')).strip().split('.')
valor = str(input('-Valor do produto: ')).strip().split('.')
parcela = int(input('-Por quantos anos você quer parcelar este produto? '))

salario1 = int(''.join(salario))
valor1 = int(''.join(valor))

salario2 = ( 30 / 100 ) * salario1 
cal = valor1/(parcela*12)


if float(cal) > float(salario2):
    print(f'\n{("="*60)}')
    print('\033[4;0;41mEmpréstimo negado, valor muito acima do seu salário mensal\033[m')
    print("="*60)
    
else:
    print(f'\n{("="*68)}')
    print(f'\033[1;37;42m{(" "*28)}Valor aceito{(" "*28)}\033[m')
        
    sleep(1)
    print('\n\033[4m Aguarde alguns segundos até a transação ser efetivada\033[m', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.')
    sleep(1)
    print('\n Você pagará \033[32mR${:.2f}\033[m durante \033[33m{} meses\033[m '.format(cal, 12*parcela))
    print(f'{("="*68)}')


