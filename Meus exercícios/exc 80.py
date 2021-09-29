lista_valores = list()
maior = menor = count = 0

while count <= 5:

    valor = int(input('Coloque um valor: '))

    if count == 0:
        lista_valores.append(valor)
    
    else:
        while True:
            for pos in range(0, len(lista_valores)):
                if valor > lista_valores[pos]:
                    
                    lista_valores.insert(pos+1, valor )
                    break

                elif valor < lista_valores[pos]:
                
                    lista_valores.insert(pos, valor )
                    break

            break
    
    count = count + 1 

print(lista_valores, '\n')
print('PROGRAMA FECHOU')




# for count in range(1, 6):
#     valor = int(input(f'[{count}] Coloque um valor: '))

#     if count <= 2:
#         lista_valores.append(valor)
    
#     elif count > 1:
#         for num in lista_valores:
#             if valor > lista_valores[num]:
#                 lista_valores.insert(valor, count)
            

# print(lista_valores)
        