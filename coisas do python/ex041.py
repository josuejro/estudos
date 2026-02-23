from datetime import date

ano_nasc = int(input('Digite o ano do seu nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade <= 9:
    print(f'Você possui {idade} anos, logo, pertence a categoria MIRIM.')
elif 9 < idade <=14:
    print(f'Você possui {idade} anos, logo, pertence a categoria INFANTIL.')
elif 14 < idade <= 19:
    print(f'Você possui {idade} anos, logo, pertence a categoria JÚNIOR.')
elif 19 < idade <= 25:
    print(f'Você possui {idade} anos, logo, pertence a categoria SÊNIOR.')
else:
    print(f'Você possui {idade} anos, logo, pertence a categoria MASTER.')
    