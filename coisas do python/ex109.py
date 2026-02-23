from utilidadeCeV import moeda

p = float(input('Digite o preço: R$ '))
t = float(input('Digite a porcentagem para acréscimo ou decréscimo: '))

print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, formato=True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, formato=True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, t, formato=True)}')
print(f'Diminuindo 10%, temos {moeda.diminuir(p, t, formato=True)}')