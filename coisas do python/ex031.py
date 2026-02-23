distancia = float(input('Digite a distância da sua viagem: '))

if distancia <= 200:
    valor_1 = distancia * 0.50
    print(f'A distância da sua viagem é de {distancia} km e custará R$ {valor_1:.2f}.')
else:
    valor_2 = distancia * 0.45
    print(f'A distância da sua viagem é de {distancia} km e custará R$ {valor_2:.2f}')