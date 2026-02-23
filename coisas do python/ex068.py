from random import randint

cont = 0

while True:
    computador = randint(0, 10)

    usuario = int(input('Digite um número de 0 a 10: '))
    x = str(input('Escolhe par ou impar? ')).strip().upper()[0]

    soma = usuario + computador

    if (soma % 2 == 0 and x == 'P') or (soma % 2 == 1 and x == 'I'):
        print('Usuário venceu!! Continue jogando!\n')
        cont += 1
    else:
        print(f'Você perdeu. O computador escolheu {computador} e você escolheu {usuario} :(')
        print(f'Partidas vencidas: {cont}')
        break

