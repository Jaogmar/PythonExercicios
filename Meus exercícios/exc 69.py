from time import sleep

count18 = 0
homens = 0
mulheres = 0

while True:
    idade = int(input('-->Idade: '))#Input de idade
    if idade > 18:#maiores de 18
        count18 = count18 + 1

    while True: #input de valor correto apenas para F e M
        sexo = str(input('-->Qual o seu sexo [M/F]: ')).strip().upper()

        if sexo == 'M':
            homens = homens + 1 #contagem de homens
            break

        elif sexo == 'F':
            if idade < 20:
                mulheres = mulheres + 1 #mulheres mais de 20
            break

        else:
            print('Apenas é validado [F/M]')
    
    opicao = str(input('Você quer continuar: [S/N]')).strip().upper()
    if opicao == 'N':
        break

    print('=-'*20)
    
print('='*40)
print(f'''-->Pessoas que são +18: {count18}
-->Homens cadastrados: {homens}
-->Mulheres de -20 anos: {mulheres}''')
