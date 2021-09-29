from typing import List


exp = str(input('Coloque a sua expressão: '))
exp = list(exp)  
parenteses = list()

for letra in exp:
    if letra == '(':
        parenteses.append(letra)

    elif letra == ')':
        parenteses.append(letra)

abrindo = 0
for letras in parenteses:

    if letras == '(':
        abrindo = abrindo + 1

    elif len(letras) == 0:
        if letras == ')':
            abrindo = abrindo + 1
    
    elif letras == ')':
        abrindo = abrindo - 1

if abrindo == 0:
    print('Expressão correta')

print('Expressão incorreta')
