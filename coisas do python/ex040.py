n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))

media = (n1 + n2) / 2

if media >= 7.0:
    print(f'Sua média é {media:.2f}. \033[1;32mVocê foi aprovado!\033[m')
elif 7 > media >= 5:
    print(f'Sua média é {media:.2f}. \033[1;33mVocê está de recuperação.\033[m')
else:
    print(f'Sua média é {media:.2f}. \033[1;31mVocê foi reprovado.\033[m')
