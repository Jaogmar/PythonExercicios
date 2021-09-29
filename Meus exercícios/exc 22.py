frase = str(input("Coloque uma frase, porfavor: "))
letras = (len(frase))
quantidade = str(input("Que letra que você quer que procure? "))
print(f"O número total da frase, contando espaços é de: {letras} da frase {frase} e tem {len(quantidade)} {quantidade}'s ")

#=========================
#Ou daria para fazer assim
#=========================



frase1 = str(input('Coloque seu nome, por favor:')).strip()

c1 = len(frase1) - frase1.count(' ')

print(f'A quantidade de letras do seu nome é: {c1}')
print(f'Em maísculo é: {frase1.upper()}')
print(f'Em minúsculo é: {frase1.lower()}')
print(f'Caso seu nome fosse um título ele seria assim: {frase1.title()}')
