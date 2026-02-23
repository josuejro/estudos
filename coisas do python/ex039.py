from datetime import date

nasc = int(input('Digite o ano do seu nascimento: '))
gen = str(input('Qual o seu gênero (Masculino ou Feminino)? ')).strip().upper()

if gen == 'FEMININO':
    print('Seu alistamento não é obrigatório! Caso deseje, busque a Junta Militar mais próxima!')
else:
    atual = date.today().year
    idade = atual - nasc
    ano_alist = nasc + 18

    if idade == 18:
        print(f'Você possui {idade} anos, é hora de buscar a Junta Militar de sua cidade para realizar o alistamento militar.')
    elif idade < 18:
        print(f'Você tem {idade} anos, ainda faltam {ano_alist - atual} anos para você se alistar.')
        print(f'Você deverá buscar a Junta Militar para seu alistamento em {atual+(ano_alist - atual)}.')
    else:
        print(f'Você tem {idade} anos e está {atual - ano_alist} anos atrasado para se alistar, caso ainda não tenha se alistado.')
        print(f'Você devia ter buscado a Junta militar para seu alistamento em {atual - (atual - ano_alist)}, caso já não tenha ido.')
