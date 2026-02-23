palavras = ('Aprender', 'Estudar', 'Python', 'Programar', 'Listas', 'Montanha', 'Cidade')

for p in palavras:
    print(f'\nA palavra {p.upper()} possui as seguintes vogais: ', end='')

    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')