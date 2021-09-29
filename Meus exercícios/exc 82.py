valores = list()
impares = list()
pares = list()

for count in range(0, 5):
    valores.append(int(input(f'[{count+1}] Coloque um número: ')))

    if valores[count]%2 == 0:
        pares.append(valores[count])
        print('par')

    elif valores[count]%3 > 0:
        impares.append(valores[count])
        print('impar')

print(f'''Resultado:
Valores: {sorted(valores)}
Pares: {sorted(pares)}
Impares: {sorted(impares)}''')