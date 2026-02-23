def leiaDinheiro(msg):
    while True:
        entrada = input(msg).strip().replace(',', '.')
        if entrada == '':
            print('ERRO: Digite um valor.')
        else:
            try:
                valor = float(entrada)
                return valor
            except ValueError:
                print(f'ERRO: "{entrada}" não é um valor monetário válido.')

def leiaInt(frase):
    while True:
        try:
            n = int(input(frase))
        except(ValueError, TypeError):
            print('ERRO: Por favor, digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar esse número.')
            return 0
        else:
            return n

def leiaFloat(frase):
    while True:
        try:
            f = float(input(frase))
        except(ValueError, TypeError):
            print('ERRO: Por favor, digite um número real válido.')
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar esse número.')
            return 0
        else:
            return f