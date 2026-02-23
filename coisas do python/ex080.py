lista = []

for l in range(0,5):
    n = int(input('Digite um valor: '))

    if l == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        for pos, x in enumerate(lista):
            if n <= x:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break

print(f'A lista ordenada é: {lista}')