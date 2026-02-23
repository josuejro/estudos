expressao = str(input('Digite uma expressão: '))
cont = 0

for caractere in expressao:
    if caractere == '(':
        cont += 1
    elif caractere == ')':
        cont -= 1

    if cont < 0:
        break

if cont == 0:
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')