def notas(*n, situacao=False):
    resumo = {}

    resumo['total'] = len(n)
    resumo['maior'] = max(n)
    resumo['menor'] = min(n)
    resumo['media'] = sum(n) / len(n)

    if situacao == True:
        if resumo['media'] >= 7:
            resumo['situacao'] = 'Boa'
        elif resumo['media'] >= 5:
            resumo['situacao'] = 'Razoável'
        else:
            resumo['situacao'] = 'Ruim'

    return resumo

resp = notas(4.5, 6.5, 9, situacao=False)
print(resp)