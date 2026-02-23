import math

ang = float(input('Insira o valor do ângulo: '))

ang_rad = math.radians(ang)

sin = math.sin(ang_rad)
cos = math.cos(ang_rad)
tan = math.tan(ang_rad)

print(f'O seno, cosseno e tangente do ângulo {ang}º é:')
print(f'Seno: {sin:.4f}')
print(f'Cosseno: {cos:.4f}')
print(f'Tangente: {tan:.4f}')