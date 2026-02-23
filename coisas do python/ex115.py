from lib import interface, arquivo
from time import sleep

arq = 'cadastro.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])

    if resposta == 1:
        interface.cabeçalho('OPÇÃO 1: PESSOAS CADASTRADAS')
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        interface.cabeçalho('OPÇÃO 2: NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = interface.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        interface.cabeçalho('Saindo do sistema... Até mais!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
        sleep(1.5)
