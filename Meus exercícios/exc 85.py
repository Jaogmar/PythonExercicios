lista = [[],[]]
count = 1

while True:
    num = int(input(f'[{count}]Coloque algum número: '))

    if num%2 == 0:
        lista[0].append(num)
    
    else:
        lista[1].append(num)
    
    resp = str(input('Você quer adicionar mais números? [S/N]'))
    if resp in 'Nn':
        print('Fechando o programa... \n')
        break

    else:    
        while resp not in 'Ss':
            resp = str(input('Você quer adicionar mais números? [S/N]'))
    
    count = count + 1

print(f'Os núemeros pares são: {sorted(lista[0])}')
print(f'Os números ímpares são: {sorted(lista[1])}')