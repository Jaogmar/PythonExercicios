num = str(input('Coloque 3 números entre espaços: ')).split(' ')

num1 = int(num[0])
num2 = int(num[1])
num3 = int(num[2])

#Num1 é o maior?
if num1 > num2 and num1 > num3:

    print('=' * 40)
    print(f'O número {num1} é o maior')
    
    if num1 > num2 and num2 < num3:
        print(f'O número {num3} é o médio\nO número {num2} é o menor')
    
    if num1 > num3 and num3 < num2:
        print(f'O número {num2} é o médio\nO número {num3} é o menor')
    print('=' * 40)

#Num2 é o maior?
if num1 < num2 and num3 < num2:

    print('=' * 40)
    print(f'O número {num2} é o maior')

    if num2 > num1 and num1 < num3:
        print(f'O número {num3} é o médio\nO número {num1} é o menor')
    
    if num1 > num3 and num3 < num2:
        print(f'O número {num1} é o médio\nO número {num3} é o menor')
    print('=' * 40)
    

#Num3 é o maior? 
if num3 > num2 and num3 > num1:
    
    print('=' * 40)
    print(f'O número {num3} é o maior')

    if num2 > num1 and num1 < num3:
        print(f'O número {num2} é o médio\nO número {num1} é o menor')
    
    if num1 > num2 and num2 < num1:
        print(f'O número {num1} é o médio\nO número {num2} é o menor')
    print('=' * 40)
