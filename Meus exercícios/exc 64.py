num = 0
result = 0
c = 0

print('=-'*20)
print('Caso você queira parar coloque 999')

while num != 999:

    num = int(input('Coloque algum número inteiro: '))

    if num != 999:
        result = result + num

    c = c + 1 #contagem

print(f'Você colocou {c-1} números, onde a soma entre eles é {result}')
print('=-'*20)