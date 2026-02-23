salario = float(input('Insira o valor do seu salário: R$ ').replace('.','').replace(',','.'))

if salario >= 1250.00:
    aumento_1 = salario * (10 / 100)
    novo_salario_1 = salario + aumento_1
    print(f'O seu salário de R$ {salario}, com aumento de 10%, agora será de R$ \033[1;32m{novo_salario_1:.2f}\033[m')
else:
    aumento_2 = salario * (15/100)
    novo_salario_2 = salario + aumento_2
    print(f'O seu salário de R$ {salario}, com aumento de 15%, agora será de R$ \033[1;32m{novo_salario_2:.2f}\033[m')