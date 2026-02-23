cidade = str(input('Digite o nome da sua cidade: '))

cidade_maiuscula = cidade.upper()
cidade_final = cidade_maiuscula.strip()

print(cidade_final[:5] == 'SANTO')
