lista = []

while True:
    n = int(input('Digite um valor: '))

    if n not in lista:
        lista.append(n)
        print('O valor foi adicionado com sucesso!')
    else:
        print('O valor já está na lista, tente outro valor.')
    
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    
    if resposta in 'N':
        break


lista.sort()
print(f'A lista digitada foi: {lista}')