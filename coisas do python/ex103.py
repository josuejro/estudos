def ficha(nome_atleta='<desconhecido>', gols=0):
    print(f'O jogador {nome_atleta} fez {gols} gol(s) no campeonato.')

n = str(input('Digite o nome do jogador: '))
g = str(input(f'Digite a quantidade de gols do jogador {n}: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols = g)
else:
    ficha(n, g)