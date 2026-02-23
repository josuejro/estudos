lista = []
lista_par = []
lista_impar = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    
    if resposta in 'N':
        break

for l in lista:
    if l % 2 == 0:
        lista_par.append(l)
    else:
        lista_impar.append(l)

print('-' * 45)
print(f'A lista inicial é a seguinte: {lista}')
print()
print(f'A lista apenas com números pares é: {lista_par}')
print()
print(f'A lista apenas com os números ímpares é: {lista_impar}')
print('-' * 45)