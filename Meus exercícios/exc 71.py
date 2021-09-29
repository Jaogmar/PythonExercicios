ced1 = ced2 = ced3 = ced4 = ced5 = 0

valor = int(input('Informe o valor: '))

while True:
    
    if valor >= 50:
        valor = valor - 50
        ced1 = ced1 + 1
        
    
    elif valor >= 20:
        valor = valor - 20
        ced2 = ced2 + 1
    
    elif valor >= 10:
        valor = valor - 10
        ced3 = ced3 + 1
    
    elif valor >= 5:
        valor = valor - 5
        ced4 = ced4 + 1
    
    elif valor >= 1:
        valor = valor - 1
        ced5 = ced5 + 1
    
    else:
        break

print(valor)

print(f'-->Você receberá {ced1} notas de 50$')
print(f'-->Você receberá {ced2} notas de 20$')
print(f'-->Você receberá {ced3} notas de 10$')
print(f'-->Você receberá {ced4} notas de 5$')
print(f'-->Você receberá {ced5} notas de 1$')

#Ou daria para ter feito o programa assim

