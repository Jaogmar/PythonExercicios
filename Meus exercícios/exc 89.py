dados = list()
alunos = list()

print('-='*30)
print(' '*27, 'EVN')
print('-='*30)

num = 1
while True:
    print(f'----> {num}º Aluno:')
    dados.append(str(input('Nome: ')).capitalize())
    dados.append(float(input('Nota P1: ')))
    dados.append(float(input('Nota P2: ')))
    dados.append((dados[1] + dados[2])/2)

    alunos.append(dados[:])
    dados.clear()

    # CONFIRMAÇÃO DE RESPOSTA
    resp = str(input('Deseja continuar? [S/N] '))
    while resp not in 'Ss':
        if resp in 'Nn':
            break

        resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break

    num = num + 1

print('-'*30)
print('N°   NOME           MÉDIA')
print('-'*30)

num = 0
for x in alunos:
    print(f'{num}   {x[0]}{" " * (16 - len(x[0]))}{x[3]}', flush=True)
    num = num + 1

while True: 
    print('=-'*30)
    inter = int(input('Mostras notas de qual aluno? (999 interrompe): '))

    if inter != 999:
        if inter > len(alunos)-1:
            print('Número fora do alcance da lista, lista ', flush=True)
        print(f'Notas de {alunos[inter][0]} são [{alunos[inter][1]}, {alunos[inter][2]}]') 
    
    else:
        print('Programa finalizado, volte sempre!!!')
        break
    