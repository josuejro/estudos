from utilidadeCeV import moeda

p = float(input('Digite o valor: R$ '))
t_a = float(input('Digite a porcentagem para aumento: '))
t_r = float(input('Digite a porcentagem de redução: '))

moeda.resumo(p, t_a, t_r)