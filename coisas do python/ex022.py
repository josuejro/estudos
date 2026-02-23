nome = str(input('Digite seu nome completo: '))

print(f'Seu nome em letras maísculas fica: {nome.upper()}')
print(f'Seu nome em letras minúsculas fica: {nome.lower()}')
nome_novo = len(nome.replace(" ", ""))
print(f'Seu nome completo ({nome}) possui {nome_novo} letras')
nome_novissimo = nome.split()
print(f'Seu primeiro nome ({nome_novissimo[0]}) possui {len(nome_novissimo[0])} letras')