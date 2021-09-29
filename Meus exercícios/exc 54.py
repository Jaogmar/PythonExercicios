from time import strftime

time = int(strftime("%Y"))
pes = 0

for c in range(1,8):
    res = int(input(f'{c}º pessoas: Ano em que você nasceu -->'))

    anos = time - res
    if anos >= 18:
        pes = pes + 1

print(f'Dessa lista, apenas \033[32m{pes}\033[m pessoas são maiores de idade 🍸')