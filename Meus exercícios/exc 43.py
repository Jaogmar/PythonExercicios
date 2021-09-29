import colorama
colorama.init()

print("="*100 , '\nEste é um aplicativo que calcula o IMC\n')
kg = str(input('Coloque o seu peso ---> ')).strip().replace(',', '.')
m = str(input('Colque o seu tamanho em metros ---> ')).strip().replace(',', '.')
print(' ')

c = float(kg)/(float(m)**2)
c = ('{:.1f}'.format(c))
c = float(c)

if c <= 18.5:
    r = '\033[32mAbaixo do peso\033[m'
    
elif c <= 25:
    r = '\033[32mPeso ideal\033[m'

elif c <= 30:
    r = '\033[33mSobrepeso\033[m'

elif c <= 40:
    r = '\033[31mObesidade\033[m'

else:
    r = '\033[31mObesidade mórbida\033[m'

print(f'Então você é classificado como: "{r}" \n', "=-"*50)
