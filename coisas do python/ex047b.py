import time

inicio = time.time()

for p in range(1,1000000000):
    if p % 2 == 0:
        # print(p, end=' ')
        pass
# print('FIM')

fim = time.time()
print(f'Tempo de execução: {fim - inicio:.5f} segundos')