aluno = {}

aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input(f'Digite a média do aluno {aluno['nome']}: '))

print()
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'- {k.title()} é igual a {v}')


