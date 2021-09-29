valores = list()

for count in range(1, 6):
    valores.append(int(input(f'[{count}] Colque um número: ')))

valores.sort(reverse=True)
print(f'Nessa lista temos {len(valores)} números')
print(f'Esses valores de forma decrescente, fica assim: {valores}')

if 5 in valores:
    print('O valor 5 está na lista')

else:
    print(f'O valor 5 está na posição {valores.index(5)}')