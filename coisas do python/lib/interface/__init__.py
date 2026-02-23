def leiaInt(frase):
    while True:
        try:
            n = int(input(frase))
        except(ValueError, TypeError):
            print('ERRO: Por favor, digite um número válido.')
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar esse número.')
            return 0
        else:
            return n

def linha(tamanho_padrao = 42):
    return '-' * tamanho_padrao

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista_de_opcoes):
    cabeçalho('MENU PRINCIPAL')

    cont = 1
    for item in lista_de_opcoes:
        print(f'{cont} - {item}')
        cont += 1

    linha()

    opc = leiaInt('Sua opção: ')
    return opc