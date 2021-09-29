import colorama
colorama.init()

print('Impares dividos por três')
for c in range(1, 502, 2):
    c = int(c)

    if (c % 3) == 0:
        
        print(f'[\033[32m{c}\033[m]', end='-')
print(' ')
    
