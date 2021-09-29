print('Caso queira parar, digite "Stop"')

lista = list()

while True:
    num = input('Coloque um valor: ').lower()

    if num.isalpha() == True:
        if 'stop' in num:
            print('finalizando programa')
            break
    
    elif num.isnumeric() == True:
        if num not in lista:
            lista.append(num)
        
print(sorted(lista))