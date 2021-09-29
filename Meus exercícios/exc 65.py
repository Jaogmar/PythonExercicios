c = 0
res = 'S'
num = 0
media = 0

while res == 'S':
    num1 = int(input('-->Coloque algum número: '))
    num = num + num1

    res = str(input('-->Você quer continuar colocando números? [S/N]')).strip().upper()

    if c == 0:
        maior = num1
        menor = num1
    
    elif num1 > maior:
        maior = num1
    
    else:
        menor = num1
    
    c = c + 1
media = num/c
print(f'\n-->Você colocou {c} números e a soma entre esses valores é {num}')
print(f'-->Maior número: {maior} -->Menor número: {menor}')
print(f'-->Média: {media}')
