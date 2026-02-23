def area(l, c):
    resposta = l * c
    print(f'A área do terreno com as dimensões informadas ({l}m)x({c}m)  é de: {resposta}m².')

l = float(input('Qual a largura do terreno: '))
c = float(input('Qual o comprimento do terreno: '))

print()
area(l, c)