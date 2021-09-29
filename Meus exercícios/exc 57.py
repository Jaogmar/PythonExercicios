import colorama
colorama.init()

sexo = str('')
q = 0

while q != True:
    sexo = str(input('Qual o seu sexo? [m/f] ')).strip().lower()

    if sexo == 'm' or sexo == 'f':
        q = True
    else:
        q = False

    print(sexo)
print('\033[32mOk, resposta registrada\033[m')