soma = 0
count = 0
for c in range(0, 6):
    n = int(input('Coloque um número inteiro: ')) 
    count = count + 1
    if (c%2) == 0:
        soma = soma + n

print(f'Você informou {count} números, e a soma desses pares são {soma}')