from random import choice, randint

num = randint(0,10)

num_user = int(input('Digite um número entre 0 e 10: '))
palpite = 1

while num != num_user:
    if num > num_user:
        print('Tente um número maior...')
    else:
        print('Tente um número menor...')

    num_user = int(input(f'Você errou, tente novamente! Digite um número: '))
    palpite += 1

print(f'Você acertou! Eu escolhi {num} e você escolheu também {num_user}!')
print(f'Você levou {palpite} vezes para acertar!')
