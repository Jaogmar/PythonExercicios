from time import sleep

vkm = int(input('Distância percorrida: '))
cvkm = vkm

sleep(2)
print('Calculando...')
sleep(1)

if vkm <= 200:
    print('{}\nEntão, por sua viagem ser de curta distância será cobrado R$0,50 por Km rodado, então:\n{}\nViagem: {}Km\nPreço: R${:.2f}'.format( (30 * "="), (30 * "="), vkm, vkm*0.50))

else:
    print('Então sua viagem por ser de maior Kilometragêm, será cobrado R$O,45 por Km rodado, então:\n{}\nViagem: {}Km\n{}\nPreço: R${:.2f}'.format((30 * "="), vkm, (30 * "="), vkm*0.45))