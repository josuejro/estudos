preco = float(input('Insira o preço: '))
desconto = float(input('Insira o valor do desconto: '))
preco_desconto = preco * (desconto / 100)
novo_preco = preco - preco_desconto
print(f'O valor de R$ {preco:.2f} após o desconto de {desconto:.0f}% é de R$ {novo_preco:.2f}.')