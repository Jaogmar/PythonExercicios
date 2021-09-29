num = int(input('Coloque um número: '))
count = num
result = 1

while count > 0:

    print(f'{count}', end='')

    if count > 1:
        print(' x ', end ='')
    else:
        print(f' =', end = ' ')
        
    result = count * result
    count = count - 1
    

print(f'{result}')