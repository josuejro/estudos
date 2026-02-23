pessoas = []

while True:
    nome = str(input('Informe o nome: '))
    peso = float(input('Informe o peso: '))

    pessoas.append([nome, peso])

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    
    if resposta in 'N':
        break

maior = pessoas[0][1]
menor = pessoas[0][1]

for pessoa in pessoas:
    if pessoa[1] > maior:
        maior = pessoa[1]
    if pessoa[1] < menor:
        menor = pessoa[1]

print('-' * 45)
print(f'Total de pessoas cadastradas: {len(pessoas)}')
print()
print(f'O maior peso foi {maior}kg. Pessoa(s): ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}] ', end='')
print()
print(f'O menor peso foi {menor}kg. Pessoa(s): ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}] ', end='')
print()
print('-' * 45)