a = float(input('Insira o comprimento do primeiro segmento de reta: '))
b = float(input('Insira o comprimento do segundo segmento de reta: '))
c = float(input('Insira o comprimento do terceiro segmento de reta: '))

if a + b > c and b + c > a and a + c > b:
    print('\nSegundo o Teorema da Desigualdade Triangular, os três comprimentos de reta inseridos formam um triângulo!')
    if a == b == c:
        print('Além disso, o triângulo formado com os valores dos segmentos de reta informados é do tipo EQUILÁTERO.')
    elif a != b and b != c and a != c:
        print('Além disso, o triângulo formado com os valores dos segmentos de reta informados é do tipo ESCALENO.')
    else:
        print('Além disso, o triângulo formado com os valores dos segmentos de reta informados é do tipo ISÓSCELES.')
else:
    print('\nSegundo o Teorema da Desigualdade Triangular, os três comprimentos de reta inseridos não formam um triângulo!')