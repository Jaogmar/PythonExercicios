from random import randint

def sorteia(começo, fim):
    numeros = []
    for x in range(0, 5):
        numeros.append(randint(começo, fim))

    return(numeros)

def somaPar(num):
    soma = 0
    pares = []

    for x in num:
        if x%2 == 0:
            soma = soma + x
            pares.append(x)
    print(f'Os números colocados foram: {num}\nOs números pares são: {pares} e a soma delesé {soma}')

x1 = int(input('Coloque o limite do Sorteio:\nComeço: '))
x2 = int(input('Fim: '))

somaPar(sorteia(x1, x2))
