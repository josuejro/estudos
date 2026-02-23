salario = float(input('Insira o valor do salário: '))
aumento = float (input('Insira o valor do aumento: '))
salario_aumento = salario * (aumento/100)
novo_salario = salario + salario_aumento
print(f'Após o aumento de {aumento}%, o valor do salário irá subir de R$ {salario:.2f} para R$ {novo_salario:.2f}')