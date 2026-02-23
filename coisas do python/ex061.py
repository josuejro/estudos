termo = int(input('Informe o primeiro termo: '))
razão = int(input('Informe a razão: '))

cont = 1

while cont <= 10:
    print(f'{termo}',end='')
    print(' -> ' if cont < 10 else '', end='')
    termo += razão
    cont += 1
