from time import sleep
def maior(*val):
    print('='*50, '\nAnalisando os valores passados...')
    sleep(0.5)

    if len(val) > 0:
        maior = val[0]
        for x in val:
            print(f'{x}', end=' ')
            if x > maior:
                maior = x
        print(f'O maior valor é ({maior})')
    
    print(f'Foram informados {len(val)} valores')

maior(0,5,6,8,2,8,2,3,15,7)
maior()