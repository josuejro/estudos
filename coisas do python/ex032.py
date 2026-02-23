from datetime import date

ano = int(input('Insira aqui o ano que deseja verificar (ou digite 0 para escolher o ano atual): '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano escolhido ({ano}) é bissexto.')
else:
    print(f'O ano escolhido ({ano}) não é bissexto.')