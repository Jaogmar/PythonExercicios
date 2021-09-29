num = list()

for c in range(0,5):
    num.append(int(input('-->Coloque um valor: ')))

cresnum = sorted(num)

print(f'''Da lista:
{num}
Menor número: {cresnum[0]}
Maior número: {cresnum[4]}''')