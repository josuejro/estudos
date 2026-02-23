from random import sample
from time import sleep

lista_jogos = []

quant = int(input('Quantos jogos você deseja jogar? '))

for _ in range(quant):
    jogo = sample(range(1,60),6)
    jogo.sort()

    lista_jogos.append(jogo)

print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)

for indice, jogo in enumerate(lista_jogos):
    print(f'Jogo {indice+1}: {jogo}')
    sleep(1)

print('-=' * 3, '< BOA SORTE! >', '-=' * 3)