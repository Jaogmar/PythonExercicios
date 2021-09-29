'''maior = 0
menor = 0

for p in range('1, 6'):
    peso = floar(input(f'Peso da {p}ª pessoas: '))

    if p == 1:
        maior = p
        menor = p
    
    else:
        if peso > maior:'''

v = 0
maior = 0
menor = 0
pos1 = 0
pos2 = 0

for p in range(1, 6):
    peso = float(input(f'[{p}]Informe seu peso: '))

    if p == 1:
        maior = peso
        menor = peso
        
    else:
        if peso > maior:
            pos1 = p
            maior = peso
        
        else:
            if peso < menor:
                pos2 = p
                menor = peso

print(f'O maior⬆️ peso é o {pos1}º = {maior}Kg')
print(f'O menor⬇️ peso é o {pos2}º = {menor}Kg')