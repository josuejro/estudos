n = int(input('Digite um número: '))

cont = 0

for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
        print('\033[32m', end=' ')
    else:
        print('\033[m', end=' ')
    
    print(f'{c}', end=' ')

print(f'\n\n\033[mO número {n} foi dividido {cont} vezes...')

if cont == 2:
    print(f'\033[m... portanto, {n} É um número primo!')
else:
    print(f'\033[m... portanto, {n} NÃO é um número primo.')