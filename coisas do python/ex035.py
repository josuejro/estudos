a = float(input('Insira o comprimento da primeira reta: '))
b = float(input('Insira o comprimento da segunda reta: '))
c = float(input('Insira o comprimento da terceira reta: '))

if a + b > c and a + c > b and b + c > a:
    print('Segundo o Teorema da Desigualdade Triangular, os três comprimentos de reta inseridos \033[32mformam\033[m um triângulo!')
else:
    print('Segundo o Teorema da Desigualdade Triangular, os três comprimentos de reta inseridos \033[31mnão formam\033[m um triângulo!')