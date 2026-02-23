lista = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    
    if resposta in 'N':
        break

print('-' * 40)
print(f'A lista digitada tem {len(lista)} elementos.')
print()
lista.sort(reverse=True)
print(f'A lista na ordem decrescente é: {lista}')
print()
if 5 in lista:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
print('-' * 40)

