from time import sleep

def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p = abs(p)

    if i < f:
        while i <= f:
            print(i, end=' ', flush=True)
            sleep(0.3)
            i = i + p

    else:
        while i >= f:
            print(i, end=' ', flush=True)
            sleep(0.3)
            i = i - p
    print('FIM!') 

i = int(input('Digite de onde quer começar a contagem: '))
f = int(input('Digite onde quer terminar a contagem: '))
p = int(input('Digite o intervalo da contagem: '))

contador(i, f, p)
