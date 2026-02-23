from random import randint
from time import sleep

lista_alvo = []

def sorteia(lista_alvo):
    print(f'Os números sorteados foram: ', end='')

    for _ in range(1,6):
        n = randint(1, 10)
        lista_alvo.append(n)
        print(f'{n} ', end=' ', flush=True)
        sleep(0.4)
    
def somaPar(lista_alvo):
    soma = 0

    for v in lista_alvo:
        if v % 2 == 0:
            soma += v
    
    print(f'\nA soma dos valores pares é: {soma}')

sorteia(lista_alvo)  
somaPar(lista_alvo)