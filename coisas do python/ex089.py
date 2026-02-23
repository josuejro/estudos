lista = []

while True:
    nome = str(input('Digite o nome do(a) aluno(a): '))
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))

    lista.append([nome, [n1, n2]])

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    
    if resposta in 'N':
        break

print(f'{"No.":<4} {"NOME":<10} {"MÉDIA":>6}')
print('-' * 30)
for indice, aluno in enumerate(lista):
    nome = aluno[0]
    notas = aluno[1]
    media = (notas[0] + notas[1]) / 2
    print(f'{indice + 1:<4} {nome:<10} {media:>6.1f}')
print('-' * 30)

while True:
    num = int(input('Gostaria de ver as notas de qual aluno? (Digitar 999 encerra o programa): '))
    if num == 999:
        break
    elif num <= len(lista):
        print()
        print(f'Aluno(a): {lista[num - 1][0]}')
        print(f'Notas: {lista[num - 1][1]}')
        print()
    else:
        print('Aluno não encontrado na lista, tente novamente!')
