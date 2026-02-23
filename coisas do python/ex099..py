def maior(*num):
    print('-' * 50)
    print('Analisando os valores informados...'.center(50))

    quantidade = len(num)

    print(f'Os valores digitados foram: {num}')
    print(f'Ao todo foram informados {quantidade} valores.')

    if quantidade == 0:
        maior_valor = 0
    else:
        maior_valor = num[0]
        for n in num:
            if n > maior_valor:
                maior_valor = n
    
    print(f"O maior valor informado foi {maior_valor}")

lista_temp = []

while True:
    n = int(input('Digite um valor: '))
    lista_temp.append(n)

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer inserir outro número? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

maior(*lista_temp)


