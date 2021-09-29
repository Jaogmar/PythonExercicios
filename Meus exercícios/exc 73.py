times = 'palmeiras', 'cruzeiro', 'grêmio', 'santos', 'corinthians', 'flamengo', 'atlético mineiro', 'athletico paranaense', 'internacional','chapecoense', 'botafogo', 'são paulo', 'fluminense', 'vasco da gama' , 'bahia'	, 'sport'	, 'vitória'	, 'ponte preta', 'américa'	, 'coritiba'

print('='*20, 'Primeiros colocados', '='*20)

for count in range(0, 5):
	print(f'{count+1}º lugar: {times[count].capitalize()}')
count = 0

print('='*20, '4 Últimos colocados', '='*20)
for count in range(len(times)-4, len(times)):
	print(f'{count+1}º lugar: {times[count].capitalize()}')
count = 0

organizados = sorted(times)

print('='*20, 'Lista em ordem alfabética', '='*20)
for count in range(0, len(organizados)):
	print(f'{organizados[count].capitalize()}')

print(f"-->Chpecoense está na {times.index('chapecoense')+1}º posição")

########################################################################
#                          OUTRO PROGRAMINHA                           #
########################################################################
print(f'Os 5 primeiros {times[0:5]}')
print(f'Os 4 últimos {times[-4:]}')
