pares = 0

valores = int(input('-->Coloque um número: ')),
for count in range(0,3):
    valor = int(input('-->Coloque um número: ')),
    valores = valores + valor
count = 0

print(f'Nessa lista de números, apareceu {valores.count(9)} número que eram igual a 9')
if 3 in valores:
    print(f'O primeiro valor com o número 3 esta na posição: {valores.index(1)+1}º da lista')

print('Os números pares são os seguintes (', end='')
for n in valores:
    if n%2 == 0:
        print(f'{n}', end=', ')
print(')')