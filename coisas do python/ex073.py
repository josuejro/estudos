times = ('Sesc Flamengo', 'Minas', 'Osasco', 'Sesi Bauru', 
         'Praia Clube', 'Maringá', 'Fluminense',
         'Brasília', 'Barueri', 'Mackenzie', 'Tijuca', 'Sorocaba')

print('-' * 120)
print('Os cinco primeiros colocados da Superliga 25/26 até o momento são: ')
print(f'{", " .join(times[:5])}')
print('-' * 120)
print('Já os últimos quatro colocados são:')
print(f'{", ".join(times[-4:])}')
print('-' * 120)
print('Os times em ordem alfabética: ')
print(f'{", ".join(sorted(times))}')
print('-' * 120)
print(f'O Praia CLube está atualmente na {times.index('Praia Clube') + 1}º posição na tabela.')
print('-' * 120)
