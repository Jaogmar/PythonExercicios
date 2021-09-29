import colorama
colorama.init()

word1 = str(input('Coloque uma palavra --> ')).strip().lower()
word = list(word1)
q = int(len(word))

num = 0
compativeis = 0

'''print(word)
print(q)
print('-----')'''

for c in range(q-1, -1,-1):

    if word[num] == word[c]:
        print(f'\033[32m{word[num]}\033[m', end=' ')
        compativeis = compativeis + 1
    
    else:
        print(f'\033[31m{word[num]}\033[m', end=' ')

    num = num + 1

if compativeis != q:
    
    print('Essa palavra não é um \033[32mpalíndromo\033[m')

else:
    print(f'{word1} É um Palíndromo')

