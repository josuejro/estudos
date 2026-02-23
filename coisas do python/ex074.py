from random import randint

n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10),)

print(f'Os números sorteados foram: ', end='')
print(*n, sep=', ')
print(f'\nO maior número presente na tupla é {max(n)}')
print(f'O menor número presente na tupla é {min(n)}')