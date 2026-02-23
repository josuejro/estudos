valores = []

for cont in range(0, 5):
    valores.append(int(input('Insira um valor: ')))

    if cont == 0:
        maior = menor = valores[cont]

    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print(f'O maior valor encontrado foi {maior} na(s) posição(ões): ', end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}... ', end='')

print()

print(f'Já o menor valor encontrado foi {menor} na(s) posição(ões): ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}... ', end='')




