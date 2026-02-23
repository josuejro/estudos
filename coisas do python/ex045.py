from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('''Suas opções:
[1] - Pedra
[2] - Papel
[3] - Tesoura''')

jogador = int(input('Qual a sua jogada? ')) - 1

print('JO')
sleep(1) 
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 11)
print(f'O computador escolheu: {itens[computador]}')
print(f'Você escolheu: {itens[jogador]}')
print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA')
