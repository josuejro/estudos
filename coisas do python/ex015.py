km = float(input('Insira quantos KM você percorreu com o carro: '))
dias = int(input('Insira o número de dias você ficou com o carro: '))
valor = (dias * 60) + (km * 0.15)
print(f'O valor a ser pago após percorrer {km:.1f} km por {dias} dias com o carro é de: R$ {valor:.2f}')