matriz = [[], [], []]
soma_pares = 0
soma_coluna = 0
maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input('Digite um valor: '))
        matriz[linha].append(num)
        if num % 2 == 0:
            soma_pares += num

print('-' * 40)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print('-' * 40)
print(f'A soma de todos os números pares digitados é: {soma_pares}')
print()
for linha in range(0, 3): soma_coluna += matriz[linha][2]
print(f'A soma de todos os números da terceira coluna é: {soma_coluna}')
print()
maior = max(matriz[1])
print(f'O maior valor da segunda linha é: {maior}')
print('-' * 40)
