nome = str(input('Digite seu nome completo: '))

print(f'Seu primeiro nome é: {nome.split()[0]}')
print(f'Seu último nome é: {nome.rsplit()[-1]}')

'''
Solução computacionalmente eficiente:

n = nome.strip()

print(f'Seu primeiro nome é: {n[0]}')
print(f'Seu último nome é: {n[-1]}')

'''