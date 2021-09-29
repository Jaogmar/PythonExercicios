import colorama
colorama.init()

media = 0   #Variável da média
maior = 0   #Variável da homem de maior idade
count = 0   #Variável da quantidade de mulher -20
nome1 = 0   #Variável para salvar o nome do homem mais velho

for c in range(1,5):
    print('-'*20, f'\033[3{c}m[{c}] Pessoa\033[m', '-'*20)
    nome = str(input('-Nome: ')).strip().capitalize()
    sexo = str(input('-Sexo: ')).strip().lower()
    idade = int(input('-Idade: '))

    media = media + idade

    if c == 1:
        maior = idade

    elif sexo == 'homem' or sexo == 'masculino' or sexo == 'h':
        if idade > maior:
            maior = idade
            nome1 = nome
    
    elif sexo == 'mulher' or sexo == 'm' or sexo == 'feminino':
        if idade < 20:
            count = count + 1
    
    else:
        print('Erro: informação inválida')

print('-='*25)

media = media/4

print(f'-A média dessas idade é {media}\n')
print(f'-O homem mais velho dessa lista é {maior} e seu nome é {nome1}\n')
print(f'-{count} mulheres tem menos de 20 anos nessa lista\n')

