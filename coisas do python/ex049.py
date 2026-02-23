n = int(input('Digite um número: '))

print('---------------------------------------')
print(f'A tabuada do número {n} é a seguinte:')
print('---------------------------------------')

for c in range(0,11):
    print (f'{n} x {c:2} = {n * c}')

print('---------------------------------------')