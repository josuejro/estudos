from utilidadeCeV import moeda, dado

p = dado.leiaDinheiro('Digite o valor: R$ ')
t_a = float(input('Digite a porcentagem para aumento: '))
t_r = float(input('Digite a porcentagem de redução: '))

moeda.resumo(p, t_a, t_r)