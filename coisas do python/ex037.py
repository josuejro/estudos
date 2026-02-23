numero = int(input('Insira o número que deseja converter: '))

print('-' * 35)
print('Escolha para qual base numérica você deseja converter:')
print('-' * 20)
print('''[1]: converter para BINÁRIO
[2]: converter para OCTAL
[3]: converter para HEXADECIMAL''')
print('-' * 35)
opcao = int(input('Digite a opção: '))
print('-' * 35)

if opcao == 1:
    print(f'O número {numero} em binário é: {bin(numero)[2:]}')
elif opcao == 2:
    print(f'O número {numero} em octal é: {oct(numero)[2:]}')
elif opcao == 3:
    print(f'O número em {numero} em hexadecimal é: {hex(numero)[2:]}')
else:
    print('Opção inválida, tente novamente.')