numeros = [[], []]

for c in range(1, 8):
    num = int(input(f'Digite o {c}º número: '))

    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()

print()
print(f'Dos números que você digitou, os números pares são: {numeros[0]}...')
print()
print(f'...já os números ímpares do que você digitou são: {numeros[1]}')
print()