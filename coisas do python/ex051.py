print('-------------------------------------------')
print('           10 TERMOS DE UMA PA'             )
print('-------------------------------------------')
p_t = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))

decimo = p_t + (10 - 1) * r

for c in range(p_t, decimo + r, r):
    print(c, end=' -> ')

print('ACABOU')