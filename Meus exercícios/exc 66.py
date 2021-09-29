c = result = 0
print('-->Caso deseje parar coloque 999')

while True:
    num = int(input('-->Coloque um número inteiro: '))

    if num != 999:
        result = num + result
        c = c + 1

    else:
        break

print(f'Você colocou {c} números, que somando dão {result}')