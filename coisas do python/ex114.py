import urllib.request

try:
    url = 'http://www.pudim.com.br'
    # Criamos um "pedido" personalizado com identidade de navegador
    cabecalho = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=cabecalho)
    
    # Agora abrimos o pedido em vez da URL direta
    site = urllib.request.urlopen(req)
except Exception as erro:
    print(f'\033[31mO site Pudim não está acessível no momento.\033[m')
    print(f'Motivo técnico: {erro}')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')