print('=' * 100)
print('Coloque três valores inteiros, para podermos ver se essas medidas formam um triângulo: ')
md = str(input('Mas coloque neste formato, entre espaços:\n[menor] [médio] [maior] = ')).replace(' ', '')

if len(md) > 3 or len(md) < 3:
    print('=' * 20)
    print('Só é aceito 3 números')
    print('=' * 20)

else:

    print('=' * 40)

    md.split()

    md1 = int(md[0])
    md2 = int(md[1])
    md3 = int(md[2])

    #Número md1 caso for o maior
    if md1 > md2 and md1 > md3:
        soma1 = md2 + md3
        if soma1 > md1:
            print(f'Estes números, {md1} {md2} {md3} tem a capacidade de formar um Triãngulo')
            print('=' * 100)

        else:
            print(f'Estes números, {md1} {md2} {md3} não tem a capacidade de formar um Triângulo')
            print('=' * 100)
    
    #Número md2 caso for o maior
    if md2 > md1 and md2 > md3:
        soma2 = md2 + md3
        if soma2 > md2:
            print(f'Estes números, {md1} {md2} {md3} tem a capacidade de formar um Triângulo')
            print('=' * 100)

        else:
            print(f'Estes números, {md1} {md2} {md3} não tem a capacidade de formar um Triângulo')
            print('=' * 100)
    
    #Número md3 caso for o maior
    if md3 > md1 and md3 > md2:
        soma3 = md2 + md1
        if soma3 > md3:
            print(f'Estes números, {md1} {md2} {md3} tem a capacidade de formar um Triãngulo')
            print('=' * 100)

        else:
            print(f'Estes números, {md1} {md2} {md3} não tem a capacidade de formar um Triângulo')
            print('=' * 100)
    
    #Números iguais
    '''if md1 == md2 or md1 == md3:
        soma4 = md2 + md3
        if soma4 > md1:
            print(f'Estes números, {md1} {md2} {md3} tem a capacidade de formar um Triãngulo')
            print('=' * 100)

        else:
            print(f'Estes números, {md1} {md2} {md3} não tem a capacidade de formar um Triângulo')
            print('=' * 100)
    
    if md2 == md1 or md2 == md3:
        soma5 = md1 + md3
        if soma5 > md2:
            print(f'Estes números, {md1} {md2} {md3} tem a capacidade de formar um Triãngulo')
            print('=' * 100)

        else:
            print(f'Estes números, {md1} {md2} {md3} não tem a capacidade de formar um Triângulo')
            print('=' * 100)'''

    '''if md3 == md1 or md3 == md2:
        soma5 = md1 + md2
        if soma5 > md3:
            print(f'Estes números, {md1} {md2} {md3} tem a capacidade de formar um Triãngulo')
            print('=' * 100)

        else:
            print(f'Estes números, {md1} {md2} {md3} não tem a capacidade de formar um Triângulo')
            print('=' * 100)'''
        



