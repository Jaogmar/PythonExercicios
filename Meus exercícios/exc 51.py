razao = int(input('Coloque a razão dessa PA: '))
n = int(input('Coloque o primeiro valor dessa PA: '))
r = 0 + n

print('Valor dessa P.A -->', end=' ')
print(f'[{n}]', end='-')
for c in range (0, 9):
    r = r + razao
    print(f'[{r}]', end='-')
print('\n')