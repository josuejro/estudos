from utilidadeCeV import moeda

p = float(input('Digite o preço: R$ '))
t = float(input('Digite a porcentagem para acréscimo ou decréscimo: '))

print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, t)}')
print(f'Diminuindo 10%, temos {moeda.diminuir(p, t)}')