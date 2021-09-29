from time import sleep

while True:

 numero1 = str(input('Coloque um número de 0 á 9999: '))
 num = numero1.strip()
 numero = int(numero1)

 if len(num) > 4:
     print('Por favor coloque um número entre as capacidades máximas')
     sleep(3)
 else:
     print(f'Unidade: {numero // 1 % 10}')
     print(f'Dezena: {numero // 10 % 100}')
     print(f'Centena: {numero // 100 % 1000}')
     print(f'Milhar: {numero // 1000 % 10000}')
