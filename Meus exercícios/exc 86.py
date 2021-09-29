# (0, 0), (0, 1), (0, 2)
lista = [[], [], []]

for x1 in range(0,3):
    num1 = int(input(f'(0,{x1}): '))
    lista[0].append(num1)

for x2 in range(0,3):
    num2 = int(input(f'(1,{x2}): '))
    lista[1].append(num2)

for x3 in range(0,3):
    num3 = int(input(f'(2,{x3}): '))
    lista[2].append(num3)

print('-='*50)
for num in lista:
    print(f'({num[0]}) ({num[1]}) ({num[2]})')
