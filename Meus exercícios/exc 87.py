lista = [[], [], []]
count = 0

#Pegando os valores
for x1 in range(0,3):
    num1 = int(input(f'(0,{x1}): '))
    lista[0].append(num1)

for x2 in range(0,3):
    num2 = int(input(f'(1,{x2}): '))
    lista[1].append(num2)

for x3 in range(0,3):
    num3 = int(input(f'(2,{x3}): '))
    lista[2].append(num3)

#Print da lista
for num in lista:
    print(f'({num[0]}) ({num[1]}) ({num[2]})')


somapar = soma3 = 0
pares = list()
for count in range(0, len(lista)):
    for x in lista[count]:
        if x%2 == 0:
            pares.append(x)
            somapar = somapar + x 

    if count == 1:
        maior = lista[1][0] 
        for x in lista[1]:
            if x > maior:
                maior = x

    elif count == 2:
        for x in lista[2]:
            soma3 = x + soma3
    
    

print(f'''Números pares: {pares}
Somas de todos os pares: {somapar}
\nSoma da 3º coluna: {soma3}
Maior número da 2º coluna: {maior}''')