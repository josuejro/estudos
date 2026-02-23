import math

c_o = float(input('Insira o comprimento do cateto oposto: '))
c_a = float(input('Insira o comprimento do cateto adjascente: '))
# hip = math.sqrt((c_o ** 2) + (c_a ** 2))
hip = math.hypot(c_o, c_a)
print(f'O comprimento da hipotenusa é: {hip:.3f}')