from time import sleep

while True:
    count = 0
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('='*20)
    if num >= 0:
        while count < 11:
            print(f'{num} x {count} = {count*num}')
            count = count + 1
        print('='*20)
    else:
        print('Finalizando programa...')
        break
sleep(1)
print('Sistema de tabuada FECHADO, volte sempre!')
        