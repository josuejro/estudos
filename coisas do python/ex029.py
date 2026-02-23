velocidade = int(input('Insira a velocidade que você está andando: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você estava acima do limite de 80 km/h ({velocidade} km/h) e foi multado.')
    print(f'O valor da multa é: R$ {multa:.2f}')
    print('Dirija com segurança!')
else:
    print(f'Você está abaixo da velocidade permitida, parabéns. Boa condução!')