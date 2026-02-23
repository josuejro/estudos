soma_idade = 0
maior_idade_homem = 0
nome_velho = '' 
cont_mulher20 = 0

for p in range(1,5):
    print(f'---------------{p}º PESSOA---------------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()

    soma_idade += idade

    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_velho = nome

    if sexo == 'F':
        if idade < 20:
            cont_mulher20 += 1

print('-' * 30)
print(f'Foram informadas {cont_mulher20} mulheres com menos de 20 anos.')
print(f'O nome do homem mais velho é: {nome_velho}...')
print(f'...e sua idade é de: {maior_idade_homem} anos.')
print(f'A média das idades foi de {soma_idade / p} anos.')
print('-' * 30)
