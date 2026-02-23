from random import choice

aluno = ['Maria', 'Carlos', 'Antônio', 'Luísa']

sort = choice(aluno)

print(f'O(a) aluno(a) escolhido(a) foi: {sort}')

'''Opção complexa:

a1 = str(input('Insira o primeiro aluno:'))
a2 = str(input('Insira o segundo aluno:'))
a3 = str(input('Insira o terceiro aluno:'))
a4 = str(input('Insira o quarto aluno:'))

lista = [a1, a2, a3, a4]

sort = choice(lista)

print(f'O(a) aluno(a) escolhido(a) foi: {sort}')
'''