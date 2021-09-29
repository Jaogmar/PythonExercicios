velo = int(input('Coloque a velocidade do carro em km, em inteiros: ----> '))

if velo > 80:
    print('\nO carro passou dos limites de velocidade de 80Km/h\n ')
    print(f'Ele passou {((velo)-80)*1}km acima da velocidade, então ele receberá uma multa de 7 reais a cada Km/hora acima')
    print(f'\nOu seja a pessoa terá que pagar R${((velo - 80))*7}reais')
    print('=' * 100)
    
else:
    print('=' * 100)
    print('\033[1;32mEsta ok, o seu carro não passou do limite de velocidade\033[m')
    print('=' * 100)

print('\033[1;32mEsta ok, o seu carro não passou do limite de velocidade\033[m')
