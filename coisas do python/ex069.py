cont_idade18 = cont_homem = cont_mulher20 = 0

while True:
    print('-' * 30)
    print(f'{'Cadastro de pessoas':^30}')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (Masculino/Feminino): ')).strip().upper()[0]
    print('-' * 30)

    if idade >= 18:
         cont_idade18 += 1

    if sexo == 'M':
        cont_homem += 1
    if sexo == 'F' and idade <20:
            cont_mulher20 += 1
    
    opcao = str(input('Deseja continuar? [Sim/Não]: ')).strip().upper()[0]
    if opcao == 'N':
        break

print(f'{' FIM DO PROGRAMA ':-^40}')
print(f'Total de pessoas com mais de 18 anos: {cont_idade18}')
print(f'Ao todo temos {cont_homem} homens cadastrados.')
print(f'E temos {cont_mulher20} mulheres com menos de 20 anos.')
