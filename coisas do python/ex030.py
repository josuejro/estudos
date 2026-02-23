num = int(input('Insira um número a seguir: '))
num_final = num % 2

if num_final == 0:
    print(f'O número escolhido {num} é par!')
else:
    print(f'O número escolhido {num} é ímpar')