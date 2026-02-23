soma = 0
cont = 0

for s in range (1,501,2):
    if s % 3 == 0:
        soma += s
        cont += 1

print(f'A soma de todos os números solicitados ({cont}) é: {soma}')
