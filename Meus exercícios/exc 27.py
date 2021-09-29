from time import sleep

nome = str(input('Fale seu nome: ')).strip()

n1 = nome.title()
n2 = n1.split()

print(f'Então, seu primeiro nome com o último é: {n2[0]} {n2[-1]}')
