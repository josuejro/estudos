frase = str(input('Digite uma frase qualquer: '))

f_tratada = (frase).upper().strip().replace(' ','')
f_junta = f_tratada
f_inversa = ''

for f in range(len(f_tratada) - 1, - 1, - 1):
    f_inversa += f_junta[f]

#print(f'\nO que eu juntei: {f_junta}\n')
#print(f'\nO que eu inverti: {f_inversa}\n')

if f_junta == f_inversa:
    print(f'A frase "{frase}" é um palíndromo!')
else:
    print(f'A frase "{frase}" não é um palíndromo.')