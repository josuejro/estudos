from random import shuffle

alunos = ['Luana', 'Fernando', 'Mateus', 'Helena']

shuffle(alunos)

print(f'A ordem de apresentação é: {alunos}')

'''Opção complexa:

a1 = str(input('Insira o primeiro aluno:'))
a2 = str(input('Insira o segundo aluno:'))
a3 = str(input('Insira o terceiro aluno:'))
a4 = str(input('Insira o quarto aluno:'))

lista = [a1, a2, a3, a4]

sort = shuffle(lista)

print(f'A ordem da apresentação é: {sort}')
'''