preco = float(input('Insira o valor a ser pago: R$ ').replace('.','').replace(',','.'))

print('--------------------------------------------')
print('Escolha a forma de pagamento: ')
print('--------------------------------------------')
print('''[1]: À vista dinheiro/cheque - 10% de desconto
[2]: À vista no cartão - 5% de desconto
[3]: 2x no cartão - preço normal
[4]: 3x ou mais no cartão - 20% de juros''')
print('--------------------------------------------')

opcao = (int(input('Digite a opção desejada: ')))

if opcao == 1:
    print(f'O preço a ser pago é de R$ {preco * 0.9:.2f}.')
elif opcao == 2:
    print(f'O preço a ser pago é de R$ {preco * 0.95:.2f}.')
elif opcao == 3:
    print(f'O preço a ser pago é de R$ {preco:.2f} em duas parcelas de R$ {preco / 2:.2f}.')
elif opcao == 4:
    parcela = int(input('\nQuantas parcelas você deseja? '))
    novo_preco = preco + (preco * 0.2)
    parcelamento = novo_preco / parcela
    print(f'\nSua compra será parcelada em {parcela}x de R$ {parcelamento} com juros.')
    print(f'Com a condição esolhida, o preço no final irá de R$ {preco:.2f} para R$ {novo_preco:.2f}')
else:
    print('Opção inválida, tente novamente.')
