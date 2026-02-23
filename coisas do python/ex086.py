matriz = [[], [], []]

for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input('Digite um valor: '))
        matriz[linha].append(num)

print('-' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
