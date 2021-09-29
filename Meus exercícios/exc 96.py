print('\n-->Calculador de terrenos\n', '='*40 )

def area(c,l):
    x = c * l
    print(f'A área de um terreno {c} x {l} é de {x}m2')

c = float(input('Comprimento do terreno: '))
l = float(input('Largura do terreno: '))

area(c,l)
