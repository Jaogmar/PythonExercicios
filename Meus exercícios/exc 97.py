def alin(msg):
    tam = len(msg)
    print('~'*(tam+2))
    print(f'  {msg}')
    print('~'*(tam+2))

txt = input('Escreve sua mensagem: ').capitalize()
alin(txt)