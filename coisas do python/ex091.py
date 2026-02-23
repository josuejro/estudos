from random import randint
from operator import itemgetter
from time import sleep

jogo = {}
ranking = {}

print('-' * 30)
print('   JOGADORES JOGANDO O DADO   ')
print('-' * 30)

for j in range(1,5):
    print(f'Jogador{j} jogando o dado...', end=' ')
    sleep(1)  
    jogo[f'jogador{j}'] = randint(1, 6)
    print(f'Tirou {jogo[f"jogador{j}"]}!')
    sleep(0.5)  

print('-' * 30)

print('\nOrganizando resultados...')
sleep(2)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, (nome, valor) in enumerate(ranking):
    if i == 0:
        print(f'\n🥇 CAMPEÃO: {nome} com {valor}! 🎉')
        sleep(1)
    else:
        print(f'{i+1}º lugar: {nome} com {valor}')
        sleep(0.5)

print('-' * 30)