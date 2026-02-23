from time import sleep

# Lista de cores (Global para facilitar o acesso)
# 0: sem cor, 1: vermelho, 2: verde, 3: amarelo, 4: azul, 5: roxo, 6: branco
c = (
    '\033[m',          
    '\033[0;30;41m',   
    '\033[0;30;42m',   
    '\033[0;30;43m',   
    '\033[0;30;44m',   
    '\033[0;30;45m',   
    '\033[7;30m'       
)

def ajuda(com):
    """
    -> Acessa o manual de um comando do Python.
    """
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='') # Muda para fundo branco para o manual
    help(com)
    print(c[0], end='') # Reseta a cor
    sleep(2)

def titulo(msg, cor=0):
    """
    -> Cria um cabeçalho personalizado com cor de fundo.
    """
    tam = len(msg) + 4
    print(c[cor], end='') # Inicia a cor escolhida
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='') # Reseta a cor para o padrão
    sleep(1)

# --- PROGRAMA PRINCIPAL ---
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > ')).strip().lower()
    
    if comando == 'fim':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO!', 1)