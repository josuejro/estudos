casa = float(input('Insira o valor da casa que você deseja adquirir: R$ '))
salario = float(input('Insira o valor do seu salário: R$ '))
anos = int(input('Insira a quantidade de anos que você deseja pagar: '))

mes = anos * 12
parcela = casa / mes
limite = salario * 30/100

if parcela <= limite:
    print(f'\nO valor da parcela (R$ {parcela:.2f}) não ultrapassa o limite de 30% (seu limite: R$ {limite:.2f}) do seu salário (R$ {salario}). Empréstimo aprovado!')
else:
    print(f'\nO valor da parcela (R$ {parcela:.2f}) ultrapassa o limite de 30% (seu limite: R$ {limite:.2f}) do seu salário (R$ {salario}). Empréstimo negado.')
