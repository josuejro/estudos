soma = 0
cont = 0

for c in range (1,7):
    n = int(input('Digite um número qualquer: '))
    if n % 2 == 0:
        soma += n
        cont += 1

print(f'\nForam informados {cont} números pares e a soma deles é: {soma}')
