 # ESTRUTURA PRINCIPAL: Uma lista que vai guardar vários dicionários
pessoas = []  # Lista vazia (cada elemento será um dicionário com dados de uma pessoa)

# LOOP DE CADASTRO
while True:
    # Cria um dicionário TEMPORÁRIO para cada pessoa (ZERA a cada volta do while)
    pessoa = {}
    
    # Preenche o dicionário temporário
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    
    # Adiciona uma CÓPIA do dicionário na lista principal
    # .copy() é importante! Sem isso, todos os itens da lista apontariam para o mesmo dicionário
    pessoas.append(pessoa.copy())
    
    # Pergunta se quer continuar cadastrando
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break  # Sai do while True principal

# ============================================================
# ANÁLISE DOS DADOS (tudo abaixo executa DEPOIS que o cadastro termina)

print('=' * 50)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')

# Cálculo da média de idade
soma_idades = 0
for pessoa in pessoas:
    soma_idades += pessoa['idade']  # Acessa a chave 'idade' de cada dicionário
media_idade = soma_idades / len(pessoas)
print(f'B) A média de idade é de {media_idade:5.2f} anos.')

# Lista de mulheres
mulheres = []
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':  # Verifica a chave 'sexo'
        mulheres.append(pessoa['nome'])  # Pega só o nome
print(f'C) As mulheres cadastradas foram: {mulheres}')

# Lista de pessoas acima da média
print('D) Lista das pessoas que estão acima da média de idade:')
for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        # Imprime todas as informações dessa pessoa
        print(f'   Nome = {pessoa["nome"]}; Sexo = {pessoa["sexo"]}; Idade = {pessoa["idade"]};')
print('<< ENCERRADO >>')