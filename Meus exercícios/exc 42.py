import colorama
colorama.init()

#Colocar três números
print('~'*100)
nume = str(input('Coloque três números divididos entre espaços para definirmos se é possível formar um triângulo --> ')).strip().replace(' ', '').replace('',' ')
num = nume.split(' ')
print(' ')
if (len(nume.replace(' ',''))) != 3:
    print('\033[1;31mSó aceitamos 3 valores\033[m')

else:
    x = int(num[1])
    y = int(num[2])
    z = int(num[3])


#Descobrir os 2 menores números 
    if x > y and x > z: #X é o maior núemero
        maior = x
        if y > z:
            medio = y
            menor = z
    
        else:
            medio = z
            menor = y

    elif y > x and y > z: #Y é o maior número 
        maior = y
        if x > z:
            medio = x
            menor = z
        else:
            medio = z
            menor = x

    else:                 #Z é o maior número 
        maior = z
        if x > y:
            medio = x
            menor = y
    
        else:
            medio = y
            menor = x

#falar se ele da para formar um triangulo
    if (medio + menor) > maior:
        if x == y == z:
            car = 'Equilátero'

        elif y == x or y == z or x == z:
            car = 'Isóceles'

        else:
            car = 'Escaleno'
    
        print(f'Com esses números \033[1;32m"{x} {y} {z}"\033[m é possível fazer um triangulo cuja as característica é de um \033[1;32m{car}\033[m')

    else:
        print('\033[1;31mÉ impossível fazer um triãngulo com esses valores\033[m')

print('~'*100)

print('Outro programa')

r1 = int(input('Valor núemro 1: '))
r2 = int(input('Valor núemro 2: '))
r3 = int(input('Valor núemro 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

    if r1 == r2 and r2 == r3:
        print('Este triângulo é Equilátero')

    elif r1 != r2 and r2 != r3:
        print('Este triângulo é Escaleno')

    else:
        print('Este triângulo é Isóceles')
    
else:
    print('É impossível fazer um triângulo com esses valores')