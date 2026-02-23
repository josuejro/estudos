listagem = ('Computador', 3299.90, 'Refrigerante', 12.99, 'Chocolate', 7.90, 'Caderno', 32.99)

print('-' * 40)
print(f"{'Listagem de Preços':^40}")
print('-' * 40)

for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}', end='')
    else:
        print(f'R$ {listagem[c]:>7.2f}')

print('-' * 40)