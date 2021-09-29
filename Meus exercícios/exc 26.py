from time import sleep

frase = str(input('Escreva alguma coisa: '))
frase1 = frase.upper()
frase2 = frase1.split()
frase3 = ''.join(frase2)

letra = str(input('Que letra ou palavra você quer que eu encontre? ')).strip()
letra1 = letra.upper()
quantidade = frase3.count(letra1)


if (letra1 in frase3) == True:
    print('Ah ok, aparentemente o sistemas encontrou a letra que você desejou aqui\n ')
    sleep(2)
    print(f'Eu encontrei onde sua letra(s) ou palavra(s) começa e onde por ultimo ela aparece \né o seguinte:\n \n-Ela tem na posição: {frase3.find(letra1)}')
    print(f'-E vista por último em: {frase3.find(letra1, quantidade)}')
else:
    print(f'Esta frase não tem "{letra.upper()}"')