n1 = float(input('Insira um número: '))
n2 = float(input('Insira outro número: '))

opcao = 0

while opcao != 5:
    print('-' * 50)
    print('                   Calculadora                   ')
    print('-' * 50)
    print('[1] - Somar;')
    print('[2] - Multiplicar;')
    print('[3] - Maior;')
    print('[4] - Novos números')
    print('[5] - Sair do programa.')
    print('-' * 50)

    opcao = int(input('Qual opção você escolhe? '))

    if opcao == 1:
        soma = n1 + n2
        print(f'O resultado da soma de {n1} e {n2} é: {soma}.')
    elif opcao == 2:
        multi = n1 * n2
        print(f'O resultado da soma de {n1} e {n2} é: {multi:.2f}.')
    elif opcao == 3:
        if n1 > n2:
            print(f'O número {n1} é maior que {n2}.')
        else:
            print(f'O número {n2} é maior que {n1}')
    elif opcao == 4:
        n1 = float(input('Insira um novo número: '))
        n2 = float(input('Insira novamente um novo número: '))
    elif opcao == 5:
        print('Encerrando...')
    else:
        print('Opção inválida! Tente novamente.')