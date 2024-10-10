import numpy as np
N = 3

matriz = np.zeros((N, N))

for i in range(N):
    for j in range(N):
        matriz[i][j] = int(input("Digite um número: "))

soma = 0
for i in matriz:
    soma += sum(i)

print(matriz)
print(soma)

