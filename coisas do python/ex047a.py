import time

inicio = time.time()

for p in range(2,1000000000,2):
   ''' print(p, end=' ')
print('FIM')'''

fim = time.time()
print(f'Tempo de execução: {fim - inicio:.5f} segundos')