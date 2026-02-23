from itertools import count

num = (int(input('Primeiro número: ')), int(input('Segundo número: ')),
       int(input('Terceiro número: ')), int(input('Quarto número: ')))

print(f'O número 9 apareceu {num.count(9)} vezes.')

if 3 in num:
    print(f'O número 3 foi achado na {num.index(3) + 1}º posição.')

print('Os valores pares digitados foram: ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
    