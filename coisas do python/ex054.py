from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0

for t in range (1,8):
    ano_nasc = int(input(f'Insira o ano que a {t}º pessoa nasceu: '))
    idade = ano_atual - ano_nasc

    if idade >= 21:
        maior += 1
    else:
        menor += 1

print(f'{maior} pessoas tem mais de 21 anos dentre os anos de nascimento informados.')
print(f'{menor} pessoas tem mais de 21 anos dentre os anos de nascimento informados.\n')
