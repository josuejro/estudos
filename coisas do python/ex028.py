from random import choice, randint
import time

num = randint(0, 5)

num_user = int(input('Digite um número entre 0 e 5: '))

print('\nPensando...')
time.sleep(2)

if num_user == num:
    print(f'\nVocê adivinhou o número (Eu escolhi o número {num} e você o {num_user}) :)\n')
else:
    print(f'\nNão foi dessa vez (Eu escolhi o número {num} e você o {num_user}) :(\n')