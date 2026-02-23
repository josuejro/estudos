termo = int(input('Informe o primeiro termo: '))
razão = int(input('Informe a razão: '))

cont = 1
mais = 10
total = 0

while mais != 0:
    total = total + mais

    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razão
        cont += 1

    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar? '))

print('FIM!')