from lib.interface import cabeçalho
def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt', encoding='utf-8')
        arquivo.close()
        return True
    except:
        return False
    
def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+',encoding='utf-8')
        arquivo.close()
    except:
        print('Erro ao criar o arquivo.')
    else:
        print('Arquivo criado com sucesso.')

def lerArquivo(nome):
    try:
        arquivo = open(nome, 'rt', encoding='utf-8')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        arquivo.close()

def cadastrar(arquivo, nome_pessoa, idade_pessoa):
    try:
        objeto_arquivo = open(arquivo, 'at', encoding='utf-8')
    except:
        print('Houve um erro ao abrir o arquivo para cadastro.')
    else:
        try:
            objeto_arquivo.write(f'{nome_pessoa};{idade_pessoa}\n')
        except:
            print('Erro ao registrar os dados.')
        else:
            print('Novo registro adicionado com sucesso!')
            objeto_arquivo.close()

