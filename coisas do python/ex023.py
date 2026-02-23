num = int(input('Digite um número de 0 a 9999: '))

print(f'O número {num} tem as seguintes divisões')

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

'''# 1. Transforme em string
n = str(num)

# 2. O TRUQUE: Coloque zeros na frente e fatie os últimos 4
# Ex: se n for '10', vira '00010'. Pegando os últimos 4 vira '0010'.
n = '0000' + n
n = n[-4:]  # Pega os 4 últimos caracteres

print(f'Unidade: {n[3]}')
print(f'Dezena:  {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar:  {n[0]}')'''