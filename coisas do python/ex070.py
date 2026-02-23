total = total_1000 = menor = cont = 0
menor_nome = ''

print('-' * 40)
print(f"{'LOJA SUPER BARATÃO':^40}")
print('-' * 40)

while True:
    produto = str(input('Nome do Produto: ')).strip().title()
    preco = float(input('Preço: R$ ').replace(',', '.'))

    cont += 1
    total += preco

    if preco > 1000:
        total_1000 += 1

    if cont == 1 or preco < menor:
        menor = preco
        menor_nome = produto

    resp = ' ' 
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        print(f"{' FIM DO PROGRAMA ':-^40}")
        break

print('\n' + '=' * 40)
print(f"{'RESUMO DA COMPRA':^40}")
print('=' * 40)
print(f"Total gasto:.................. R$ {total:>10.2f}")
print(f"Produtos acima de R$1000:..... {total_1000:>10}")
print(f"Produto mais barato:.......... {menor_nome}, (R$ {menor:.2f})")
print('=' * 40)