time = []

while True:
    jogador = {}
    partidas = []

    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))

    for c in range(0, total):
        gols = int(input(f'Quantos gols foram feitas na {c+1}º partida? '))
        partidas.append(gols)

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja cadastrar outro jogador? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

    print()
    print(f'O jogador {jogador['nome']} jogou {total} partidas.')
    print('-' * 40)
    for i, v in enumerate(jogador['gols']):
        print(f'{jogador['nome']} fez {v} gols na {i+1}º partida.')

    print()
    print(f'Foram feitos um total de {jogador['total']} gols.')
    print('-' * 40)

print('-' * 40)
print(f'{'COD':<4}{'NOME':<15}{'GOLS':<20}{'TOTAL':<5}')

for k, v in enumerate(time):
    print(f'{k:>2}{v['nome']:<15}{str(v['gols']):<20}{v['total']:<5}')

print('-' * 40)

while True:
    busca = int(input('Qual jogador deseja consultar os dados? (999 encerra o programa): '))
    
    if busca == 999:
        break

    if busca >= len(time) or busca < 0:
        print(f'Não existe jogador no banco de dados com o código {busca}. Tente novamente.')
    else:
        levantamento = time[busca]
        print(f'Informações do jogador {levantamento['nome']}: ')

        for i, g in enumerate(levantamento['gols']):
            print()
            print(f'No {i+1}º jogo foram feitos {g} gols.')
print('-' * 40)
