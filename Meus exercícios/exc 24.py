nome = str(input('Caso você não saiba ler eu posso te dizer se essa palavra começa ou não com "Santo": '))
n1 = nome.strip()
nome1 = n1.split()
nupper = nome1[0].upper()
l1 = 'SANTO' in nupper 
print(f'Então a sua palavra {l1} Santo')

#=========================
#Ou daria para fazer assim
#=========================

nome1 = str(input('Qual cidade você nasceu? ')).strip()
nome2 = nome1.lower()

tem = 'santo' in nome2 

print(f'Nossa que ligal a cidade que eu nasci {tem} Santo')

#=========================
#Ou daria para fazer assim
#=========================

cid = str(input('Qual a linda cidade que você nasceu? \n'))
print(cid[:5].upper == 'SANTO')