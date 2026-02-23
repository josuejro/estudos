#ex110
def resumo(preço=0, taxa_a=0, taxa_r=0):
    print('-' * 40)
    print('Resumo de valores'.center(40))
    print('-' * 40)

    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxa_a}% de aumento: \t{aumentar(preço, taxa_a, True)}')
    print(f'{taxa_r}% de redução: \t{diminuir(preço, taxa_r, True)}')

#ex108
def moeda(preço, símbolo='R$'):
    valor = f'{símbolo} {preço:.2f}'
    return valor.replace('.',',')

#ex107
def aumentar(preço, taxa = 10, formato=False):
    aumento = preço + (preço * taxa / 100)
    return aumento if not formato else moeda(aumento) #ex109

def diminuir(preço, taxa = 10, formato=False):
    diminuicao = preço - (preço * taxa / 100)
    return diminuicao if not formato else moeda(diminuicao) #ex109

def dobro(preço, formato=False):
    dobrar = preço * 2
    return dobrar if not formato else moeda(dobrar) #ex109

def metade(preço, formato=False):
    m = preço / 2
    return m if not formato else moeda(m) #ex109