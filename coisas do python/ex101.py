def voto(nasc):
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - nasc

    if idade < 16:
        return f'Com {idade} anos, você não vota.'
    elif (idade >= 16 and idade < 18) or (idade > 65):
        return f'Com {idade} anos, seu voto é opcional.'
    else:
        return f'Com {idade} anos, seu voto é obrigatório.'
    
nasc = int(input('Digite o ano do seu nascimento: '))
print(voto(nasc))
