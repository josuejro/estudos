peso = float(input('Insira seu peso em quilogramas: ').replace(',','.'))
altura = float(input('Insira sua altura em metros: ').replace(',','.'))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print(f'Seu IMC ({imc:.1f}) indica que você está abaixo do peso.')
elif imc <= 25:
    print(f'Seu IMC ({imc:.1f}) indica que você está no peso ideal.')
elif imc <= 30:
    print(f'Seu IMC ({imc:.1f}) indica que você está com sobrepeso.')
elif imc <= 40:
    print(f'Seu IMC ({imc:.1f}) indica que você está obeso.')
else:
    print(f'Seu IMC ({imc:.1f}) indica que você está com obesidade mórbida.')