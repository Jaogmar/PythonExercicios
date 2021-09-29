quant = maior = menor = count = 0
pesado = list()
leve = list()
info = list()
pessoas = list()
while True:

    info.append(str(input('Nome: ')))
    info.append(float(input('Peso: ')))
    pessoas.append(info[:])

    if count == 0:
        maior = info[1]
        menor = info[1]
    
    elif info[1] > maior:
        maior = info[1]
    
    elif info[1] < menor:
        menor = info[1]

    resp = str(input('Você quer adicionar mais uma pessoa? [S/N]'))
    if resp in 'Nn':
        print('Fechando o programa... \n')
        break

    else:    
        while resp not in 'Ss':
            resp = str(input('Você quer adicionar mais uma pessoa? [S/N]'))

    count = count + 1
    info.clear()

for p in pessoas:
    print(p[0])
    if p[1] == maior:
        pesado.append(p[0])

    elif p[1] == menor:
        leve.append(p[0])
             
print(f'As pessoas mais leves: {leve}')
print(f'As pessoas mais pesadas: {pesado}')


