frase = str(input('Digite uma frase: ')).strip().upper().replace('Á','A').replace('À','A').replace('Ã','A').replace('Â','A')

print(f'A letra A aparece {frase.count('A')} vezes.')
print(f'Ela aparece pela primeira vez na seguinte posição: {frase.find('A') + 1}')
print(f'Ela aparece pela última vez na seguinte posição: {frase.rfind('A') + 1}')
