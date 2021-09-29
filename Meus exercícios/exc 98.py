from time import sleep

def contador(inicio, fim, passo):
    print('-='*20)
    print(f'Contagem de {inicio} até {fim} em {passo}')

    if fim > inicio:
        for count in range(inicio, fim+1, passo):
            print(f'{count}', end=' ', flush= True)
            sleep(0.2)        
    else:
        for count in range(inicio, fim-1, -passo):
            print(f'{count}', end=' ', flush= True)
            sleep(0.2)
    print('Fim!')

contador(1, 10, 1)
contador(10, 0, 2)

print('=-'*20, '\nAgora é a sua vez de personalizar o contador:')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
