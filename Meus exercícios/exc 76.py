produtos = 'chocolate', 'manteiga', 'arroz', 'feijão', 'abóbora', 'macarrão', 'chimarrão'
preços = 5.50, 4.20, 10.00, 8.90, 5.45, 3.90, 15.50

print('-'*20, 'Compras', '-'*20)
for count in range(0, (len(produtos))):
    pontos = len(produtos[count])
    print(f'{produtos[count].capitalize()}', '.'*(30-pontos), end=' ')
    print(f' R$ {float(preços[count])}')
