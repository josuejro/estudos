def leiaInt(frase):
    while True:
        dado = input(frase)

        if dado.isnumeric():
            dado = int(dado)
            return dado
        else:
            print('ERRO! Digite um valor númerico nteiro válido.')

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
