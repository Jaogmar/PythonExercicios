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
salario1 = int(salario1)
valor1 = int(''.join(valor))
valor1 = int(valor1)

presta = valor1 / (parcela * 12) #resulta no valor a ser pago por mês
salario2 = salario1 * (30/100) #30% do salario


print(f'30% do salário {salario2} e valor de prestação por mêses {presta}')