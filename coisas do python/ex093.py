jogador = {}
partidas = []

jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))

for c in range(0, total):
    gols = int(input(f'Quantos gols foram feitas na {c+1}º partida? '))
    partidas.append(gols)

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print()
print(f'O jogador {jogador['nome']} jogou {total} partidas.')
print('-' * 40)
for i, v in enumerate(jogador['gols']):
    print(f'{jogador['nome']} fez {v} gols na {i+1}º partida.')

print()
print(f'Foram feitos um total de {jogador['total']} gols.')
print('-' * 40)
