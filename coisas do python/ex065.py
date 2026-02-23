soma = quant = media = maior = menor = 0
resp = 'S'

while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1

    if quant == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]

media = soma / quant
print('-' * 50)
print(f'A média de todos os {quant} valores informados é {media}\n')
print(f'O maior valor lido foi {maior} e o mmenor foi {menor}.')
print('-' * 50)