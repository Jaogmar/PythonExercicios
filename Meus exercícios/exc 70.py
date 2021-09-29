quantidade_maiores_1000 = 0
menor = 0
total = 0
count = 0

print('=-'*20)

while True:
    nome_produto = str(input('-->Nome do produto: '))
    preço = int(input('-->Preço: '))

    if count == 0:
        menor = preço
    
    elif preço < menor:
        menor = preço
    
    elif preço > 1000:
        quantidade_maiores_1000 = nome_produto

    total = total + preço
    count = count + 1 
    print('='*40)

    opçao = str(input('Você quer adicionar mais algum produto? [S/N]')).strip()
    while opçao not in 'SsNn':
        opçao = str(input('Você quer adicionar mais algum produto? [S/N]')).strip()
    
    if opçao in 'Nn':
        break


print('=-'*20)
print(f'''Valor total da compra: {total}
Produto valendo mais de 1000$: {quantidade_maiores_1000}
O produto mais barato: {menor}''')