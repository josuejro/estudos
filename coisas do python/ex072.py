
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 
        'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número de 0 a 20: '))

    if 0 <= num <= 20:
        print(f'O número digitado foi: {cont[num]}')
        break
    else:
        print('Tente novamente.')
        
